# Taiwan Claude Legal 🇹🇼⚖️

> **來源說明**：本專案是基於 [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) 的架構進行台灣本地化擴充與自動化改進。

這是一個專為 [Claude for Legal](https://github.com/anthropics/claude-for-legal) 設計的擴充知識庫與 Playbook 專案，旨在讓 Claude 能夠完美理解並應用台灣《民法》及其他核心法規。

## 專案特色
- **HTML 穩定抓取**：使用 BeautifulSoup 解析法務部網頁，比 API 更有保障。
- **每日自動同步**：透過 GitHub Actions 每日自動檢查最新修法。
- **繁體中文優化**：所有條文、提示詞與回覆均採用台灣法律慣用語。
- **即時知識庫**：條文自動轉換為 Claude 易於檢索的 Markdown 結構。

## 快速安裝 (60 秒教學)

請確保您已安裝 [Claude CLI](https://github.com/anthropics/claude-code)。

1. **複製專案到本地**：
   ```bash
   git clone https://github.com/tern/taiwan-claude-legal.git
   cd taiwan-claude-legal
   ```

2. **將專案加入為 Claude 插件**：
   ```bash
   claude plugins add .
   ```

## 如何使用

載入後，您可以在對話中直接使用：

- **合約風險分析**：`@playbook taiwan-civil-code "請分析這份合約中關於違約金的條款是否合理？"`
- **法規諮詢**：`"依據台灣民法，口頭合約是否有效？"`
- **文件草擬**：`@playbook taiwan-civil-code "請幫我草擬一份符合台灣法律的簡易借貸協議。"`

## 自動更新機制
本專案透過 `.github/workflows/update-laws.yml` 進行排程更新：
- **時間**：每日台灣時間 14:00 (UTC 06:00)。
- **邏輯**：抓取 [法務部全國法規資料庫](https://law.moj.gov.tw/)，若有更新則自動產出新的 `full.json` 與 `articles.md` 並 commit 回 repo。

## 免責聲明 ⚠️
本專案提供之內容僅供參考，**不構成任何形式的法律建議**。法律分析受個案事實影響極大，任何具體法律問題請務必諮詢領有台灣執照的專業律師。
