# GitHubへのアップロードガイド

## 📋 手順

### ステップ1: GitHubアカウントの作成（まだの場合）

1. https://github.com/ にアクセス
2. 「Sign up」をクリック
3. アカウントを作成

### ステップ2: 新しいリポジトリを作成

1. GitHubにログイン
2. 右上の「+」→「New repository」をクリック
3. 以下の設定を行う：
   - **Repository name**: `todo-list-app`（任意の名前）
   - **Description**: `Todo List App with LINE integration`（任意）
   - **Visibility**: `Public` または `Private`（お好みで）
   - **Initialize this repository with**: チェックを外す（既存のコードをアップロードするため）
4. 「Create repository」をクリック

### ステップ3: Gitリポジトリの初期化とアップロード

PowerShellで以下を実行してください：

```powershell
# todo_list_appフォルダに移動
cd "C:\Users\mhero\OneDrive\デスクトップ\cursor練習\todo_list_app"

# Gitリポジトリを初期化
git init

# すべてのファイルをステージング
git add .

# コミット
git commit -m "Initial commit: Todo List App with LINE integration"

# メインブランチに設定
git branch -M main

# リモートリポジトリを追加（YOUR_USERNAMEとYOUR_REPO_NAMEを置き換えてください）
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# GitHubにプッシュ
git push -u origin main
```

**重要**: 
- `YOUR_USERNAME` をあなたのGitHubユーザー名に置き換えてください
- `YOUR_REPO_NAME` をステップ2で作成したリポジトリ名に置き換えてください

### ステップ4: 認証情報の確認

アップロード前に、以下のファイルが`.gitignore`に含まれていることを確認：

- ✅ `.env` - 環境変数ファイル（機密情報）
- ✅ `configs/credentials.json` - Google認証ファイル（機密情報）
- ✅ `configs/*.json` - その他の認証ファイル

これらはGitHubにアップロードされません（セキュリティのため）。

## 🔐 セキュリティ確認

アップロード前に、以下のファイルが含まれていないことを確認：

- ❌ `.env` - 含まれない（.gitignoreに追加済み）
- ❌ `configs/credentials.json` - 含まれない（.gitignoreに追加済み）
- ✅ その他のコードファイル - 含まれる

## 📝 アップロードされるファイル

以下のファイルがGitHubにアップロードされます：

- ✅ `main.py` - メインアプリケーション
- ✅ `requirements.txt` - 依存パッケージ
- ✅ `Procfile` - デプロイ用設定
- ✅ `runtime.txt` - Pythonバージョン
- ✅ `templates/` - HTMLテンプレート
- ✅ `static/` - CSS、JavaScript
- ✅ `core/` - コアロジック
- ✅ `configs/` - 設定ファイル（認証ファイル以外）
- ✅ `.gitignore` - Git除外設定
- ✅ その他のドキュメントファイル

## ⚠️ 注意事項

1. **認証ファイルはアップロードされません**
   - `.env`ファイル
   - `configs/credentials.json`
   - これらは環境変数として設定する必要があります

2. **初回プッシュ時に認証を求められる場合があります**
   - GitHubのユーザー名とパスワード（またはPersonal Access Token）を入力

3. **Personal Access Tokenが必要な場合**
   - GitHubの設定 → Developer settings → Personal access tokens → Tokens (classic)
   - 新しいトークンを生成（`repo`権限が必要）

## 🚀 アップロード後の確認

1. GitHubのリポジトリページにアクセス
2. ファイルが正しくアップロードされているか確認
3. `.env`や`credentials.json`が含まれていないことを確認

## 📋 次のステップ

アップロードが完了したら：

1. RenderまたはRailwayでデプロイ
2. 環境変数を設定
3. LINE Webhook URLを更新

詳細は `FREE_DEPLOYMENT_GUIDE.md` を参照してください。

