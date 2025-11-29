# GitHubリポジトリにアップロード

## 📋 あなたのリポジトリ情報

- **リポジトリURL**: `https://github.com/tale555/todo-list-app.git`
- **ユーザー名**: `tale555`

## 🚀 アップロード手順

### ステップ1: PowerShellでコマンドを実行

`todo_list_app`フォルダで、以下のコマンドを順番に実行してください：

```powershell
# 1. Gitリポジトリを初期化（まだの場合）
git init

# 2. すべてのファイルを追加
git add .

# 3. コミット
git commit -m "Initial commit: Todo List App with LINE integration"

# 4. メインブランチに設定
git branch -M main

# 5. リモートリポジトリを追加
git remote add origin https://github.com/tale555/todo-list-app.git

# 6. GitHubにプッシュ
git push -u origin main
```

### ステップ2: 認証

初回プッシュ時に認証を求められる場合があります：

- **ユーザー名**: `tale555`
- **パスワード**: Personal Access Token（パスワードではありません）

#### Personal Access Tokenの作成方法

1. GitHubにログイン
2. 右上のアイコンをクリック → **Settings**
3. 左メニューから **Developer settings**
4. **Personal access tokens** → **Tokens (classic)**
5. **Generate new token** → **Generate new token (classic)** をクリック
6. 以下の設定を行う：
   - **Note**: `todo-list-app-deploy`（任意の名前）
   - **Expiration**: お好みで（90日、1年など）
   - **Select scopes**: `repo`にチェック
7. **Generate token** をクリック
8. 表示されたトークンをコピー（**この画面を閉じると二度と表示されません**）

### ステップ3: プッシュ時の認証

`git push -u origin main` を実行すると、認証を求められます：

```
Username for 'https://github.com': tale555
Password for 'https://tale555@github.com': [ここにPersonal Access Tokenを貼り付け]
```

**重要**: パスワードの代わりに、Personal Access Tokenを入力してください。

## ⚠️ エラーが出た場合

### エラー: "remote origin already exists"

既にリモートリポジトリが設定されている場合：

```powershell
# 既存のリモートを削除
git remote remove origin

# 再度追加
git remote add origin https://github.com/tale555/todo-list-app.git
```

### エラー: "failed to push some refs"

リポジトリに既にファイルがある場合：

```powershell
# リモートの変更を取得
git pull origin main --allow-unrelated-histories

# 再度プッシュ
git push -u origin main
```

## ✅ 完了確認

GitHubのリポジトリページ（https://github.com/tale555/todo-list-app）にアクセスして、ファイルがアップロードされているか確認してください。

