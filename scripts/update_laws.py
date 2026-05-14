import os
import json
import time
import warnings
import requests
import urllib3
from datetime import datetime
from bs4 import BeautifulSoup

# === 設定 ===
LAWS_TO_TRACK = [
    {"pcode": "B0000001", "name": "台灣民法", "dir": "civil-code"},
    {"pcode": "J0080001", "name": "台灣公司法", "dir": "company-act"},
    {"pcode": "N0030001", "name": "台灣勞動基準法", "dir": "labor-standards-act"},
    {"pcode": "I0050021", "name": "個人資料保護法", "dir": "pdpa"},
    {"pcode": "J0070017", "name": "著作權法", "dir": "copyright-act"}
]

LAWS_ROOT_DIR = "laws"
CHANGELOG_FILE = os.path.join(LAWS_ROOT_DIR, "changelog.md")

def fetch_law_html(pcode):
    url = f"https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode={pcode}"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; TaiwanClaudeLegalBot/1.0)"}
    for attempt in range(3):
        try:
            r = requests.get(url, headers=headers, timeout=15)
            r.raise_for_status()
            return r.text
        except requests.exceptions.SSLError:
            # 法務部網站偶發憑證鏈問題，降級為加密但不驗證模式
            print(f"⚠️  {pcode} SSL 驗證失敗，以無驗證模式重試（連線仍加密）")
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)
                    r = requests.get(url, headers=headers, timeout=15, verify=False)
                r.raise_for_status()
                return r.text
            except Exception as e:
                print(f"Fetch failed for {pcode} (attempt {attempt+1}): {e}")
        except Exception as e:
            print(f"Fetch failed for {pcode} (attempt {attempt+1}): {e}")
        time.sleep(2)
    raise Exception(f"無法取得法規網頁: {pcode}")

def parse_law_html(html):
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
    
    # 3. 備用匹配
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

    # 去重
    seen_nos = set()
    unique_articles = []
    for art in articles:
        if art["article_no"] not in seen_nos:
            unique_articles.append(art)
            seen_nos.add(art["article_no"])

    return unique_articles

def update_law(law_info):
    pcode = law_info["pcode"]
    name = law_info["name"]
    target_dir = os.path.join(LAWS_ROOT_DIR, law_info["dir"])
    os.makedirs(target_dir, exist_ok=True)

    print(f"🚀 正在抓取: {name} (PCode: {pcode})...")

    try:
        html = fetch_law_html(pcode)
        articles = parse_law_html(html)
    except Exception as e:
        print(f"❌ 錯誤 ({name}): {e}")
        return False

    if len(articles) < 5:
        print(f"⚠️ {name} 解析條文過少，跳過更新")
        return False

    full_json = {
        "law_name": name,
        "pcode": pcode,
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_articles": len(articles),
        "articles": articles
    }

    json_path = os.path.join(target_dir, "full.json")
    md_path = os.path.join(target_dir, "articles.md")

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
        
        md_content = f"# {name}（最新更新：{full_json['last_updated']}）\n\n"
        current_ch = ""
        for art in articles:
            if art["chapter"] and art["chapter"] != current_ch:
                current_ch = art["chapter"]
                md_content += f"\n## {current_ch}\n\n"
            md_content += f"### {art['article_no']}\n{art['content']}\n\n"
        
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        
        print(f"✅ {name} 更新完成！共 {len(articles)} 條")
        return True
    else:
        print(f"✅ {name} 無變動")
        return False

def main():
    os.makedirs(LAWS_ROOT_DIR, exist_ok=True)
    updated_laws = []

    for law in LAWS_TO_TRACK:
        if update_law(law):
            updated_laws.append(law["name"])
        time.sleep(1) # 友善爬蟲

    if updated_laws:
        date_str = datetime.now().strftime("%Y-%m-%d")
        entry = f"- **{date_str}**：已自動更新法規：{', '.join(updated_laws)}\n"
        
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

if __name__ == "__main__":
    main()
