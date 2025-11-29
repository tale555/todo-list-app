# LINE連携セットアップガイド（LINE Messaging API）

このガイドでは、Todo ListアプリにLINE Messaging APIを使用した通知機能を設定する方法を説明します。

⚠️ **重要**: LINE Notifyは2025年3月31日にサービス終了予定のため、LINE Messaging APIを使用します。

## 📋 目次

1. [LINE Messaging APIの設定](#line-messaging-apiの設定)
2. [環境変数の設定](#環境変数の設定)
3. [通知機能のテスト](#通知機能のテスト)
4. [自動実行の設定](#自動実行の設定)
5. [トラブルシューティング](#トラブルシューティング)

## 🔑 LINE Messaging APIの設定

### ステップ1: LINE Developers Consoleでチャネルを作成

1. [LINE Developers Console](https://developers.line.biz/console/) にアクセス
2. LINEアカウントでログイン
3. 「新規チャネル作成」をクリック
4. 「Messaging API」を選択
5. チャネル情報を入力：
   - **チャネル名**: 任意の名前（例: "Todo List通知"）
   - **チャネル説明**: 任意の説明
   - **大業種**: 適切な業種を選択
   - **小業種**: 適切な業種を選択
6. 利用規約に同意して「作成」をクリック

### ステップ2: Channel Access Tokenを取得

1. 作成したチャネルのページで「Messaging API」タブを開く
2. 「Channel access token」セクションで「Issue」をクリック
3. **表示されたトークンをコピー**します（このトークンは後で確認できないため、必ずコピーしてください）

### ステップ3: User IDを取得

LINE Messaging APIでは、メッセージを送信するユーザーのUser IDが必要です。

#### 方法1: Webhookを使用して取得（推奨）

1. LINE Developers Consoleで「Messaging API」タブを開く
2. 「Webhook URL」にアプリのWebhook URLを設定（本番環境の場合）
3. 「Webhookの利用」を有効にする
4. LINE公式アカウントを友だち追加
5. 公式アカウントにメッセージを送信
6. WebhookイベントからUser IDを取得

#### 方法2: 一時的な取得方法（開発・テスト用）

1. LINE公式アカウントを友だち追加
2. 公式アカウントに任意のメッセージを送信
3. WebhookイベントのログからUser IDを確認
   - または、Webhook受信用のエンドポイントを作成してUser IDを取得

⚠️ **重要**: 
- Channel Access TokenとUser IDは他人に知られないように管理してください
- Channel Access Tokenは定期的に再発行することを推奨します

## ⚙️ 環境変数の設定

### ステップ1: .envファイルの作成

プロジェクトのルートディレクトリ（`todo_list_app/`）に`.env`ファイルを作成します。

### ステップ2: LINE Messaging APIの設定

`.env`ファイルを開き、取得した情報を設定します：

```env
LINE_CHANNEL_ACCESS_TOKEN=your_channel_access_token_here
LINE_USER_ID=your_user_id_here
```

例：
```env
LINE_CHANNEL_ACCESS_TOKEN=abcdefghijklmnopqrstuvwxyz1234567890
LINE_USER_ID=U1234567890abcdefghijklmnopqrstuvwxyz
```

## 🧪 通知機能のテスト

### 方法1: コマンドラインからテスト

1. アプリケーションのディレクトリに移動：
   ```bash
   cd todo_list_app
   ```

2. テストスクリプトを実行：
   ```bash
   python test_line_notify.py
   ```

3. または、対話型テストスクリプトを実行：
   ```bash
   python test_line_interactive.py
   ```

### 方法2: ブラウザから手動送信

1. アプリケーションを起動します：
   ```bash
   python main.py
   ```

2. ブラウザで `http://localhost:5000` にアクセス

3. 画面上部の「📱 LINE通知送信」ボタンをクリック

4. 通知対象のTodoがある場合、LINEに通知が送信されます

## ⏰ 自動実行の設定

LINE通知は、以下のタイミングで自動的に送信されます：

- **3日前**: 期日が3日後のTodo
- **前日**: 期日が明日のTodo
- **当日**: 期日が今日のTodo

### Windowsの場合（タスクスケジューラー）

1. 「タスクスケジューラー」を開く
2. 「基本タスクの作成」を選択
3. 以下の設定を行います：
   - **名前**: Todo List LINE通知
   - **トリガー**: 毎日、希望する時刻（例: 朝9時）
   - **操作**: プログラムの開始
   - **プログラム/スクリプト**: `python`
   - **引数の追加**: `-c "from core.line_notifier import LineNotifier; LineNotifier().check_and_send_reminders()"`
   - **開始**: プロジェクトのディレクトリパス

### Mac/Linuxの場合（cron）

`crontab`を編集して、毎日実行するように設定します：

```bash
crontab -e
```

以下の行を追加（毎日朝9時に実行する例）：

```cron
0 9 * * * cd /path/to/todo_list_app && python -c "from core.line_notifier import LineNotifier; LineNotifier().check_and_send_reminders()"
```

### Pythonスクリプトとして実行

より簡単な方法として、専用のスクリプトを作成することもできます：

```python
# send_notifications.py
from core.line_notifier import LineNotifier

if __name__ == "__main__":
    notifier = LineNotifier()
    count = notifier.check_and_send_reminders()
    print(f"{count}件の通知を送信しました")
```

このスクリプトをスケジューラーで実行するように設定します。

## 🔍 トラブルシューティング

### 通知が送信されない

1. **Channel Access Tokenの確認**
   - `.env`ファイルに正しくトークンが設定されているか確認
   - トークンに余分なスペースや改行が含まれていないか確認
   - トークンが有効期限内か確認（再発行が必要な場合があります）

2. **User IDの確認**
   - `.env`ファイルに正しくUser IDが設定されているか確認
   - LINE公式アカウントが友だち追加されているか確認

3. **環境変数の読み込み確認**
   ```python
   from configs.config import LINE_CHANNEL_ACCESS_TOKEN, LINE_USER_ID
   print(f"Token: {LINE_CHANNEL_ACCESS_TOKEN[:10]}...")  # 最初の10文字だけ表示
   print(f"User ID: {LINE_USER_ID[:10]}...")
   ```

4. **手動テスト**
   - ブラウザの「LINE通知送信」ボタンでエラーメッセージを確認
   - ブラウザの開発者ツール（F12）のコンソールでエラーを確認

### エラーメッセージ: "LINE Channel Access Tokenが設定されていません"

- `.env`ファイルが正しい場所（`todo_list_app/`ディレクトリ）にあるか確認
- `.env`ファイルに`LINE_CHANNEL_ACCESS_TOKEN`が正しく設定されているか確認
- アプリケーションを再起動して、環境変数を再読み込み

### エラーメッセージ: "LINE User IDが設定されていません"

- `.env`ファイルに`LINE_USER_ID`が正しく設定されているか確認
- User IDが正しく取得されているか確認

### エラー: 401 Unauthorized

- Channel Access Tokenが正しいか確認
- トークンが有効期限内か確認（再発行が必要な場合があります）

### エラー: 400 Bad Request

- User IDが正しいか確認
- LINE公式アカウントが友だち追加されているか確認

### 通知の内容が正しくない

- Todoの期日が正しい形式（YYYY-MM-DD）で保存されているか確認
- 完了済みのTodoは通知対象外です（正常な動作）
- LINE通知が無効になっているTodoは通知対象外です

## 📚 参考リンク

- [LINE Developers Console](https://developers.line.biz/console/)
- [LINE Messaging API ドキュメント](https://developers.line.biz/ja/docs/messaging-api/)
- [LINE Messaging API 料金](https://developers.line.biz/ja/docs/messaging-api/pricing/)

## 💡 ヒント

- 通知をテストする際は、期日を今日・明日・3日後に設定したTodoを作成してテストできます
- 通知メッセージの内容は`core/line_notifier.py`の`_create_message`メソッドでカスタマイズできます
- LINE Messaging APIには無料枠があります（月間500件など）。詳細は公式ドキュメントを確認してください
