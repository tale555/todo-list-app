# LINE API連携 最初から設定ガイド

## ✅ 現在の設定状況

- ✅ LINE_CHANNEL_ACCESS_TOKEN: 設定済み
- ❌ LINE_USER_ID: 未設定

## 📋 次のステップ：User IDを取得

### 方法1: Webhookを使用してUser IDを取得（推奨）

#### ステップ1: Flaskアプリを起動

```bash
cd todo_list_app
python main.py
```

アプリが起動したら、`http://localhost:5000` でアクセスできます。

#### ステップ2: ngrokでトンネルを作成

1. 新しいターミナルを開く
2. ngrokを起動：
   ```powershell
   & "C:\Users\mhero\OneDrive\デスクトップ\cursor練習\0 ngrok\ngrok.exe" http 5000
   ```
3. 表示されたURL（例: `https://xxxx-xxxx.ngrok-free.app`）をコピー

#### ステップ3: LINE Developers ConsoleでWebhook URLを設定

1. [LINE Developers Console](https://developers.line.biz/console/) にアクセス
2. 新しいチャネル（または既存のチャネル）を開く
3. 「Messaging API」タブを開く
4. 「Webhook URL」に以下を設定：
   ```
   https://xxxx-xxxx.ngrok-free.app/line/webhook
   ```
   （`xxxx-xxxx.ngrok-free.app` を実際のngrok URLに置き換え）
5. 「検証」ボタンをクリック（成功すればOK）
6. 「Webhookの利用」をONにする

#### ステップ4: LINE公式アカウントを友だち追加

1. LINE Developers Consoleで公式アカウントのQRコードを表示
2. QRコードをスキャンして友だち追加

#### ステップ5: User IDを取得

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

#### ステップ6: .envファイルを更新

`todo_list_app`フォルダに`.env`ファイルを作成（または既存のファイルを編集）し、以下を追加：

```env
LINE_CHANNEL_ACCESS_TOKEN=T6mzD99pdh8z4n7DIOgv...
LINE_USER_ID=取得したUser ID
```

例：
```env
LINE_CHANNEL_ACCESS_TOKEN=T6mzD99pdh8z4n7DIOgv...
LINE_USER_ID=U1234567890abcdefghijklmnopqrstuvw
```

#### ステップ7: テスト

```bash
python test_line_notify.py
```

成功すれば、LINEアプリにメッセージが届きます！

### 方法2: 対話型でUser IDを入力

もしWebhookを使わない場合：

```bash
python test_line_interactive.py
```

実行時に、Channel Access TokenとUser IDを直接入力できます。

## 🔍 設定確認

設定が完了したら、以下で確認：

```bash
python check_line_config.py
```

## 💡 重要なポイント

- **Channel Access Token**: LINE Developers Consoleの「Messaging API」タブ → 「チャネルアクセストークン」で取得
- **User ID**: 友だち追加後にWebhookイベントから取得（`U`で始まる長い文字列）
- **友だち追加が必須**: LINE Messaging APIでは、友だち追加していないユーザーにはメッセージを送信できません

