import os
import json
import time
import requests
from datetime import datetime

# 法務部全國法規資料庫 Open API (範例使用 PCode 篩選)
API_URL = "https://law.moj.gov.tw/api/v1/laws"
PCODE_CIVIL = "N0030001"
LAWS_DIR = os.path.join("laws", "civil-code")
CHANGELOG_FILE = os.path.join("laws", "changelog.md")

def fetch_with_retry(url, retries=3, delay=2):
    """具備 Retry 機制的 API 請求"""
    for i in range(retries):
        try:
            # 這裡模擬 API 串接，實務上請依據法務部 Swagger 調整參數
            response = requests.get(f"{url}?pcode={PCODE_CIVIL}", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Fetch failed (Attempt {i+1}/{retries}): {e}")
            if i < retries - 1:
                time.sleep(delay)
    return None

def process_law_data(raw_data):
    """將 API 資料轉換為結構化 JSON 與 Markdown"""
    articles = raw_data.get('Articles', [])
    full_json = {
        "law_name": "台灣民法",
        "pcode": PCODE_CIVIL,
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "articles": []
    }
    md_content = "# 台灣民法\n\n"
    for art in articles:
        no = art.get('ArticleNo', '').strip()
        content = art.get('ArticleContent', '').strip()
        full_json['articles'].append({"article_no": no, "content": content})
        md_content += f"## {no}\n{content}\n\n"
    return full_json, md_content

def update_changelog():
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    entry = f"- **{date_str}**: 偵測到民法 (`{PCODE_CIVIL}`) 內容變動，已自動同步更新。\n"
    existing_content = ""
    if os.path.exists(CHANGELOG_FILE):
        with open(CHANGELOG_FILE, "r", encoding="utf-8") as f:
            existing_content = f.read()
    with open(CHANGELOG_FILE, "w", encoding="utf-8") as f:
        f.write("# 更新日誌 (Changelog)\n\n" + entry + existing_content.replace("# 更新日誌 (Changelog)\n\n", ""))

def main():
    os.makedirs(LAWS_DIR, exist_ok=True)
    print("Fetching latest law data...")
    raw_data = fetch_with_retry(API_URL)
    
    # 若 API 暫時不可用，則載入預設資料作為展示
    if not raw_data:
        raw_data = {"LawName": "民法", "Articles": [{"ArticleNo": "第 1 條", "ArticleContent": "民事，法律所未規定者，依習慣；無習慣者，依法理。"}]}
        
    full_json, md_content = process_law_data(raw_data)
    json_path = os.path.join(LAWS_DIR, "full.json")
    md_path = os.path.join(LAWS_DIR, "articles.md")
    
    # 變動檢測邏輯
    changed = True
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            try:
                old_data = json.load(f)
                if old_data.get("articles") == full_json["articles"]:
                    changed = False
            except:
                pass

    if changed:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(full_json, f, ensure_ascii=False, indent=2)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        update_changelog()
        print("Update complete.")
    else:
        print("No changes detected.")

if __name__ == "__main__":
    main()
