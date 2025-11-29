# ngrokクイックスタート

## ngrokの場所

ngrokは以下のフォルダにあります：
```
C:\Users\mhero\OneDrive\デスクトップ\cursor練習\★ngrok\ngrok.exe
```

## 実行方法

### 方法1: フォルダに移動して実行（推奨）

1. ターミナルを開く
2. 以下のコマンドを実行：

```powershell
cd "C:\Users\mhero\OneDrive\デスクトップ\cursor練習\★ngrok"
.\ngrok.exe http 5000
```

### 方法2: フルパスで実行

```powershell
& "C:\Users\mhero\OneDrive\デスクトップ\cursor練習\★ngrok\ngrok.exe" http 5000
```

### 方法3: バッチファイルを使用

`todo_list_app`フォルダ内の`start_ngrok.bat`をダブルクリック

## 実行前の確認

**重要**: アプリ（`python main.py`）が起動している状態で実行してください。

## 実行後の手順

1. ngrokが起動すると、以下のようなURLが表示されます：
   ```
   Forwarding  https://xxxx-xxxx-xxxx.ngrok-free.app -> http://localhost:5000
   ```

2. このURL（`https://xxxx-xxxx-xxxx.ngrok-free.app`）をコピー

3. LINE Developers ConsoleでWebhook URLに設定：
   ```
   https://xxxx-xxxx-xxxx.ngrok-free.app/line/webhook
   ```

4. 「検証」ボタンをクリック → 成功を確認

5. 「Webhookの利用」をONにする

## 注意事項

- ngrokのURLは起動するたびに変わります（無料版の場合）
- ngrokを再起動したら、LINE Developers ConsoleでWebhook URLも更新が必要です
- ngrokとアプリの両方が起動している必要があります
