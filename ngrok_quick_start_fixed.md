# ngrok クイックスタート（修正版）

## 🚀 ngrokの起動方法

### 正しいパス

ngrokは以下の場所にあります：
```
C:\Users\mhero\OneDrive\デスクトップ\cursor練習\★ngrok\ngrok.exe
```

### 起動コマンド

PowerShellで以下を実行：

```powershell
& "C:\Users\mhero\OneDrive\デスクトップ\cursor練習\★ngrok\ngrok.exe" http 5000
```

### バッチファイルを使用（簡単）

`todo_list_app`フォルダに `start_ngrok.bat` を作成して、以下を保存：

```batch
@echo off
cd /d "C:\Users\mhero\OneDrive\デスクトップ\cursor練習\★ngrok"
ngrok.exe http 5000
```

その後、`start_ngrok.bat` をダブルクリックするだけで起動できます。

## 📋 起動後の確認

ngrokが起動すると、以下のような表示が出ます：

```
ngrok                                                                               

Session Status                online
Account                       your-email@example.com
Version                       3.x.x
Region                        Japan (jp)
Latency                       -
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://xxxx-xxxx.ngrok-free.app -> http://localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

**重要**: `Forwarding` の行に表示されるURL（例: `https://xxxx-xxxx.ngrok-free.app`）をコピーしてください。

このURLをLINE Developers ConsoleのWebhook URLに設定します。

## 🔗 Webhook URLの設定

LINE Developers Consoleで、以下の形式でWebhook URLを設定：

```
https://xxxx-xxxx.ngrok-free.app/line/webhook
```

（`xxxx-xxxx.ngrok-free.app` を実際のngrok URLに置き換え）

## ⚠️ 注意事項

- ngrokを起動したら、そのターミナルは開いたままにしておいてください
- Flaskアプリも別のターミナルで起動しておく必要があります
- ngrokのURLは起動のたびに変わります（無料プランの場合）

