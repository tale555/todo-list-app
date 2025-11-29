# User ID取得 ステップバイステップガイド

## ✅ 現在の設定状況

- ✅ LINE_CHANNEL_ACCESS_TOKEN: 設定済み
- ❌ LINE_USER_ID: 未設定

## 📋 User IDを取得する手順

### ステップ1: Flaskアプリを起動

新しいターミナルを開いて、以下を実行：

```bash
cd todo_list_app
python main.py
```

アプリが起動したら、`http://localhost:5000` でアクセスできます。

**重要**: このターミナルは開いたままにしておいてください。

### ステップ2: ngrokでトンネルを作成

別の新しいターミナルを開いて、以下を実行：

```powershell
& "C:\Users\mhero\OneDrive\デスクトップ\cursor練習\★ngrok\ngrok.exe" http 5000
```

または、バッチファイルを使用：

```batch
cd todo_list_app
start_ngrok.bat
```

ngrokが起動すると、以下のような表示が出ます：

```
Forwarding  https://xxxx-xxxx.ngrok-free.app -> http://localhost:5000
```

**`https://xxxx-xxxx.ngrok-free.app` の部分をコピーしてください。**

**重要**: このターミナルも開いたままにしておいてください。

### ステップ3: LINE Developers ConsoleでWebhook URLを設定

1. [LINE Developers Console](https://developers.line.biz/console/) にアクセス
2. 新しいチャネル（または既存のチャネル）を開く
3. 「Messaging API」タブを開く
4. 「Webhook URL」に以下を設定：
   ```
   https://xxxx-xxxx.ngrok-free.app/line/webhook
   ```
   （`xxxx-xxxx.ngrok-free.app` をステップ2でコピーしたURLに置き換え）
5. 「検証」ボタンをクリック
   - 成功すれば「✅ 成功」と表示されます
   - 失敗した場合は、Flaskアプリとngrokが起動しているか確認してください
6. 「Webhookの利用」をONにする

### ステップ4: LINE公式アカウントを友だち追加

1. LINE Developers Consoleの「Messaging API」タブで、公式アカウントのQRコードを表示
2. スマートフォンのLINEアプリでQRコードをスキャン
3. 友だち追加を完了

### ステップ5: User IDを取得

友だち追加後、**Flaskアプリのターミナル**（ステップ1で開いたターミナル）に以下のようなメッセージが表示されます：

```
============================================================
✅ 友だち追加イベントを受信しました！
   User ID: U1234567890abcdefghijklmnopqrstuvw
   このUser IDを.envファイルのLINE_USER_IDに設定してください
============================================================
```

**このUser ID（`U`で始まる長い文字列）をコピーしてください。**

もし表示されない場合は、公式アカウントにメッセージを送信してみてください（例: 「テスト」）。すると、以下のようなメッセージが表示されます：

```
============================================================
✅ メッセージイベントを受信しました！
   User ID: U1234567890abcdefghijklmnopqrstuvw
   このUser IDを.envファイルのLINE_USER_IDに設定してください
============================================================
```

### ステップ6: .envファイルを更新

取得したUser IDを`.env`ファイルに設定します。

**方法1: 手動で編集**

`todo_list_app/.env`ファイルを開いて、以下を追加または更新：

```env
LINE_USER_ID=取得したUser ID
```

例：
```env
LINE_USER_ID=U1234567890abcdefghijklmnopqrstuvw
```

**方法2: 対話型スクリプトを使用**

```bash
cd todo_list_app
python setup_line_env.py
```

実行時に、User IDを入力してください。

### ステップ7: テスト

設定が完了したら、以下でテスト：

```bash
cd todo_list_app
python test_line_notify.py
```

成功すれば、LINEアプリにメッセージが届きます！

### ステップ8: ngrokを停止（オプション）

User IDを取得したら、ngrokは停止してOKです。ただし、今後Webhookイベントを受信する必要がある場合は、ngrokを起動したままにしておいてください。

## 🔍 トラブルシューティング

### Webhook検証が失敗する場合

1. Flaskアプリが起動しているか確認
2. ngrokが起動しているか確認
3. ngrokのURLが正しいか確認（`.app` または `.io` で終わる）
4. Webhook URLに `/line/webhook` が含まれているか確認

### User IDが表示されない場合

1. 友だち追加が完了しているか確認
2. 「Webhookの利用」がONになっているか確認
3. Flaskアプリのターミナルにエラーが出ていないか確認
4. 公式アカウントにメッセージを送信してみる

### テストでエラーが出る場合

1. `.env`ファイルに`LINE_USER_ID`が正しく設定されているか確認
2. User IDが`U`で始まっているか確認
3. 友だち追加が完了しているか確認

