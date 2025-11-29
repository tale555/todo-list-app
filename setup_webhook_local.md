# ローカル開発環境でのWebhook設定

## ステップ1: ngrokをインストール

1. [ngrok公式サイト](https://ngrok.com/)にアクセス
2. アカウントを作成（無料）
3. ngrokをダウンロードしてインストール
4. 認証トークンを設定（ダウンロードページに表示されています）

## ステップ2: ngrokでトンネルを作成

1. ターミナルで以下のコマンドを実行：
   ```bash
   ngrok http 5000
   ```

2. 以下のような出力が表示されます：
   ```
   Forwarding  https://xxxx-xxxx-xxxx.ngrok-free.app -> http://localhost:5000
   ```

3. **この `https://xxxx-xxxx-xxxx.ngrok-free.app` のURLをコピー**

## ステップ3: LINE Developers ConsoleでWebhook URLを設定

1. [LINE Developers Console](https://developers.line.biz/console/)にアクセス
2. 作成したチャネルの「Messaging API」タブを開く
3. 「Webhook URL」セクションで：
   - 「編集」ボタンをクリック
   - Webhook URLに以下を入力：
     ```
     https://xxxx-xxxx-xxxx.ngrok-free.app/line/webhook
     ```
     （ngrokで取得したURL + `/line/webhook`）
   - 「更新」をクリック
4. 「Webhookの利用」のトグルを**ON**にする
5. 「検証」ボタンをクリックして接続を確認

## ステップ4: アプリを起動

別のターミナルで：
```bash
cd todo_list_app
python main.py
```

## ステップ5: テスト

1. LINE公式アカウントを友だち追加
2. 公式アカウントに「テスト」とメッセージを送信
3. アプリのコンソールでUser IDが表示されることを確認
4. 取得したUser IDを`.env`ファイルに設定

## 注意事項

- ngrokの無料版では、URLが毎回変わる可能性があります
- ngrokを再起動するとURLが変わるので、その都度LINE Developers Consoleで更新が必要です
- ngrokのセッションが切れると、Webhookが動作しなくなります

