# User ID取得方法（Webhookイベントログ・ngrok不要）

## 🎯 方法：FlaskアプリのWebhookエンドポイントを使用

### ステップ1: Flaskアプリを起動

```bash
cd todo_list_app
python main.py
```

アプリが起動したら、`http://localhost:5000` でアクセスできます。

### ステップ2: ngrokでトンネルを作成（一時的）

**注意**: これはUser IDを取得するためだけに一時的に使用します。

1. 新しいターミナルを開く
2. ngrokを起動：
   ```powershell
   & "C:\Users\mhero\OneDrive\デスクトップ\cursor練習\0 ngrok\ngrok.exe" http 5000
   ```
3. 表示されたURL（例: `https://xxxx-xxxx.ngrok-free.app`）をコピー

### ステップ3: LINE Developers ConsoleでWebhook URLを設定

1. [LINE Developers Console](https://developers.line.biz/console/) にアクセス
2. 「Todoリスト」チャネルを開く
3. 「Messaging API」タブを開く
4. 「Webhook URL」に以下を設定：
   ```
   https://xxxx-xxxx.ngrok-free.app/line/webhook
   ```
   （`xxxx-xxxx.ngrok-free.app` を実際のngrok URLに置き換え）
5. 「検証」ボタンをクリック（成功すればOK）
6. 「Webhookの利用」をONにする

### ステップ4: LINE公式アカウントを友だち追加

1. LINE Developers Consoleで公式アカウントのQRコードを表示
2. QRコードをスキャンして友だち追加

### ステップ5: User IDを取得

友だち追加後、**Flaskアプリのターミナル**に以下のようなメッセージが表示されます：

```
============================================================
✅ 友だち追加イベントを受信しました！
   User ID: U1234567890abcdefghijklmnopqrstuvw
   このUser IDを.envファイルのLINE_USER_IDに設定してください
============================================================
```

または、公式アカウントにメッセージを送信すると：

```
============================================================
✅ メッセージイベントを受信しました！
   User ID: U1234567890abcdefghijklmnopqrstuvw
   このUser IDを.envファイルのLINE_USER_IDに設定してください
============================================================
```

### ステップ6: .envファイルを更新

取得したUser IDを`.env`ファイルに設定：

```env
LINE_USER_ID=U1234567890abcdefghijklmnopqrstuvw
```

### ステップ7: ngrokを停止

User IDを取得したら、ngrokは停止してOKです。

### ステップ8: テスト

```bash
python test_line_notify.py
```

成功すれば、LINEアプリにメッセージが届きます！

## 💡 重要なポイント

- **ngrokは一時的です**。User IDを取得したら停止してOKです。
- **Webhook URLの設定は必須です**。友だち追加やメッセージ送信のイベントを受信するために必要です。
- **友だち追加が必須です**。LINE Messaging APIでは、友だち追加していないユーザーにはメッセージを送信できません。

