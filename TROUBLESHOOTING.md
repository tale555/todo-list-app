# トラブルシューティングガイド

## よくあるエラーと解決方法

### エラー1: `Service account info was not in the expected format, missing fields token_uri, client_email`

**原因**: 認証ファイル（JSON）のパスが間違っているか、正しいサービスアカウントのJSONファイルではない

**解決方法**:

1. **認証ファイルのパスを確認**
   ```bash
   python check_credentials.py
   ```
   このスクリプトで認証ファイルのパスと内容を確認できます。

2. **既存の認証ファイルを使用する場合**
   
   既存の認証ファイル（`../configs/silent-life-473721-e2-bd839ba557ad.json`）を使用する場合は、`.env`ファイルに以下のように設定してください：
   
   ```env
   GOOGLE_CREDENTIALS_PATH=../configs/silent-life-473721-e2-bd839ba557ad.json
   ```
   
   または、`configs/config.py`のデフォルト値を変更：
   ```python
   GOOGLE_CREDENTIALS_PATH = os.getenv(
       'GOOGLE_CREDENTIALS_PATH',
       '../configs/silent-life-473721-e2-bd839ba557ad.json'  # 既存ファイルを使用
   )
   ```

3. **新しい認証ファイルを使用する場合**
   
   - `configs/credentials.json`にサービスアカウントのJSONファイルを配置
   - `.env`ファイルでパスを指定（デフォルトは`configs/credentials.json`）

4. **認証ファイルの形式を確認**
   
   サービスアカウントのJSONファイルには以下のフィールドが必要です：
   - `type`: "service_account"
   - `project_id`
   - `private_key_id`
   - `private_key`
   - `client_email`
   - `token_uri`
   
   OAuth2.0の認証ファイル（`client_secrets.json`等）ではなく、**サービスアカウントのJSONファイル**を使用してください。

---

### エラー2: `スプレッドシートIDが設定されていません` または `HttpError 404: Requested entity was not found`

**原因**: 
- `.env`ファイルに`SPREADSHEET_ID`が設定されていない
- スプレッドシートIDに完全なURLが設定されている（IDのみが必要）

**解決方法**:

1. `.env`ファイルを開く
2. `SPREADSHEET_ID`を設定：
   ```env
   SPREADSHEET_ID=1hs3erHyqAyP1dC-CwgjL_4b-rEefVoJfoK_26e3A6EE
   ```
   **重要**: 完全なURLではなく、ID部分だけを設定してください
   
3. スプレッドシートIDの取得方法：
   - スプレッドシートのURL: `https://docs.google.com/spreadsheets/d/【ここがスプレッドシートID】/edit`
   - URLの`/d/`と`/edit`の間の文字列がスプレッドシートIDです
   - 例: URLが `https://docs.google.com/spreadsheets/d/1A2B3C4D5E6F7G8H9I0J/edit` の場合
     - スプレッドシートIDは `1A2B3C4D5E6F7G8H9I0J` です
   
4. **URLから自動抽出される機能を追加しました**
   - 完全なURLを設定しても、自動的にID部分が抽出されます
   - ただし、IDのみを設定することを推奨します

---

### エラー3: `認証ファイルが見つかりません`

**原因**: 認証ファイルのパスが間違っている

**解決方法**:

1. 認証ファイルの実際の場所を確認
2. `.env`ファイルで正しいパスを設定
3. 相対パスの場合、`todo_list_app`フォルダからの相対パスを指定

**例**:
- 認証ファイルが`configs/credentials.json`にある場合: `GOOGLE_CREDENTIALS_PATH=configs/credentials.json`
- 認証ファイルが`../configs/silent-life-473721-e2-bd839ba557ad.json`にある場合: `GOOGLE_CREDENTIALS_PATH=../configs/silent-life-473721-e2-bd839ba557ad.json`

---

### エラー4: `スプレッドシート情報の取得に失敗しました` または `HttpError 404: Requested entity was not found`

**原因**: 
- スプレッドシートIDが間違っている（完全なURLが設定されている等）
- サービスアカウントにスプレッドシートへのアクセス権限がない
- スプレッドシートが存在しない

**解決方法**:

1. **スプレッドシートIDの確認**
   - `.env`ファイルで`SPREADSHEET_ID`が正しく設定されているか確認
   - 完全なURLではなく、ID部分だけを設定してください
   - 例: `SPREADSHEET_ID=1hs3erHyqAyP1dC-CwgjL_4b-rEefVoJfoK_26e3A6EE`
   
2. **スプレッドシートの存在確認**
   - スプレッドシートが実際に存在するか確認
   - スプレッドシートを開いて、URLからIDを確認
   
3. **サービスアカウントへの権限付与**
   - スプレッドシートを開く
   - 「共有」ボタンをクリック
   - サービスアカウントのメールアドレス（認証ファイルの`client_email`）を追加
   - 権限を「編集者」に設定
   - 認証ファイル（`configs/credentials.json`）を開いて、`client_email`の値を確認

---

## デバッグ方法

### 1. 認証ファイルの確認
```bash
python check_credentials.py
```

### 2. Google Sheets API接続のテスト
```bash
python test_sheets.py
```

### 3. ブラウザでテストエンドポイントにアクセス
```
http://localhost:5000/test-sheets
```

---

## 設定の確認チェックリスト

- [ ] `.env`ファイルが存在する
- [ ] `GOOGLE_CREDENTIALS_PATH`が正しく設定されている
- [ ] 認証ファイルが指定されたパスに存在する
- [ ] 認証ファイルが正しいサービスアカウントのJSONファイルである
- [ ] `SPREADSHEET_ID`が設定されている
- [ ] サービスアカウントにスプレッドシートへのアクセス権限がある

---

## まだ解決しない場合

1. `USER_SETUP_GUIDE.md`を参照して、Google Sheets APIの設定を最初からやり直す
2. 新しいサービスアカウントを作成して、新しい認証ファイルをダウンロードする
3. エラーメッセージの全文を確認して、具体的な問題を特定する

