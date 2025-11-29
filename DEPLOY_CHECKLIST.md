# デプロイ前チェックリスト

## ✅ デプロイ前に確認すること

### 1. ファイルの準備

- [ ] `requirements.txt`が最新（すべての依存パッケージが含まれている）
- [ ] `Procfile`が存在（Render用）
- [ ] `runtime.txt`が存在（Pythonバージョン指定）
- [ ] `.gitignore`に`credentials.json`が含まれている（セキュリティ）

### 2. 環境変数の準備

以下の環境変数を準備してください：

#### Google Sheets API
- [ ] `GOOGLE_CREDENTIALS_JSON` - credentials.jsonの内容（JSON形式）
- [ ] `SPREADSHEET_ID` - スプレッドシートID
- [ ] `SHEET_NAME` - シート名（例: `Todo`）

#### Flask設定
- [ ] `SECRET_KEY` - ランダムな文字列（32文字以上推奨）
- [ ] `FLASK_DEBUG` - `False`（本番環境）

#### LINE Messaging API
- [ ] `LINE_CHANNEL_ACCESS_TOKEN` - Channel Access Token
- [ ] `LINE_USER_ID` - User ID

### 3. SECRET_KEYの生成

PowerShellで以下を実行：

```powershell
-join ((48..57) + (65..90) + (97..122) | Get-Random -Count 32 | ForEach-Object {[char]$_})
```

または、オンラインツールを使用：
- https://randomkeygen.com/

### 4. GOOGLE_CREDENTIALS_JSONの取得

1. `configs/credentials.json`ファイルを開く
2. ファイルの内容をすべてコピー（改行も含めて）
3. 環境変数として設定する準備をする

### 5. GitHubへのアップロード

- [ ] GitHubアカウントを作成
- [ ] リポジトリを作成
- [ ] コードをアップロード

```bash
cd todo_list_app
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/your-repo-name.git
git push -u origin main
```

### 6. デプロイ先の選択

- [ ] Render（推奨）- 無料プランあり
- [ ] Railway - 無料プランあり
- [ ] その他

## 📋 デプロイ手順

詳細は `FREE_DEPLOYMENT_GUIDE.md` を参照してください。

## ⚠️ 注意事項

1. **認証ファイル**: 絶対にGitHubにコミットしない
2. **SECRET_KEY**: 本番環境では必ずランダムな文字列を設定
3. **環境変数**: 機密情報はすべて環境変数で管理
4. **LINE Webhook URL**: デプロイ後に更新が必要

## 🔧 デプロイ後の確認

- [ ] アプリが正常に起動しているか
- [ ] Todo一覧が表示されるか
- [ ] 新規Todoを作成できるか
- [ ] LINE Webhook URLを更新したか
- [ ] LINE通知が動作するか

