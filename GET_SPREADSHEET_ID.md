# スプレッドシートIDの取得方法

## 📋 スプレッドシートIDはどこから見れる？

### 方法1: GoogleスプレッドシートのURLから取得（最も簡単）

1. **Googleスプレッドシートを開く**
   - ブラウザでスプレッドシートを開く

2. **URLを確認**
   - ブラウザのアドレスバーに表示されているURLを確認
   - URLの形式: `https://docs.google.com/spreadsheets/d/【ここがスプレッドシートID】/edit`

3. **IDをコピー**
   - `/d/` と `/edit` の間の文字列がスプレッドシートIDです

**例**:
```
URL: https://docs.google.com/spreadsheets/d/1hs3erHyqAyP1dC-CwgjL_4b-rEefVoJfoK_26e3A6EE/edit

スプレッドシートID: 1hs3erHyqAyP1dC-CwgjL_4b-rEefVoJfoK_26e3A6EE
```

### 方法2: ローカルの.envファイルから確認

もし既に`.env`ファイルに設定されている場合：

1. `todo_list_app/.env`ファイルを開く
2. `SPREADSHEET_ID=` の行を確認

### 方法3: 確認スクリプトを実行

```bash
cd todo_list_app
python check_spreadsheet_id.py
```

このスクリプトを実行すると、現在設定されているスプレッドシートIDが表示されます。

## 🔑 シークレットキーについて

### 既に作成されたシークレットキーを使う場合

**はい、そのまま入力でOKです！**

ただし、以下の点を確認してください：

1. **ローカルの.envファイルに設定されているSECRET_KEYを確認**
   - `todo_list_app/.env`ファイルを開く
   - `SECRET_KEY=` の行を確認

2. **本番環境用に新しいキーを生成することを推奨**
   - 開発環境と本番環境で同じキーを使うのはセキュリティ上推奨されません
   - 新しいキーを生成することをお勧めします

### 新しいシークレットキーを生成する場合

PowerShellで以下を実行：

```powershell
-join ((48..57) + (65..90) + (97..122) | Get-Random -Count 32 | ForEach-Object {[char]$_})
```

生成された文字列をコピーして、Renderの環境変数に設定してください。

## 📝 Renderでの設定

### SPREADSHEET_ID

1. GoogleスプレッドシートのURLからIDを取得
2. Renderの環境変数 `SPREADSHEET_ID` に設定
3. **重要**: URL全体ではなく、ID部分だけを設定してください

### SECRET_KEY

1. 既存のキーを使うか、新しいキーを生成
2. Renderの環境変数 `SECRET_KEY` に設定
3. **重要**: 本番環境では必ずランダムな文字列を使用してください

## ✅ 確認方法

設定後、以下のコマンドで確認できます：

```bash
cd todo_list_app
python check_spreadsheet_id.py
```

