# 簡単なテスト方法（Webhookイベントログ不要）

## 🎯 最も簡単な方法：既存のUser IDでテスト

### ステップ1: LINE公式アカウントを友だち追加

1. [LINE Developers Console](https://developers.line.biz/console/) にアクセス
2. 「Todoリスト」チャネルを開く
3. 「Messaging API」タブを開く
4. 公式アカウントのQRコードを表示
5. QRコードをスキャンして友だち追加

### ステップ2: テスト実行

友だち追加後、以下でテスト：

```bash
cd todo_list_app
python test_line_notify.py
```

**成功すれば、LINEアプリにメッセージが届きます！**

## 💡 もしエラーが出た場合

### エラー1: "The property, 'to', in the request body is invalid"

→ User IDが正しくない可能性があります。友だち追加後に再度User IDを取得する必要があります。

### エラー2: メッセージが届かない

→ 友だち追加が完了しているか確認してください。LINE Messaging APIでは、友だち追加していないユーザーにはメッセージを送信できません。

## 🔄 別の方法：対話型でUser IDを入力

もし既存のUser IDでうまくいかない場合：

```bash
cd todo_list_app
python test_line_interactive.py
```

実行時に、新しいUser IDを直接入力できます。

## 📝 重要なポイント

- **友だち追加が必須です**。LINE Messaging APIでは、友だち追加していないユーザーにはメッセージを送信できません。
- Webhookイベントログは不要です。友だち追加してテストすれば、動作確認できます。
- 現在のUser IDが正しいかは、友だち追加後にテストすることで確認できます。

