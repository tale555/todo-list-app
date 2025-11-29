# User ID取得方法（ngrok不要）

## 方法1: LINE Developers ConsoleのWebhookイベントから取得（最も簡単）

### ステップ1: LINE公式アカウントを友だち追加

1. LINE Developers Consoleで「Todoリスト」チャネルを開く
2. 「Messaging API」タブを開く
3. 公式アカウントのQRコードを表示
4. QRコードをスキャンして友だち追加

### ステップ2: メッセージを送信

1. LINE公式アカウントに任意のメッセージを送信（例: 「テスト」）

### ステップ3: WebhookイベントからUser IDを取得

1. LINE Developers Consoleの「Messaging API」タブを開く
2. 「Webhookイベント」セクションを開く
3. 最新のイベントをクリック
4. JSONデータから `source.userId` を探す
5. その値をコピー

例：
```json
{
  "events": [
    {
      "type": "message",
      "source": {
        "userId": "U1234567890abcdefghijklmnopqrstuvw"
      },
      ...
    }
  ]
}
```

### ステップ4: .envファイルに設定

取得したUser IDを`.env`ファイル`に設定：

```env
LINE_USER_ID=U1234567890abcdefghijklmnopqrstuvw
```

## 方法2: 既存のUser IDでテスト

現在設定されているUser ID（`Ubd12a463884a8bdb388ded25999bfa2e`）が正しいか確認：

1. LINE公式アカウントを友だち追加しているか確認
2. 友だち追加後、再度テスト：
   ```bash
   python test_line_notify.py
   ```

## 方法3: 対話型でUser IDを入力

```bash
python test_line_interactive.py
```

実行時に、取得したUser IDを直接入力できます。

