# ngrok認証設定ガイド

## エラー内容

```
ERROR: authentication failed: Usage of ngrok requires a verified account and authtoken.
```

ngrok v3では、認証トークン（authtoken）の設定が必要です。

## 解決手順

### ステップ1: ngrokアカウントにサインアップ

1. [ngrok公式サイト](https://dashboard.ngrok.com/signup)にアクセス
2. 無料アカウントを作成（メールアドレスで登録）

### ステップ2: 認証トークンを取得

1. ログイン後、[認証トークンページ](https://dashboard.ngrok.com/get-started/your-authtoken)にアクセス
2. 表示された認証トークンをコピー

### ステップ3: 認証トークンを設定

ターミナルで以下のコマンドを実行：

```powershell
cd "C:\Users\mhero\OneDrive\デスクトップ\cursor練習\★ngrok"
.\ngrok.exe config add-authtoken YOUR_AUTHTOKEN_HERE
```

（`YOUR_AUTHTOKEN_HERE`の部分を、コピーした認証トークンに置き換えてください）

### ステップ4: 確認

認証トークンを設定したら、再度ngrokを起動：

```powershell
.\ngrok.exe http 5000
```

今度は正常に起動するはずです。

## 注意事項

- 認証トークンは一度設定すれば、次回以降は設定不要です
- 認証トークンは他人に知られないように管理してください

