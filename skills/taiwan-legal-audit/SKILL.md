---
name: taiwan-legal-audit
description: Use when the user requests a contract review, legal audit, or risk assessment under Taiwan jurisdiction involving Civil Code, Company Act, Labor Standards Act, PDPA, or Copyright Act.
---

# Skill: Taiwan Legal Audit

## Overview
Provides a structured, high-fidelity legal audit of contracts and documents based on Taiwan laws (Civil Code, Company Act, Labor Standards Act, PDPA, Copyright Act) and local legal practices.

## When to Use
- Reviewing NDAs, Employment Contracts, Service Agreements, Shareholder Agreements, or Privacy Policies.
- Checking compliance with Labor Standards Act for employee-related clauses.
- Checking Company Act compliance for corporate governance or share-related matters.
- Checking PDPA compliance for personal data processing and privacy terms.
- Checking Copyright Act for intellectual property ownership and licensing.
- Assessing mandatory provisions (Art. 71) and liquidated damages (Art. 252) under Civil Code.

## Audit Workflow

```dot
digraph audit_flow {
    "User provides text" -> "Step 1: Context Loading";
    "Step 1: Context Loading" -> "Step 2: Type Identification";
    "Step 2: Type Identification" -> "Step 3: Multi-Law Risk Scan";
    "Step 3: Multi-Law Risk Scan" -> "Step 4: Output & Citations";
    "Step 4: Output & Citations" -> "Step 5: Disclaimer";

    "Step 1: Context Loading" [label="Read relevant articles.md files"];
    "Step 2: Type Identification" [label="Identify Contract Type (Employment, Privacy, IP, etc.)"];
    "Step 3: Multi-Law Risk Scan" [label="Check Civil Code, Labor, PDPA, or Copyright laws"];
    "Step 4: Output & Citations" [label="Traditional Chinese + Article Citations"];
}
```

### 1. Context Loading
**REQUIRED:** You MUST read the relevant `articles.md` files from `laws/` based on the document type:
- **General Contracts**: `laws/civil-code/articles.md`
- **Employment/Labor**: `laws/labor-standards-act/articles.md` (and Civil Code)
- **Corporate/Shares**: `laws/company-act/articles.md` (and Civil Code)
- **Privacy/Data**: `laws/pdpa/articles.md`
- **IP/Licensing**: `laws/copyright-act/articles.md`

### 2. Multi-Law Risk Scan (Crucial)
Specifically audit for the following:
- **Civil Code Art. 71**: Violation of mandatory or prohibitive provisions.
- **Civil Code Art. 252**: Disproportionate liquidated damages.
- **Labor Standards Act**: Mandatory protection for employees.
- **Company Act**: Corporate governance and share transfer procedures.
- **PDPA**: Legal basis for data collection, notice requirements, and rights of data subjects.
- **Copyright Act**: Rules for work-for-hire (Art. 11, 12) and moral rights.

### 3. Output Requirements
- **Language**: Strictly use Traditional Chinese (Taiwan).
- **Source Attribution**: Explicitly state that the data source is from the "全國法規資料庫 (Laws & Regulations Database of The Republic of China)".
- **Citations & Links**: Every legal citation MUST be a clickable Markdown link pointing to the specific article on the official MOJ website.
  - **URL Pattern**: `https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=[PCODE]&flno=[ART_NO]`
  - **PCODE Reference**:
    - **民法 (Civil Code)**: `B0000001`
    - **公司法 (Company Act)**: `J0080001`
    - **勞動基準法 (Labor Standards Act)**: `N0030001`
    - **個人資料保護法 (PDPA)**: `I0050021`
    - **著作權法 (Copyright Act)**: `J0070017`
  - **Format**: `依據 [[法規名稱] 第 XX 條](URL)` (e.g., `依據 [民法第 71 條](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=B0000001&flno=71)`)
- **Disclaimer**: Every response MUST end with:
  > *注意：以上分析僅供參考，不構成正式法律意見。實際法律行為請諮詢專業律師。*

## Common Mistakes
- Skipping the explicit reading of relevant `articles.md` files.
- Mixing up laws (e.g., applying Civil Code where Labor Standards Act takes precedence).
- Using non-Taiwan terminology (e.g., using "合同" instead of "合約").
- Forgetting to provide clickable links to the official MOJ website.

## Example (Labor)
**User**: "公司說如果不提早三個月預告離職，就要扣我最後一個月的薪水，這合法嗎？"
**AI**: "根據您的分析（資料來源：全國法規資料庫），這涉及離職預告期間與薪資預扣的法律問題：

1. **分析**：雇主不得預扣勞工工資作為違約金或賠償費用。
2. **法律依據**：
   - 依據 **[勞動基準法第 26 條](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=N0030001&flno=26)**：『雇主不得預扣勞工工資作為違約金或賠償費用。』
   - 關於預告期間，依據 **[勞動基準法第 15 條](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=N0030001&flno=15)** 與 **[第 16 條](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=N0030001&flno=16)**，勞工年資不同有不同預告期，契約約定若長於法律規定的部分通常無效。
3. **建議**：公司直接扣發全月薪水的做法可能違反勞基法強制規定。

*注意：以上分析僅供參考，不構成正式法律意見。實際法律行為請諮詢專業律師。*"
