# 工具、技能與授權清單

查閱日期：2026-10-13。這是選型紀錄，並非已安裝清單或經驗證的部署 lockfile。

## 四項工具，各負責一種角色

| 工具 | 唯一主要角色 | VAC | 上游授權 | 原始來源 |
|---|---|---|---|---|
| Wazuh | 端點與日誌安全營運平台 | 01、02、03、06、07 | GPLv2；依賴另有各自授權 | [Repo](https://github.com/wazuh/wazuh)、[LICENSE](https://github.com/wazuh/wazuh/blob/main/LICENSE) |
| Wazuh MCP Server | Agent 存取 Wazuh 的社群連接器 | 04；其他步驟共用介面 | MIT | [Repo](https://github.com/gensecaihq/Wazuh-MCP-Server)、[LICENSE](https://github.com/gensecaihq/Wazuh-MCP-Server/blob/main/LICENSE) |
| Trivy | 軟體供應鏈與設定掃描 | 03、07 | Apache-2.0 | [Repo](https://github.com/aquasecurity/trivy)、[LICENSE](https://github.com/aquasecurity/trivy/blob/main/LICENSE) |
| OPA | 獨立政策決策引擎 | 05 | Apache-2.0 | [Repo](https://github.com/open-policy-agent/opa)、[LICENSE](https://github.com/open-policy-agent/opa/blob/main/LICENSE) |

Wazuh MCP 是社群專案，不是 Wazuh 官方連接器。OPA 回傳政策決策，不會自行替執行器落實權限；仍需自行實作驗證決策與參數的受限執行器。這四項工具也不包含完整的持續 Agent Runtime。

免費開源授權不等於無條件使用、免費雲端或免費模型 API。部署與再散布須遵守各元件的完整條款、通知與原始碼義務；不能把四個工具統一改標成本專案授權。本 Repo 僅引用來源，不附第三方程式或二進位檔。

## 2026 版本候選

| 工具 | 前序查核記錄的候選 | 上游發布入口 | 部署狀態 |
|---|---|---|---|
| Wazuh | 4.14.8 | [Releases](https://github.com/wazuh/wazuh/releases) | 未安裝、未鎖定 |
| Wazuh MCP Server | 5.0.0 | [Releases](https://github.com/gensecaihq/Wazuh-MCP-Server/releases) | 未安裝、未鎖定 |
| Trivy | 0.74.0 | [Releases](https://github.com/aquasecurity/trivy/releases) | 未安裝、未鎖定 |
| OPA | 1.21.2 | [Releases](https://github.com/open-policy-agent/opa/releases) | 未安裝、未鎖定 |

以上保留本次討論的候選版號，不宣稱最新版或互相相容。發布頁可讀不代表已完成固定 tag 的 LICENSE 與供應鏈查驗。正式接入前，逐項填入 tag、commit SHA、下載 SHA-256、該 commit 授權全文、相依授權、支援平台與測試紀錄。

## 技能不重複

本 Repo 僅提供一份 [enterprise-security-operations](../skills/security-operations/SKILL.md)，統一負責事件流程與產物。Wazuh、Trivy 是工具，MCP 是介面，OPA 是政策引擎，均不再另包一份功能重複的 Skill。

Trail of Bits 的 fp-check 僅適合程式發現項目的誤報審查，未列為必裝，也未複製進本 Repo。Velociraptor 可能提供進階鑑識，本版未列入，以減少第一階段平台數量；並非因其授權不允許免費使用。

01–08 重複引用同一工具表示共用能力，不代表安裝多套。缺少的企業政策、服務健康探針與回復程序須由導入團隊補上。
