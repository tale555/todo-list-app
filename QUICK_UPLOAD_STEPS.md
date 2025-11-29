# GitHubへのアップロード - クイックガイド

## 🚀 手順

### ステップ1: GitHubでリポジトリを作成

1. https://github.com/new にアクセス
2. リポジトリ名を入力（例: `todo-list-app`）
3. 「Create repository」をクリック
4. **重要**: 「Initialize this repository with」のチェックは**外す**

### ステップ2: PowerShellでコマンドを実行

`todo_list_app`フォルダで、以下のコマンドを順番に実行してください：

```powershell
# 1. Gitリポジトリを初期化
git init

# 2. すべてのファイルを追加
git add .

# 3. コミット
git commit -m "Initial commit: Todo List App with LINE integration"

# 4. メインブランチに設定
git branch -M main

# 5. リモートリポジトリを追加（YOUR_USERNAMEとYOUR_REPO_NAMEを置き換え）
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 6. GitHubにプッシュ
git push -u origin main
```

**重要**: 
- `YOUR_USERNAME` をあなたのGitHubユーザー名に置き換えてください
- `YOUR_REPO_NAME` をステップ1で作成したリポジトリ名に置き換えてください

### ステップ3: 認証

初回プッシュ時に認証を求められる場合があります：

- **ユーザー名**: GitHubのユーザー名を入力
- **パスワード**: Personal Access Tokenを入力（パスワードではなく）

Personal Access Tokenの作成方法：
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. 「Generate new token」をクリック
3. `repo`権限を選択
4. トークンを生成してコピー

## ✅ 完了確認

GitHubのリポジトリページにアクセスして、ファイルがアップロードされているか確認してください。

## 📋 次のステップ

アップロードが完了したら：

1. RenderまたはRailwayでデプロイ
2. 環境変数を設定
3. LINE Webhook URLを更新

詳細は `FREE_DEPLOYMENT_GUIDE.md` を参照してください。

