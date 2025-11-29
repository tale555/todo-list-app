# LINE User ID取得ガイド

## 問題

友だち追加前に取得したUser IDは、友だち追加後でも使用できない場合があります。
LINE Messaging APIでは、**友だち追加後に再度User IDを取得**する必要があります。

## 解決方法

### 方法1: Webhookを使用（推奨）

1. **ngrokをインストール**（まだの場合）
   - [ngrok公式サイト](https://ngrok.com/)からダウンロード
   - または `choco install ngrok` (Windows)

2. **ngrokでトンネルを作成**
   ```bash
   ngrok http 5001
   ```
   表示されたURL（例: `https://xxxx-xxxx.ngrok-free.app`）をコピー

3. **User ID取得サーバーを起動**
   ```bash
   python get_user_id_simple.py
   ```

4. **LINE Developers ConsoleでWebhook URLを設定**
   - Webhook URL: `https://xxxx-xxxx.ngrok-free.app/line/webhook`
   - 「Webhookの利用」をONにする
   - 「検証」ボタンで接続確認

5. **LINE公式アカウントを友だち追加**
   - LINE Developers Consoleで公式アカウントのQRコードを確認
   - QRコードをスキャンして友だち追加

6. **User IDを取得**
   - 友だち追加後、自動的にUser IDがコンソールに表示されます
   - または、公式アカウントにメッセージを送信

7. **.envファイルを更新**
   ```env
   LINE_USER_ID=取得したUser ID
   ```

### 方法2: ngrokなしで確認（簡易版）

1. **LINE公式アカウントを友だち追加**
2. **公式アカウントにメッセージを送信**
3. **LINE Developers ConsoleでWebhookイベントを確認**
   - 「Messaging API」タブ → 「Webhookイベント」セクション
   - 最新のイベントからUser IDを確認
   - `source.userId` の値をコピー

4. **.envファイルを更新**
   ```env
   LINE_USER_ID=取得したUser ID
   ```

## 確認

User IDを更新したら、以下でテスト：

```bash
python test_line_notify.py
```

成功すれば、LINEアプリにメッセージが届きます！

