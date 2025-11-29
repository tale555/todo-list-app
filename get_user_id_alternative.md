# User ID取得方法（Webhookイベントログなし）

## 方法1: 既存のUser IDでテスト（最も簡単）

現在設定されているUser ID（`Ubd12a463884a8bdb388ded25999bfa2e`）を使用してテストします。

### ステップ1: LINE公式アカウントを友だち追加

1. [LINE Developers Console](https://developers.line.biz/console/) にアクセス
2. 「Todoリスト」チャネルを開く
3. 「Messaging API」タブを開く
4. 公式アカウントのQRコードを表示
5. QRコードをスキャンして友だち追加

### ステップ2: テスト

友だち追加後、以下でテスト：

```bash
python test_line_notify.py
```

成功すれば、LINEアプリにメッセージが届きます！

## 方法2: 対話型でUser IDを入力

```bash
python test_line_interactive.py
```

実行時に、User IDを直接入力できます。

## 方法3: 別のチャネルからUser IDを確認

もし他のLINE BotやチャネルでUser IDを取得したことがあれば、そのUser IDを使用できます。

## 重要なポイント

- **友だち追加が必須です**。LINE Messaging APIでは、友だち追加していないユーザーにはメッセージを送信できません。
- 現在のUser IDが正しいかは、友だち追加後にテストすることで確認できます。

