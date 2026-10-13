# 01｜核心定位與方法論定稿

規格基準：1.1.0｜2026-10-13｜方法論定稿；企業部署未驗證。

## 一句話定位
Enterprise Security OS（企業自主資安作業系統）讓 Agent 在企業授權與證據治理下，持續負責整體數位環境的安全營運：發現、監控、偵測、調查、決策、處置、驗證與改善。

「OS」是協調層的架構名稱，不是替換 Windows／Linux 的作業系統，也不是已完成的商用資安平台。本版交付方法論、任務規格、政策範本及可執行的離線驗收示範。

## 問題與價值
企業的設備、帳號、SaaS、資料、程式與 AI 工具由不同人管理，事件易落在責任縫隙。本系統以事件為主線連接資產、權限、工具和業務結果，讓日常工作有責任人、有處理期限、有結案證據。

直觀理解：Agent 是值班安全營運員；工具是感測器與操作介面；政策是值班授權；證據是交接簿；企業主管保留風險接受與重大變更決定權。

## 凍結項目
| 項目 | 本版定義 |
|---|---|
| Repo | ai-to-agent-enterprise-security-os |
| 中文／英文 | 企業自主資安作業系統／Enterprise Security OS |
| 副標 | AI to Agent Autonomous Security Governance Framework |
| 系統組成 | Agent + Tools + Policies + Evidence + Human Governance |
| VAD | Visual Agent Design：定義責任、資料流與信任邊界 |
| VAC | Visual Agent Card：定義可執行、可驗收的事件任務 |
| 責任覆蓋 | 八個職責；可由一個協調 Agent 加 Skills 實現 |
| 任務循環 | Discover → Monitor → Detect → Investigate → Decide → Respond → Verify → Improve |
| 自主授權 | A0–A4；依每次行動判定，不對 Agent 永久授予整級權限 |
| 核心治理 | Human Sovereignty + Evidence + Task Economics |

## 三層理解
1. VAD：保護哪些業務與資產，由誰負責。
2. VAC／Runtime：每個事件如何完成、遇錯如何修正。
3. Governance：誰能授權、如何停止、如何證明與衡量。

Capability 是技術可達能力；Authority 是授權範圍；Autonomy 是授權內可自行決策的程度。三者各自記錄，不能互相替代。

## 範圍與限制
涵蓋端點、網路、雲端、帳號、資料、SaaS、軟體供應鏈、Agent／MCP／Skills 與備份復原。OT、醫療設備等特殊系統先納入資產及責任清冊，變更須另建經驗證的專用程序。第三方服務只管理本企業合法持有的租戶與帳號權限。

本版不包含生產連接器、常駐監控服務或已驗證的自動修復。沒有企業資料時不可推定環境安全，也不可把離線示範當成資安效能實測。

## 成功定義
事件在授權內完成，威脅與業務功能分別驗證，證據可追溯；未完成項目有責任人與期限。結案不得只依模型自評。安全性、可用性、成本與人工負擔同時衡量。

