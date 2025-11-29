# デプロイガイド

このガイドでは、Todo List Appをサーバーで公開する手順を説明します。

## 📋 目次

1. [デプロイ先の選択](#デプロイ先の選択)
2. [Renderへのデプロイ](#renderへのデプロイ)
3. [Railwayへのデプロイ](#railwayへのデプロイ)
4. [Herokuへのデプロイ](#herokuへのデプロイ)
5. [デプロイ後の設定](#デプロイ後の設定)

---

## デプロイ先の選択

以下のいずれかのサービスを使用できます：

- **Render**（推奨）: 無料プランあり、GitHub連携で簡単
- **Railway**: 無料プランあり、GitHub連携で簡単
- **Heroku**: 有料プラン（無料プランは廃止）

---

## Renderへのデプロイ

### ステップ1: Renderアカウントの作成

1. https://render.com/ にアクセス
2. 「Get Started for Free」をクリック
3. GitHubアカウントでサインアップ

### ステップ2: 新しいWebサービスを作成

1. Renderダッシュボードで「New +」→「Web Service」をクリック
2. GitHubリポジトリを接続
3. 以下の設定を行う：
   - **Name**: `todo-list-app`（任意の名前）
   - **Region**: `Singapore`（日本に近い地域）
   - **Branch**: `main`（または`master`）
   - **Root Directory**: `todo_list_app`（プロジェクトフォルダ名）
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn main:app`

### ステップ3: 環境変数の設定

Renderダッシュボードの「Environment」セクションで以下を設定：

```env
GOOGLE_CREDENTIALS_PATH=configs/credentials.json
SPREADSHEET_ID=your_spreadsheet_id_here
SHEET_NAME=Sheet1
SECRET_KEY=your_secret_key_here（ランダムな文字列を生成）
FLASK_DEBUG=False
```

**重要**: 
- `SECRET_KEY`はランダムな文字列を生成してください（例: `openssl rand -hex 32`）
- 認証ファイル（`credentials.json`）は後でアップロードします

### ステップ4: 認証ファイルのアップロード

Renderでは直接ファイルをアップロードできないため、以下のいずれかの方法を使用：

**方法A: 環境変数として設定（推奨）**

1. 認証ファイル（`credentials.json`）を開く
2. ファイルの内容をコピー
3. Renderダッシュボードの「Environment」で新しい環境変数を追加：
   - **Key**: `GOOGLE_CREDENTIALS_JSON`
   - **Value**: コピーしたJSONの内容を貼り付け
4. アプリケーション起動時に環境変数からファイルを作成するコードを追加（後述）

**方法B: GitHubにコミット（非推奨）**

セキュリティ上の理由から、認証ファイルをGitHubにコミットするのは推奨されません。

### ステップ5: デプロイの実行

1. 「Create Web Service」をクリック
2. デプロイが完了するまで待つ（数分かかります）
3. 提供されたURL（例: `https://todo-list-app.onrender.com`）にアクセス

---

## Railwayへのデプロイ

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
   - **Start Command**: `gunicorn main:app`

### ステップ4: 環境変数の設定

「Variables」タブで以下を設定：

```env
GOOGLE_CREDENTIALS_PATH=configs/credentials.json
SPREADSHEET_ID=your_spreadsheet_id_here
SHEET_NAME=Sheet1
SECRET_KEY=your_secret_key_here
FLASK_DEBUG=False
```

### ステップ5: 認証ファイルの設定

Railwayでは環境変数として設定する方法が推奨されます（Renderと同様）。

---

## Herokuへのデプロイ

### ステップ1: Heroku CLIのインストール

1. https://devcenter.heroku.com/articles/heroku-cli からインストール
2. コマンドラインで `heroku login` を実行

### ステップ2: Herokuアプリの作成

```bash
cd todo_list_app
heroku create your-app-name
```

### ステップ3: 環境変数の設定

```bash
heroku config:set GOOGLE_CREDENTIALS_PATH=configs/credentials.json
heroku config:set SPREADSHEET_ID=your_spreadsheet_id_here
heroku config:set SHEET_NAME=Sheet1
heroku config:set SECRET_KEY=your_secret_key_here
heroku config:set FLASK_DEBUG=False
```

### ステップ4: 認証ファイルのアップロード

```bash
# 認証ファイルをbase64エンコードして環境変数に設定
heroku config:set GOOGLE_CREDENTIALS_JSON="$(cat configs/credentials.json | base64)"
```

### ステップ5: デプロイ

```bash
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

---

## デプロイ後の設定

### 認証ファイルを環境変数から作成する

環境変数から認証ファイルを作成するコードを`main.py`に追加：

```python
import os
import json

# 環境変数から認証ファイルを作成（Render/Railway用）
if os.getenv('GOOGLE_CREDENTIALS_JSON'):
    credentials_json = os.getenv('GOOGLE_CREDENTIALS_JSON')
    credentials_path = os.path.join('configs', 'credentials.json')
    os.makedirs('configs', exist_ok=True)
    with open(credentials_path, 'w') as f:
        f.write(credentials_json)
```

### 動作確認

1. デプロイされたURLにアクセス
2. Todo一覧が表示されることを確認
3. 新規Todoを作成して動作確認

---

## トラブルシューティング

### エラー: 認証ファイルが見つからない

- 環境変数`GOOGLE_CREDENTIALS_JSON`が正しく設定されているか確認
- アプリケーション起動時に認証ファイルが作成されるコードが実行されているか確認

### エラー: スプレッドシートIDが設定されていない

- 環境変数`SPREADSHEET_ID`が正しく設定されているか確認
- スプレッドシートIDが完全なURLではなく、ID部分だけであることを確認

### エラー: アプリケーションが起動しない

- ログを確認（Render/Railway/Herokuのダッシュボードで確認可能）
- `requirements.txt`に必要なパッケージが含まれているか確認
- `Procfile`の内容が正しいか確認

---

## セキュリティの注意事項

1. **認証ファイル**: 絶対にGitHubにコミットしない（`.gitignore`に追加済み）
2. **SECRET_KEY**: 本番環境では必ずランダムな文字列を設定
3. **環境変数**: 機密情報はすべて環境変数で管理

---

## 次のステップ

デプロイが完了したら：

1. 動作確認を行う
2. カスタムドメインを設定（オプション）
3. 定期的なバックアップを設定（オプション）

---

**デプロイで困ったら**: TROUBLESHOOTING.mdを参照してください。

