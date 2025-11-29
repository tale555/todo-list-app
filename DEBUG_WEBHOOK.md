# Webhookデバッグガイド

## 🔍 確認すべきターミナル

**重要**: Flaskアプリを起動したターミナルを確認してください。

- `python main.py` を実行したターミナル
- 「🚀 Todo List App サーバーを起動...」と表示されているターミナル
- `http://localhost:5000` が表示されているターミナル

## 📋 ステップ1: Flaskアプリを再起動

デバッグログを追加したので、Flaskアプリを再起動してください：

1. Flaskアプリのターミナルで `Ctrl+C` を押して停止
2. 再度起動：
   ```bash
   python main.py
   ```

## 📋 ステップ2: メッセージを送信

LINE公式アカウントにメッセージを送信（例: 「テスト」）

## 📋 ステップ3: Flaskアプリのターミナルを確認

メッセージ送信後、以下のような表示が出るはずです：

```
============================================================
📥 Webhookイベントを受信しました
============================================================
   イベント数: 1

   イベント #1:
     タイプ: message
     User ID: U1234567890abcdefghijklmnopqrstuvw
============================================================
✅ メッセージイベントを受信しました！
   User ID: U1234567890abcdefghijklmnopqrstuvw
   このUser IDを.envファイルのLINE_USER_IDに設定してください
============================================================
```

## 🧪 手動テスト（オプション）

もし表示されない場合は、手動でテストできます：

```bash
python test_webhook_manual.py
```

このスクリプトは、Flaskアプリに直接テストリクエストを送信します。

## ⚠️ それでも表示されない場合

1. **Flaskアプリが起動しているか確認**
   - `http://localhost:5000` にアクセスできるか確認

2. **ngrokが起動しているか確認**
   - ngrokのターミナルで `Session Status: online` が表示されているか確認

3. **Webhook URLが正しいか確認**
   - LINE Developers Consoleで、Webhook URLが `https://aeromarine-colt-catoptrical.ngrok-free.dev/line/webhook` になっているか確認

4. **「Webhookの利用」がONになっているか確認**
   - LINE Developers Consoleで、「Webhookの利用」がONになっているか確認

5. **ターミナルをスクロール**
   - ターミナルを上にスクロールして、過去のメッセージを確認してください

