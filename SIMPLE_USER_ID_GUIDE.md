# 簡単なUser ID取得方法（ngrok不要）

## 🎯 最も簡単な方法

### ステップ1: LINE公式アカウントを友だち追加

1. [LINE Developers Console](https://developers.line.biz/console/) にアクセス
2. 「Todoリスト」チャネルを開く
3. 「Messaging API」タブを開く
4. 公式アカウントのQRコードを表示
5. QRコードをスキャンして友だち追加

### ステップ2: メッセージを送信

LINE公式アカウントに任意のメッセージを送信（例: 「テスト」）

### ステップ3: User IDを取得

1. LINE Developers Consoleの「Messaging API」タブを開く
2. 下にスクロールして「Webhookイベント」セクションを開く
3. 最新のイベント（メッセージを送信したイベント）をクリック
4. 表示されるJSONデータから `source.userId` を探す

例：
```json
{
  "events": [
    {
      "type": "message",
      "source": {
        "userId": "U1234567890abcdefghijklmnopqrstuvw"
      }
    }
  ]
}
```

5. `userId` の値（`U`で始まる長い文字列）をコピー

### ステップ4: .envファイルに設定

`todo_list_app`フォルダの`.env`ファイルを開き、以下を設定：

```env
LINE_USER_ID=コピーしたUser ID
```

例：
```env
LINE_USER_ID=U1234567890abcdefghijklmnopqrstuvw
```

### ステップ5: テスト

```bash
python test_line_notify.py
```

## 💡 ヒント

- Webhook URLの設定は不要です（メッセージ送信には不要）
- LINE Developers ConsoleのWebhookイベントログから直接User IDを取得できます
- 友だち追加後、メッセージを送信すればイベントが記録されます

