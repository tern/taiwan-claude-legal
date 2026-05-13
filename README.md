# Taiwan Claude Legal 🇹🇼⚖️

![Version](https://img.shields.io/badge/version-v1.0.0-blue)

> **來源說明**：本專案基於 [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) 架構進行台灣本地化擴充與自動化改進。

## Anthropic 推出全球最強法律生產力助手 —— 現在有台灣專屬版本！

各位台灣律師與法務朋友，大家好！

Anthropic 最近釋出開源工具 **Claude for Legal**，被譽為「全世界最親民的法律助手」。它能大幅加速日常重複性工作，讓您把時間留給真正需要專業判斷的策略性任務，真正成為您身邊最得力的 AI 法律幫手。

### 它能幫您做到：
- **快速閱讀與審查合約**：即時抓取關鍵條款與潛在風險。
- **協助起草法律文件**：針對法律回應與意見提供初步草稿。
- **建構法律表單**：自動化處理訴訟索賠或行政表格。
- **流程自動化**：自動追蹤到期日、續約通知。
- **生態系整合**：無縫連接 Slack、DocuSign、Microsoft 365 等您日常使用的工具。

全部操作都在 Claude 介面內完成，無需頻繁切換視窗。

---

## 台灣律師專屬強化版（由本地開發者維護）

我們特別打造了 **taiwan-claude-legal**，已內建最新《民法》全文（每日自動從法務部更新），並優化為繁體中文與台灣實務情境：

- **法條自動比對**：進行合約風險分析時，會自動比對《民法》第 71 條（強制規定）、第 252 條（違約金酌減）等關鍵條文。
- **合規檢查**：支援 PDPA（個人資料保護法）初步檢查。
- **在地法規支援**：未來將陸續加入《公司法》、《勞基法》等常用法規。

---

## 安裝方式（60 秒完成）

### 1. Claude Code (終端機模式)
如果您正在使用 Anthropic 的 [Claude Code CLI](https://github.com/anthropics/claude-code)，請直接在對話框中輸入：

```bash
/plugins add https://github.com/tern/taiwan-claude-legal
```

### 2. Claude Cowork 桌面版
直接在 Claude 對話框輸入：

```bash
@Library/Application Support/Claude/claude-code-vm/2.1.128/claude plugins add https://github.com/tern/taiwan-claude-legal
```

---

## 適合台灣的常見場景
- **商業合約審閱與談判**：快速識別顯失公平或違反強制規定之條款。
- **法律文件起草**：NDA、保密協議、僱傭合約之初步起草。
- **準據法檢查**：跨境交易中的台灣法準據法檢核。
- **即時合規稽核**：確保文件符合法務部最新頒佈之條文。

過去需要花數小時的重複工作，現在只需幾分鐘就能完成，讓您有更多時間專注在客戶策略、談判與高價值法律服務上。

---

## 免責聲明與重要提醒 ⚠️
這是您的**專業 AI 法律幫手**，所有分析結果仍需由具台灣律師資格的專業人士進行最終審核。AI 輔助工具無法取代您的專業判斷，其目的是幫助您更快、更準、更輕鬆地完成例行工作。

任何具體法律問題請務必諮詢領有台灣執照的專業律師。
