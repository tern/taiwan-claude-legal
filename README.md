# Taiwan Claude Legal 🇹🇼⚖️

這是一個專為 [Claude for Legal](https://anthropic.com) 設計的擴充知識庫與 Playbook 專案，旨在讓 Claude 能夠完美理解並應用台灣《民法》及其他核心法規。本專案內建自動化更新機制，每日自動同步法務部最新條文。

## 專案特色
- **自動化更新**：每日同步法務部全國法規資料庫 Open API，確保法規為最新狀態。
- **Claude for Legal 專屬格式**：條文自動轉換為 Claude 易於檢索的 Markdown 與結構化 JSON。
- **專業 Playbook**：內建針對台灣法律實務的提示詞（如合約審查、NDA、風險評估）。

## 快速安裝 (60 秒教學)

若您已經具備 Claude 的 CLI 或外掛環境，可直接將此 repo 作為 knowledge plugin 載入：

1. 複製本專案：
   ```bash
   git clone https://github.com/tern/taiwan-claude-legal.git
   cd taiwan-claude-legal
   ```
2. 將其加入 Claude Plugins（指令依您的 Claude 環境而定）：
   ```bash
   claude plugins add ./taiwan-claude-legal
   ```

## 如何在 Claude 內使用台灣民法技能

載入 Playbook 後，您可以在對話中直接引用特定的情境：

- **合約審查**：`@playbook taiwan-civil-code "請幫我審查這份僱傭合約，並列出違反台灣民法的風險。"`
- **NDA 起草**：`@playbook taiwan-civil-code "請根據台灣法律起草一份單向保密協議。"`

## 自動更新機制說明
本專案包含一組 GitHub Actions Workflow (`.github/workflows/update-laws.yml`)。
它會每天在 UTC 06:00 (台灣時間下午 2:00) 執行 `scripts/update_laws.py`。
該腳本會抓取法務部 Open API 的資料，比對 `laws/civil-code/full.json`，如果發現修法，會自動 Commit 變更並產生 Changelog。

## 免責聲明 ⚠️
本專案提供之法規資料與 Claude AI 的分析結果 **僅供參考，不構成正式的法律意見**。
AI 可能會產生幻覺或誤解法理。任何具體的法律行為、合約簽署或訴訟，請務必諮詢領有台灣執照的專業律師。
