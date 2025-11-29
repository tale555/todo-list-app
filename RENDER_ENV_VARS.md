# Render環境変数の設定方法

## ✅ 環境変数名は正しいです

環境変数の**名前（キー）**は正しく設定されています。次に、**値（Value）**を実際の値に置き換える必要があります。

## 📋 各環境変数の正しい値

### 1. GOOGLE_CREDENTIALS_JSON

**現在**: `value`  
**正しい値**: `credentials.json`ファイルの内容をそのまま貼り付け

**設定方法**:
1. ローカルの `configs/credentials.json` ファイルを開く
2. ファイルの内容を**すべてコピー**（改行も含めて）
3. Renderの環境変数の値フィールドに**そのまま貼り付け**

**例**:
```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  ...
}
```

### 2. SPREADSHEET_ID

**現在**: `value`  
**正しい値**: GoogleスプレッドシートのID

**取得方法**:
- スプレッドシートのURL: `https://docs.google.com/spreadsheets/d/【ここがID】/edit`
- 例: URLが `https://docs.google.com/spreadsheets/d/1hs3erHyqAyP1dC-Cwgj.../edit` の場合
- 値: `1hs3erHyqAyP1dC-Cwgj...`

### 3. SHEET_NAME

**現在**: `........`（マスクされている）  
**正しい値**: スプレッドシートのシート名

**例**: `Todo` または `Sheet1`

### 4. SECRET_KEY

**現在**: `value`  
**正しい値**: ランダムな文字列（32文字以上推奨）

**生成方法（PowerShell）**:
```powershell
-join ((48..57) + (65..90) + (97..122) | Get-Random -Count 32 | ForEach-Object {[char]$_})
```

**例**: `aB3dE5fG7hI9jK1lM3nO5pQ7rS9tU1vW3xY5zA7bC9dE1fG3hI5jK7lM9nO1pQ3`

### 5. FLASK_DEBUG

**現在**: `........`（マスクされている）  
**正しい値**: `False`（本番環境では必ずFalse）

### 6. LINE_CHANNEL_ACCESS_TOKEN

**現在**: `........`（マスクされている）  
**正しい値**: LINE Developers Consoleで取得したChannel Access Token

**取得方法**:
- LINE Developers Console → チャネル → Messaging API → チャネルアクセストークン

### 7. LINE_USER_ID

**現在**: `........`（マスクされている）  
**正しい値**: LINE公式アカウントを友だち追加した際に取得したUser ID

**取得方法**:
- `U`で始まる長い文字列（例: `U1234567890abcdefghijklmnopqrstuvw`）

## 🔧 設定手順

1. 各環境変数の値フィールドをクリック
2. 「value」を削除
3. 実際の値を入力または貼り付け
4. 「Save Changes」をクリック

## ⚠️ 重要な注意事項

1. **GOOGLE_CREDENTIALS_JSON**: JSONの内容をそのまま貼り付ける（改行も含めて）
2. **SECRET_KEY**: 必ずランダムな文字列を生成する（推測されないように）
3. **FLASK_DEBUG**: 本番環境では必ず`False`にする
4. **機密情報**: すべての値はマスク表示されますが、正しく入力されているか確認してください

## ✅ 設定後の確認

すべての環境変数を設定したら：

1. 「Save Changes」をクリック
2. デプロイが自動的に再実行されます
3. ログを確認して、エラーがないか確認

## 📝 チェックリスト

- [ ] GOOGLE_CREDENTIALS_JSON: credentials.jsonの内容を貼り付け
- [ ] SPREADSHEET_ID: スプレッドシートIDを入力
- [ ] SHEET_NAME: シート名を入力（例: `Todo`）
- [ ] SECRET_KEY: ランダムな文字列を生成して入力
- [ ] FLASK_DEBUG: `False`を入力
- [ ] LINE_CHANNEL_ACCESS_TOKEN: Channel Access Tokenを入力
- [ ] LINE_USER_ID: User IDを入力

