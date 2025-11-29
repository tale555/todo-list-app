# 無料デプロイガイド

## 🎯 無料でデプロイできるサービス

以下のサービスが無料プランで利用可能です：

1. **Render**（推奨）⭐
   - 無料プランあり
   - GitHub連携で簡単
   - 15分間アクセスがないとスリープ（無料プランの制限）

2. **Railway**
   - 無料プランあり（$5分のクレジット/月）
   - GitHub連携で簡単
   - 小規模アプリなら無料で使える

3. **PythonAnywhere**
   - 無料プランあり
   - 制限あり（外部URLアクセスは1時間に1回のみ）

## 🚀 Renderへのデプロイ（推奨）

### ステップ1: GitHubにコードをアップロード

1. GitHubアカウントを作成（まだの場合）
2. 新しいリポジトリを作成
3. コードをアップロード：

```bash
cd todo_list_app
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/your-repo-name.git
git push -u origin main
```

### ステップ2: Renderアカウントの作成

1. https://render.com/ にアクセス
2. 「Get Started for Free」をクリック
3. GitHubアカウントでサインアップ

### ステップ3: 新しいWebサービスを作成

1. Renderダッシュボードで「New +」→「Web Service」をクリック
2. GitHubリポジトリを接続
3. 以下の設定を行う：

   - **Name**: `todo-list-app`（任意の名前）
   - **Region**: `Singapore`（日本に近い地域）
   - **Branch**: `main`
   - **Root Directory**: `todo_list_app`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn main:app --bind 0.0.0.0:$PORT`

### ステップ4: 環境変数の設定

Renderダッシュボードの「Environment」セクションで以下を設定：

#### 必須の環境変数

```env
# Google Sheets API
GOOGLE_CREDENTIALS_JSON=ここにcredentials.jsonの内容を貼り付け
SPREADSHEET_ID=your_spreadsheet_id_here
SHEET_NAME=Todo

# Flask設定
SECRET_KEY=ランダムな文字列（後述）
FLASK_DEBUG=False
PORT=10000

# LINE Messaging API
LINE_CHANNEL_ACCESS_TOKEN=your_channel_access_token
LINE_USER_ID=your_user_id
```

#### SECRET_KEYの生成方法

PowerShellで以下を実行：

```powershell
-join ((48..57) + (65..90) + (97..122) | Get-Random -Count 32 | ForEach-Object {[char]$_})
```

または、オンラインツールを使用：
- https://randomkeygen.com/

#### GOOGLE_CREDENTIALS_JSONの設定方法

1. `configs/credentials.json`ファイルを開く
2. ファイルの内容をすべてコピー
3. Renderの環境変数`GOOGLE_CREDENTIALS_JSON`に貼り付け

**重要**: JSONの内容をそのまま貼り付けてください（改行も含めて）

### ステップ5: デプロイの実行

1. 「Create Web Service」をクリック
2. デプロイが完了するまで待つ（5-10分）
3. 提供されたURL（例: `https://todo-list-app.onrender.com`）にアクセス

### ステップ6: LINE Webhook URLの更新

1. デプロイされたURLをコピー（例: `https://todo-list-app.onrender.com`）
2. LINE Developers Consoleにアクセス
3. 「Messaging API」タブを開く
4. 「Webhook URL」を更新：
   ```
   https://todo-list-app.onrender.com/line/webhook
   ```
5. 「検証」ボタンをクリック
6. 「Webhookの利用」をONにする

## 🚂 Railwayへのデプロイ

### ステップ1: Railwayアカウントの作成

1. https://railway.app/ にアクセス
2. GitHubアカウントでサインアップ

### ステップ2: 新しいプロジェクトを作成

1. Railwayダッシュボードで「New Project」をクリック
2. 「Deploy from GitHub repo」を選択
3. リポジトリを選択

### ステップ3: 設定

1. 「Settings」タブで以下を設定：
   - **Root Directory**: `todo_list_app`
   - **Start Command**: `gunicorn main:app --bind 0.0.0.0:$PORT`

### ステップ4: 環境変数の設定

「Variables」タブで以下を設定（Renderと同様）：

```env
GOOGLE_CREDENTIALS_JSON=...
SPREADSHEET_ID=...
SHEET_NAME=Todo
SECRET_KEY=...
FLASK_DEBUG=False
LINE_CHANNEL_ACCESS_TOKEN=...
LINE_USER_ID=...
```

### ステップ5: デプロイ

自動的にデプロイが開始されます。完了後、提供されたURLにアクセスできます。

## 📋 デプロイ前のチェックリスト

- [ ] GitHubにコードをアップロード
- [ ] `requirements.txt`が最新
- [ ] `Procfile`が存在（Render用）
- [ ] `runtime.txt`が存在（Pythonバージョン指定）
- [ ] 環境変数を準備
- [ ] Google Sheets APIの認証ファイルを準備
- [ ] LINE Messaging APIのトークンとUser IDを準備

## ⚠️ 無料プランの制限

### Render（無料プラン）

- **スリープ**: 15分間アクセスがないとスリープ
- **起動時間**: スリープ後、初回アクセス時に30秒程度かかる
- **制限**: 月750時間まで

### Railway（無料プラン）

- **クレジット**: $5分のクレジット/月
- **制限**: 小規模アプリなら無料で使える

## 🔧 トラブルシューティング

### エラー: 認証ファイルが見つからない

- 環境変数`GOOGLE_CREDENTIALS_JSON`が正しく設定されているか確認
- JSONの内容が完全にコピーされているか確認（改行も含めて）

### エラー: アプリケーションが起動しない

- ログを確認（Render/Railwayのダッシュボードで確認可能）
- `requirements.txt`に必要なパッケージが含まれているか確認
- `Procfile`の内容が正しいか確認

### エラー: LINE Webhookが動作しない

- Webhook URLが正しいか確認（`/line/webhook`が含まれているか）
- RenderのURLが正しいか確認（デプロイ後のURLを使用）

## 📝 次のステップ

デプロイが完了したら：

1. 動作確認を行う
2. LINE Webhook URLを更新
3. 通知機能をテスト

## 💡 ヒント

- **Render**: 無料プランでも十分使えるが、スリープする点に注意
- **Railway**: 小規模アプリなら無料で使える
- **カスタムドメイン**: 有料プランで利用可能（無料プランでは提供されたURLを使用）

---

**質問や問題があれば**: TROUBLESHOOTING.mdを参照してください。

