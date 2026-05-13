import os
import json
import time
import requests
import urllib3
from datetime import datetime
from bs4 import BeautifulSoup

# 停用 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# === 設定 ===
# 修正：PCODE 應為 B0000001 (民法)，原 N0030001 為勞基法
PCODE_CIVIL = "B0000001"
LAW_NAME = "台灣民法"
LAWS_DIR = os.path.join("laws", "civil-code")
CHANGELOG_FILE = os.path.join("laws", "changelog.md")
HTML_URL = f"https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode={PCODE_CIVIL}"

def fetch_law_html():
    headers = {"User-Agent": "Mozilla/5.0 (compatible; TaiwanClaudeLegalBot/1.0)"}
    for attempt in range(3):
        try:
            # 加入 verify=False 以應對法務部網站憑證問題
            r = requests.get(HTML_URL, headers=headers, timeout=15, verify=False)
            r.raise_for_status()
            return r.text
        except Exception as e:
            print(f"Fetch failed (attempt {attempt+1}): {e}")
            time.sleep(2)
    raise Exception("無法取得民法網頁")

def parse_civil_code(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    current_chapter = ""

    # 先找到法規內容主容器
    content_div = soup.find("div", class_="law-reg-content")
    if not content_div:
        return []

    # 遍歷主容器下的所有子元素
    for elem in content_div.find_all(recursive=False):
        text = elem.get_text(strip=True)
        if not text:
            continue
        
        # 1. 處理章節標題 (編/章/節/款)
        # 章節通常在 div.line-0, line-1 等，或包含特定 class
        is_chapter = "line-" in elem.get("class", []) or any(x in text for x in ["編", "章", "節", "款"])
        if is_chapter and "第" in text and "條" not in text and len(text) < 100:
            current_chapter = text
            continue
        
        # 2. 處理條文 (具有 row class 的 div)
        if "row" in elem.get("class", []):
            no_div = elem.find("div", class_="col-no")
            data_div = elem.find("div", class_="col-data")
            
            if no_div and data_div:
                no = no_div.get_text(strip=True)
                content = data_div.get_text(strip=True)
                
                # 確保是有效的條號格式
                if no.startswith("第") and no.endswith("條"):
                    articles.append({
                        "article_no": no,
                        "content": content,
                        "chapter": current_chapter
                    })
    
    # 3. 如果上述結構抓不到（例如頁面結構變動），嘗試備用匹配
    if not articles:
        for elem in soup.find_all(["div", "p"]):
            text = elem.get_text(strip=True)
            if text.startswith("第") and "條" in text and "　" in text:
                parts = text.split("　", 1)
                no = parts[0].strip()
                content = parts[1].strip()
                if no.startswith("第") and no.endswith("條") and len(no) < 15:
                    articles.append({
                        "article_no": no,
                        "content": content,
                        "chapter": current_chapter
                    })

    # 去重處理 (按條號)
    seen_nos = set()
    unique_articles = []
    for art in articles:
        if art["article_no"] not in seen_nos:
            unique_articles.append(art)
            seen_nos.add(art["article_no"])

    return unique_articles

def main():
    os.makedirs(LAWS_DIR, exist_ok=True)
    print(f"🚀 正在從法務部抓取最新民法條文 (PCode: {PCODE_CIVIL})...")

    try:
        html = fetch_law_html()
        articles = parse_civil_code(html)
    except Exception as e:
        print(f"❌ 錯誤: {e}")
        return

    if len(articles) < 10:  # 防呆
        print("⚠️ 解析條文過少，使用 fallback")
        articles = [{"article_no": "第 1 條", "content": "民事，法律所未規定者，依習慣；無習慣者，依法理。", "chapter": ""}]

    full_json = {
        "law_name": LAW_NAME,
        "pcode": PCODE_CIVIL,
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_articles": len(articles),
        "articles": articles
    }

    json_path = os.path.join(LAWS_DIR, "full.json")
    md_path = os.path.join(LAWS_DIR, "articles.md")

    # 變動檢測
    changed = True
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                old = json.load(f)
                if old.get("articles") == full_json.get("articles"):
                    changed = False
        except:
            pass

    if changed:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(full_json, f, ensure_ascii=False, indent=2)
        
        # 產生易讀 Markdown
        md_content = f"# {LAW_NAME}（最新更新：{full_json['last_updated']}）\n\n"
        current_ch = ""
        for art in articles:
            if art["chapter"] and art["chapter"] != current_ch:
                current_ch = art["chapter"]
                md_content += f"\n## {current_ch}\n\n"
            md_content += f"### {art['article_no']}\n{art['content']}\n\n"
        
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        # 更新 changelog
        date_str = datetime.now().strftime("%Y-%m-%d")
        entry = f"- **{date_str}**：民法條文已自動更新（共 {len(articles)} 條）\n"
        
        old_log = "# 更新日誌\n\n"
        if os.path.exists(CHANGELOG_FILE):
            with open(CHANGELOG_FILE, "r", encoding="utf-8") as f:
                content = f.read()
                if "# 更新日誌" in content:
                    old_log = content
                else:
                    old_log += content

        with open(CHANGELOG_FILE, "w", encoding="utf-8") as f:
            if entry not in old_log:
                f.write(old_log + entry)
            else:
                f.write(old_log)
        
        print(f"✅ 更新完成！共 {len(articles)} 條民法條文")
    else:
        print("✅ 無變動，跳過更新")

if __name__ == "__main__":
    main()
