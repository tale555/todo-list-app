# ngrokセットアップガイド

## 手順

### 1. ngrokを起動

ターミナルで以下のコマンドを実行：

```bash
ngrok http 5000
```

**重要**: アプリ（`python main.py`）が起動している状態で実行してください。

### 2. ngrokの出力を確認

ngrokを起動すると、以下のような出力が表示されます：

```
Forwarding  https://xxxx-xxxx-xxxx.ngrok-free.app -> http://localhost:5000
```

この `https://xxxx-xxxx-xxxx.ngrok-free.app` のURLをコピーしてください。

### 3. LINE Developers ConsoleでWebhook URLを設定

1. [LINE Developers Console](https://developers.line.biz/console/) にアクセス
2. 「Todoリスト」チャネルを開く
3. 「Messaging API」タブを開く
4. Webhook URLに以下を設定：
   ```
   https://xxxx-xxxx-xxxx.ngrok-free.app/line/webhook
   ```
   （ngrokのURL + `/line/webhook`）
5. 「編集」→ URLを入力 → 「更新」
6. 「検証」ボタンをクリック

### 4. 確認

アプリのコンソールに「✅ Webhook検証リクエストを受信しました」と表示されれば成功です。

## 注意事項

- ngrokのURLは起動するたびに変わります（無料版の場合）
- ngrokを再起動したら、LINE Developers ConsoleでWebhook URLも更新が必要です
- ngrokとアプリの両方が起動している必要があります

