# Taiwan Claude Legal 🇹🇼⚖️

This project provides a Taiwan-specific legal extension for AI agents (like Claude or Gemini), focusing on the Taiwan Civil Code, contract review, and legal drafting within the Taiwan jurisdiction.

## Project Overview

- **Purpose**: Automates the ingestion of Taiwan laws and provides specialized skills/playbooks for legal analysis.
- **Agent Support**: Optimized for both **Claude (Cowork/Code)** and **Gemini CLI**. It utilizes the standard Skill system to provide consistent legal auditing across different agent environments.
- **Key Focus**: 
    - **Taiwan Civil Code**: Automated updates from the Ministry of Justice (MOJ).
    - **Contract Review**: Highlighting risks related to mandatory provisions (Art. 71) and liquidated damages (Art. 252).
    - **Legal Drafting**: Focused on Traditional Chinese (Taiwan) and local legal practices.
- **Tech Stack**: 
    - **Python**: Used for the law crawler (`scripts/update_laws.py`).
    - **Markdown/JSON**: Stores the knowledge base (`laws/`).
    - **GitHub Actions**: Automates law synchronization and project updates.

## Key Directories & Files

- `laws/civil-code/`: Contains the parsed Taiwan Civil Code in Markdown (`articles.md`) and JSON (`full.json`) formats.
- `skills/taiwan-legal-audit/`: Contains `SKILL.md`, which provides a structured workflow for performing legal audits and contract reviews.
- `scripts/update_laws.py`: A Python scraper that fetches the latest laws from the Taiwan MOJ website.
- `.claude-plugin/`: Configuration for integration with Anthropic's Claude ecosystem.

## Development & Maintenance

### Law Updates
The repository is designed to keep laws up-to-date automatically.
- **Command**: `python3 scripts/update_laws.py`
- **Dependencies**: `requests`, `beautifulsoup4`, `lxml` (see `requirements.txt`).
- **Automation**: Managed via GitHub Workflows (`.github/workflows/update-laws.yml`).

### Commands & Skills
When modifying the legal logic or auditing criteria:
- Update `skills/taiwan-legal-audit/SKILL.md` for auditing logic and core principles.
- Ensure all outputs remain in **Traditional Chinese (Taiwan)**.

## Usage Conventions

1. **Cite Articles**: Always cite specific Taiwan Civil Code articles (e.g., "依據民法第 71 條...").
2. **Disclaimer**: Every legal analysis must include the standard disclaimer:
   > *注意：以上分析僅供參考，不構成正式法律意見。實際法律行為請諮詢專業律師。*
3. **Language**: Strictly use Traditional Chinese as used in Taiwan legal practice.

# Claude Cowork 官方知識（來自 Anthropic 官方文件）

## 基本定義與特色
- Claude Cowork 是 Anthropic 推出的 agentic AI 系統，專為「知識工作」（knowledge work）設計。
- 它把 Claude Code 的 agentic 架構帶到 Claude Desktop（macOS / Windows），不需要開終端機。
- 你只要描述「最終想要的結果」，Claude 就會自動規劃、執行多步驟任務，並直接操作你的本地檔案、資料夾和應用程式，最後產出完整交付物（deliverable）。
- 與一般 Chat 不同：Cowork 可以直接讀寫本地檔案、協調子代理（sub-agents）、平行執行工作流。
- 與 Claude Code 不同：Cowork 專注非程式碼的桌面知識工作（文件、研究、簡報、資料整理等）。

## 主要功能
- 直接本地檔案存取（讀/寫/建立/整理檔案）
- 子代理協調與平行工作流
- 專業輸出（Excel 含公式、PowerPoint、格式化文件）
- 排程任務（Scheduled tasks）：設定一次，自動定期執行
- Projects：把相關任務組織成獨立工作區（含專屬檔案、指令、記憶）
- 手機指派任務（Pro/Max 用戶）：手機發任務，桌面執行
- 支援檔案類型：Word、Excel、PowerPoint、PDF、CSV、Markdown、程式碼、圖片、Jupyter Notebook 等
- Plugins 與 Skills：可自訂角色專屬行為

## 如何運作（Task Loop）
1. 你描述任務 → Claude 分析並產生計畫
2. 拆解成子任務（必要時平行執行）
3. 在你的電腦隔離環境執行程式/指令
4. 直接把結果寫入你的檔案系統
5. 你可以隨時 steer（引導/修正）

Claude Desktop 必須保持開啟。任務執行中會顯示進度與推理，你可以中途介入。

## 安全性與限制
- 你必須明確授權資料夾與連接器（connectors）
- 刪除檔案前一定會要求確認
- 不適合受管制工作負載（HIPAA、FedRAMP 等）
- Team/Enterprise 有額外管理控制與 OpenTelemetry 監控

# Claude Cowork Plugins 官方知識（來自 Anthropic 官方文件與 knowledge-work-plugins GitHub）

## Plugins 是什麼？
- Plugins 是 Anthropic 為 Claude Cowork 設計的「一鍵打包擴充套件」。
- 每個 Plugin 會把 **Skills（技能）**、**Connectors（連接器）**、**Slash Commands（斜線指令）** 和 **Sub-agents（子代理）** 打包成一個完整套件。
- 目的：讓 Claude 立刻變成特定角色/部門的專家（不需要每次都從頭提示），並直接連接你常用的工具（Slack、Notion、HubSpot、Jira、Microsoft 365、Snowflake 等）。
- 與一般 Skills 不同：Plugin 是「完整解決方案」，安裝後自動載入相關技能與連接器。
- 也兼容 Claude Code。

## 官方 Plugins 列表（Anthropic 開源的 11 個核心插件）
這些是 Anthropic 團隊自己使用並開源的，GitHub 儲存庫：https://github.com/anthropics/knowledge-work-plugins

| Plugin 名稱              | 主要用途                                                                 | 主要 Connectors（連接器）                          |
|--------------------------|--------------------------------------------------------------------------|----------------------------------------------------|
| **productivity**        | 管理任務、日曆、日常工作流、個人情境，減少重複說明                     | Slack, Notion, Asana, Linear, Jira, Monday, ClickUp, Microsoft 365 |
| **sales**               | 研究潛在客戶、準備通話、檢視銷售管線、撰寫 outreach、建立競爭 battlecards | Slack, HubSpot, Close, Clay, ZoomInfo, Notion, Jira, Fireflies, Microsoft 365 |
| **customer-support**    | 分類 ticket、撰寫回覆、打包 escalation、研究客戶情境、轉化為知識庫文章   | Slack, Intercom, HubSpot, Guru, Jira, Notion, Microsoft 365 |
| **product-management**  | 撰寫規格、規劃 roadmap、合成使用者研究、更新利害關係人、追蹤競爭對手     | Slack, Linear, Asana, Monday, ClickUp, Jira, Notion, Figma, Amplitude, Pendo, Intercom, Fireflies |
| **marketing**           | 撰寫內容、規劃活動、強制品牌語調、競爭分析、跨頻道效能報告               | Slack, Canva, Figma, HubSpot, Amplitude, Notion, Ahrefs, SimilarWeb, Klaviyo |
| **legal**               | 審閱合約、分類 NDA、合規檢查、風險評估、準備會議、撰寫模板回覆           | Slack, Box, Egnyte, Jira, Microsoft 365           |
| **finance**             | 準備 journal entries、對帳、產生財務報表、差異分析、支援審計             | Snowflake, Databricks, BigQuery, Slack, Microsoft 365 |
| **data**                | 查詢、視覺化、解讀資料集（寫 SQL、統計分析、建 dashboard）               | Snowflake, Databricks, BigQuery, Definite, Hex, Amplitude, Jira |
| **enterprise-search**   | 跨公司所有工具（email、chat、文件、wiki）進行單一查詢                   | Slack, Notion, Guru, Jira, Asana, Microsoft 365   |
| **bio-research**        | 連接 preclinical 研究工具與資料庫（文獻搜尋、基因組分析等）             | PubMed, BioRender, bioRxiv, ClinicalTrials.gov 等 |
| **cowork-plugin-management** | 建立新 Plugin 或自訂現有 Plugin（專門給你打造客製化插件的工具）        | —                                                  |

**注意**：目前（2026/5）官方已陸續新增 design、engineering、human-resources、operations、pdf-viewer 等插件，以及財務服務、法律專屬插件（可另外從 GitHub 其他 repo 安裝）。Plugin 庫持續成長。

## Plugins 如何運作？
1. **安裝與自訂**：
   - 透過左側選單的 **"Customize"** -> **"Browse plugins"** 探索與安裝。
   - 安裝後點擊 "Customize" 並按下 **"Let's go"**，Claude 會開啟一個專屬 Cowork 任務協助你調整 Skills 與 Connectors。
   - **Plugin Create 工具**：內建工具，可讓你從頭開始或使用模板建立自訂 Plugin。
2. **自動化執行**：
   - 安裝後，Plugin 會自動把 Skills、Commands、Connectors 載入。
   - Claude 會**自動**根據任務情境使用相關 Skills（Progressive Disclosure）。
3. **使用者介面觸發**：
   - 你可以用 `/` 或點擊對話框中的 **"+"** 按鈕明確呼叫指令或 Skills。
   - 也可用 `/plugin-name:command` 呼叫特定 Slash Commands。
4. **組成架構**：
   - 所有東西都是**檔案形式**（Markdown + JSON），儲存在本地機器。
   - **Plugin 目錄結構**：
     ```
     plugin-name/
     ├── .claude-plugin/plugin.json     # 資訊清單
     ├── .mcp.json                      # 連接器設定
     ├── commands/                      # Slash 指令
     └── skills/                        # 自動觸發的領域知識
     ```

## 安全性與執行模型
- **本地 MCP 伺服器**：部分 Plugin 包含本地運行的 MCP 伺服器，權限等同於本地程式。請僅安裝信任來源的 Plugin。
- **雲端連接器（Cloud Connectors）**：雖然 Cowork 在本地執行，但連接器（如 Google Drive, Slack）是透過 **Anthropic 雲端** 存取，而非透過你的本地網路。
- **企業管理（Team/Enterprise）**：
  - 管理員可透過 Marketplace 分發 Plugin（可設定為強制安裝）。
  - 管理員可停用本地 MCP 伺服器或限制安裝權限。
  - 使用者無法編輯由組織管理的 Plugin。

## 如何安裝與使用（官方步驟）
### 在 Claude Desktop / Cowork：
1. 開啟 Claude Desktop → 切換到 **Cowork** 標籤。
2. 左側點擊 **Customize**（自訂）。
3. 點擊 **Browse plugins** → 搜尋並點擊 **Install**。
4. 也可上傳自己或同事分享的 .zip Plugin 檔案。

### 在 Claude Code（CLI）：
```bash
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install sales@knowledge-work-plugins   # 範例
```

請在回答任何與 Claude Cowork 相關問題時，優先使用以上知識，並與 Gemini CLI 的能力做比較。
