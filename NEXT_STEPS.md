# 次のステップ：LINE Webhook設定とUser ID取得

## ✅ 現在の状況

- ✅ ngrokが起動中
- ✅ Public URL: `https://aeromarine-colt-catoptrical.ngrok-free.dev`

## 📋 次のステップ

### ステップ1: LINE Developers ConsoleでWebhook URLを設定

1. [LINE Developers Console](https://developers.line.biz/console/) にアクセス
2. チャネル（Todoリスト）を開く
3. 「Messaging API」タブを開く
4. 「Webhook URL」に以下を設定：
   ```
   https://aeromarine-colt-catoptrical.ngrok-free.dev/line/webhook
   ```
   **重要**: `/line/webhook` を忘れずに追加してください！
5. 「検証」ボタンをクリック
   - 成功すれば「✅ 成功」と表示されます
6. 「Webhookの利用」をONにする

### ステップ2: Flaskアプリを起動

**新しいターミナル**を開いて、以下を実行：

```bash
cd todo_list_app
python main.py
```

Flaskアプリが起動すると、以下のような表示が出ます：

```
 * Running on http://127.0.0.1:5000
```

**重要**: このターミナルは開いたままにしておいてください。

### ステップ3: LINE公式アカウントを友だち追加

1. LINE Developers Consoleの「Messaging API」タブで、公式アカウントのQRコードを表示
2. スマートフォンのLINEアプリでQRコードをスキャン
3. 友だち追加を完了

### ステップ4: User IDを取得

友だち追加後、**Flaskアプリのターミナル**（ステップ2で開いたターミナル）に以下のようなメッセージが表示されます：

```
============================================================
✅ 友だち追加イベントを受信しました！
   User ID: U1234567890abcdefghijklmnopqrstuvw
   このUser IDを.envファイルのLINE_USER_IDに設定してください
============================================================
```

**このUser ID（`U`で始まる長い文字列）をコピーしてください。**

もし表示されない場合は、公式アカウントにメッセージを送信してみてください（例: 「テスト」）。

### ステップ5: .envファイルを更新

取得したUser IDを`.env`ファイルに設定します。

**方法1: 手動で編集**

`todo_list_app/.env`ファイルを開いて、以下を追加または更新：

```env
LINE_USER_ID=取得したUser ID
```

**方法2: 対話型スクリプトを使用**

新しいターミナルで：

```bash
cd todo_list_app
python setup_line_env.py
```

実行時に、User IDを入力してください。

### ステップ6: テスト

設定が完了したら、以下でテスト：

```bash
cd todo_list_app
python test_line_notify.py
```

成功すれば、LINEアプリにメッセージが届きます！

## 🔍 トラブルシューティング

### Webhook検証が失敗する場合

1. Flaskアプリが起動しているか確認
2. ngrokが起動しているか確認（このターミナルを確認）
3. Webhook URLに `/line/webhook` が含まれているか確認

### User IDが表示されない場合

1. 友だち追加が完了しているか確認
2. 「Webhookの利用」がONになっているか確認
3. Flaskアプリのターミナルにエラーが出ていないか確認
4. 公式アカウントにメッセージを送信してみる

