# User IDを.envファイルに設定する方法

## ✅ User IDを取得できました！

Flaskアプリのターミナルに表示されたUser IDをコピーしてください。

例：
```
User ID: U1234567890abcdefghijklmnopqrstuvw
```

## 📋 設定方法

### 方法1: 対話型スクリプトを使用（推奨）

```bash
cd todo_list_app
python setup_line_env.py
```

実行時に、User IDを入力してください。

### 方法2: 手動で編集

1. `todo_list_app/.env`ファイルを開く
2. 以下を追加または更新：

```env
LINE_USER_ID=コピーしたUser ID
```

例：
```env
LINE_CHANNEL_ACCESS_TOKEN=T6mzD99pdh8z4n7DIOgv...
LINE_USER_ID=U1234567890abcdefghijklmnopqrstuvw
```

## 🧪 テスト

設定が完了したら、以下でテスト：

```bash
cd todo_list_app
python test_line_notify.py
```

成功すれば、LINEアプリにメッセージが届きます！

## ✅ 完了

これでLINE API連携の設定が完了しました！

- ✅ Channel Access Token: 設定済み
- ✅ User ID: 設定済み
- ✅ Webhook: 動作確認済み

今後、Todoの期日リマインダーがLINEで通知されます！

