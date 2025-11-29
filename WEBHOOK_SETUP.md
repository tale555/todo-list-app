# LINE Webhook設定ガイド

## 問題

「Failed to send messages」エラーが発生する場合、Webhook URLが正しく設定されていない可能性があります。

## ローカル開発環境での設定方法

### 方法1: ngrokを使用（推奨）

1. **ngrokをインストール**
   - [ngrok公式サイト](https://ngrok.com/)からダウンロード
   - または `choco install ngrok` (Windows) / `brew install ngrok` (Mac)

2. **ngrokでトンネルを作成**
   ```bash
   ngrok http 5000
   ```
   これで、以下のようなURLが表示されます：
   ```
   Forwarding  https://xxxx-xxxx-xxxx.ngrok.io -> http://localhost:5000
   ```

3. **LINE Developers ConsoleでWebhook URLを設定**
   - Webhook URL: `https://xxxx-xxxx-xxxx.ngrok.io/line/webhook`
   - 「Webhookの利用」を有効にする
   - 「検証」ボタンをクリックして接続を確認

4. **アプリを起動**
   ```bash
   python main.py
   ```

### 方法2: クラウドサービスを使用

- Heroku、Railway、Renderなどのサービスにデプロイ
- デプロイ後のURLをWebhook URLに設定

## 重要な注意点

⚠️ **Webhook URLは、メッセージ受信のためだけに使用されます**

メッセージ送信（Push Message）には、Webhook URLは**不要**です。

「Failed to send messages」エラーの主な原因：
1. **LINE公式アカウントが友だち追加されていない**（最も可能性が高い）
2. User IDが正しくない
3. Channel Access Tokenが無効

## 確認手順

1. LINE公式アカウントを友だち追加しているか確認
2. 友だち追加後、公式アカウントにメッセージを送信
3. Webhookイベントが受信されるか確認（サーバーログで確認）
4. 正しいUser IDを取得して`.env`ファイルに設定

## テスト方法

Webhook URLを設定した後：

1. LINE公式アカウントを友だち追加
2. 公式アカウントに「テスト」とメッセージを送信
3. サーバーログでWebhookイベントを確認
4. User IDが正しく取得できているか確認

