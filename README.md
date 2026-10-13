# Enterprise Security OS｜企業自主資安作業系統

**AI to Agent Autonomous Security Governance Framework**

![版本](https://img.shields.io/badge/version-1.1.0-blue)

讓 Agent 在企業授權下，持續負責整體數位環境的發現、監控、調查、處置、驗證與改善。

本版為 **1.1.0 方法論與參考規格**，附離線政策示範；**不是已部署的資安產品**。版本日期 2026-10-13。完整中繼資料見 [project.json](project.json)。

![企業自主資安 Agent VAC 八步驟](assets/enterprise-security-vac.png)

[圖卡全集](assets/README.md) · [工具與授權](docs/tool-catalog.md) · [使用方式](docs/usage.md) · [社群介紹](docs/social-post.md)

## 為什麼需要
企業設備、帳號、資料、雲端、程式與 AI 工具各有管理者，安全事件卻會跨越部門。本框架把責任、權限、工具與證據接成同一條事件流程，支援 Agent 在明確政策內自主執行。

## 架構與範圍
VAD 定義全貌與信任邊界；VAC 定義八步事件工作；治理層掌握授權、急停、證據與成本。
八職責包含資產、端點、網路雲端、身分SaaS、資料機密、程式供應鏈、Agent工具與復原。可先用一個協調 Agent，加上受限工具與獨立驗證實現。

本版提供可採用的規格與範本，未提供生產連接器、持續監控或自動修復。適合企業導入規劃、教學與概念驗證；不得直接視作合規認證、端點清白證明或生產防禦部署。

## 快速開始
1. 讀取 [核心定位](docs/01-core.md) 及 [VAD](vad/architecture.md)。
2. 指定一組企業擁有且授權的資產與責任人。
3. 用 [VAC](vac/incident-card.md) 建事件，依 [授權模型](policies/authority.md) 凍結邊界。
4. 先用合成資料執行離線示範，Python 3.10+，僅標準函式庫，無安裝依賴：
   `python3 examples/policy_demo.py`
5. 查看 [SEC-001](cases/SEC-001.md) 與 [驗收規格](tests/acceptance.md)，再規劃唯讀環境接入。

示範輸入：合法A0讀取、範圍外資產、過期授權、缺證據、重大變更。輸出：ALLOW／DENY／UNKNOWN／REVIEW。示範程式不連接任何電腦、不採取系統操作、不接受真實憑證。

## 本版新增
- 最新深黑紫青 VAC 圖卡、10 張方法論知識圖卡與文字對照。
- 四項共用工具：Wazuh、Wazuh MCP、Trivy、OPA；僅保留一份本專案資安營運 Skill。
- 工具選型、授權來源、版本候選與待驗證欄位。
- 使用教學、社群文章及可填寫事件範本。

## 八步交付索引
| 工作步驟 | 文件 |
|---|---|
| 1 核心定位與方法論 | [docs/01-core.md](docs/01-core.md) |
| 2 VAD總架構 | [vad/architecture.md](vad/architecture.md) |
| 3 VAC與自主授權 | [vac/incident-card.md](vac/incident-card.md)、[policies/authority.md](policies/authority.md) |
| 4 執行元件與工具規格 | [docs/04-runtime.md](docs/04-runtime.md)、[技能](skills/security-operations/SKILL.md) |
| 5 導入路線 | [docs/05-rollout.md](docs/05-rollout.md) |
| 6 案例與驗收 | [cases/SEC-001.md](cases/SEC-001.md)、[tests/acceptance.md](tests/acceptance.md)、[報告母版](evidence/report-template.md) |
| 7 Repo發布文件 | [CHANGELOG](CHANGELOG.md)、[CONTRIBUTING](CONTRIBUTING.md)、[Release Notes](docs/release-notes.md) |
| 8 整體自我審查 | [review](docs/08-review.md)、[離線結果](evidence/offline-results.json) |

## 驗收與限制
文件審查與離線示範結果見第8步。SEC-001真實端點仍為UNKNOWN，尚缺Defender原始紀錄等證據。Windows命令未在企業環境執行；四項工具的上游授權已查閱；固定版本授權、相依套件與相容性尚未完成部署驗收。

本版框架與NIST、OWASP作設計參考對照，未宣稱認證；官方來源詳見 [sources](docs/sources.md)。

## 後續路線
依P1–P4逐步接入唯讀端點、影子分析、單一可逆處置與持續治理。新連接器與可寫入操作須通過對應驗收後才擴展。

## 授權與發布
本 repo 採保留所有權利（All rights reserved），見 [LICENSE](LICENSE)，**不是開源授權**；法律權利人為 AI Coach 益力康陳董。已建立公開 Repo 與 tag v1.1.0，未建立 GitHub Release。品牌署名不等於第三方素材或上游工具的權利認定。第三方來源見 [NOTICE](NOTICE.md)。

## 作者品牌署名
AI Coach 益力康陳董 x CGM Coach 血糖教練 | 2026 AI to Agent | 2027 AI to AGI Agent
