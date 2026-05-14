# Taiwan Claude Legal 🇹🇼⚖️

![Version](https://img.shields.io/badge/version-1.0.0-blue)

> **來源說明**：
> 1. 本專案基於 [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) 架構進行台灣本地化擴充。
> 2. 法律條文資料來源為 [**全國法規資料庫 (Laws & Regulations Database of The Republic of China)**](https://law.moj.gov.tw/)。

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

我們特別打造了 **taiwan-claude-legal**，已內建最新《民法》、《公司法》及《勞動基準法》全文（每日自動從法務部更新），並優化為繁體中文與台灣實務情境：

- **法條自動比對**：進行合約風險分析時，會自動比對《民法》第 71 條（強制規定）、第 252 條（違約金酌減）等關鍵條文。
- **勞資風險審閱**：內建《勞動基準法》支援，自動檢核加班費、預告期間及薪資扣留等合規風險。
- **公司治理支援**：內建《公司法》支援，協助處理股權轉讓、董事會決議等法規核對。
- **合規檢查**：支援 PDPA（個人資料保護法）初步檢查。


---

## 安裝方式（60 秒完成）

### 1. Claude Code (終端機模式)
如果您正在使用 Anthropic 的 [Claude Code](https://github.com/anthropics/claude-code)，在終端機執行：

```bash
claude plugin marketplace add tern/taiwan-claude-legal
claude plugin install taiwan-claude-legal
```

**安裝後可用的指令：**

| 指令 | 說明 |
|------|------|
| `/taiwan-claude-legal:audit <合約文字>` | 快速觸發台灣法律風險審查 |

也可以直接在對話中描述需求，plugin 內建的 `taiwan-legal-audit` skill 會自動根據文件類型（勞動、公司、隱私、IP）載入對應法條並分析。

### 2. Claude Desktop（Cowork 桌面版）

**方式一：透過 UI 安裝**
1. 開啟 Claude Desktop，切換至 **Cowork** 標籤。
2. 點擊左側 **Customize** > **Browse plugins**。
3. 搜尋「taiwan-claude-legal」並點擊安裝。

若搜尋不到，請先透過終端機加入 marketplace，再回到 UI 安裝：
```bash
claude plugin marketplace add tern/taiwan-claude-legal
```

**方式二：上傳 .zip 安裝**

下載本專案的 zip（GitHub → Code → Download ZIP），在 **Browse plugins** 頁面選擇上傳檔案。

### 3. Claude Code（本機測試）
若想在不安裝的情況下直接試用，可透過 `--plugin-dir` 旗標載入：

```bash
git clone https://github.com/tern/taiwan-claude-legal
claude --plugin-dir ./taiwan-claude-legal
```

### 3. Gemini CLI (終端機模式)
如果您使用的是 Gemini CLI，您可以將此技能安裝至您的全域環境或特定專案中：

**安裝指令：**
```bash
# 全域安裝（推薦，任何專案皆可使用）
gemini skills install https://github.com/tern/taiwan-claude-legal

# 僅安裝於目前專案（workspace 模式）
gemini skills install https://github.com/tern/taiwan-claude-legal --scope workspace
```

**如何使用：**
安裝完成後，您不需要手動啟動。只要在對話中詢問與台灣法律或合約審閱相關的問題（例如：「幫我審閱這份合約」），Gemini 就會根據任務需求**自動觸發**此技能。

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
