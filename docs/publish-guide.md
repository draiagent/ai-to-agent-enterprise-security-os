# GitHub 發布設定與步驟

Repo 名稱：`ai-to-agent-enterprise-security-os`。版本與 Description、Topics 的單一來源為 [project.json](../project.json)。

1. 授權已決定為保留所有權利（All rights reserved），法律權利人為 AI Coach 益力康陳董；原先「程式 MIT、文件 CC BY 4.0」的提案未採用。
2. Owner 為 draiagent，可見性公開（2026-10-13 確認）。
3. 已用保留所有權利的完整聲明替換根目錄 LICENSE，並更新 project.json、README 與 NOTICE。第三方工具仍依各自授權。
4. 執行兩項檢查：`python3 examples/policy_demo.py`、`python3 tests/check_docs.py`。重新生成檔案雜湊後再打包。
5. 建立 Repo，將 ZIP 解壓後內層專案目錄的所有內容上傳，保留 assets 與文件相對路徑。不要只上傳 ZIP。
6. 使用 project.json 的 Description 與 Topics；沒有實際網站就不要填 Website。
7. 檢查線上 README 圖片、相對連結、LICENSE 與完整檔案，再按需求建立 v1.1.0 tag 與 Release，貼入 Release Notes。

發布後才把 remote_status 改為 published，並記錄真實 Repo URL 與 commit。文件與離線測試通過，不代表企業端點、連接器或模型執行環境已通過資安驗收。
