# ngrok起動ガイド

## 🚀 最も簡単な方法

### 方法1: シンプルなバッチファイルを使用（推奨）

`todo_list_app`フォルダにある `start_ngrok_simple.bat` をダブルクリックするだけです。

### 方法2: PowerShellで直接実行

新しいPowerShellターミナルを開いて、以下を実行：

```powershell
cd "C:\Users\mhero\OneDrive\デスクトップ\cursor練習\★ngrok"
.\ngrok.exe http 5000
```

### 方法3: コマンドプロンプトで実行

新しいコマンドプロンプトを開いて、以下を実行：

```cmd
cd /d "C:\Users\mhero\OneDrive\デスクトップ\cursor練習\★ngrok"
ngrok.exe http 5000
```

## ✅ 起動確認

ngrokが正常に起動すると、以下のような表示が出ます：

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

## 📋 次のステップ

1. ngrokのURLをコピー
2. LINE Developers ConsoleでWebhook URLを設定：
   ```
   https://xxxx-xxxx.ngrok-free.app/line/webhook
   ```
3. Flaskアプリを起動（別のターミナルで）：
   ```bash
   cd todo_list_app
   python main.py
   ```
4. LINE公式アカウントを友だち追加
5. FlaskアプリのターミナルにUser IDが表示されます

## ⚠️ トラブルシューティング

### エラー: "ngrok.exeが見つかりません"

- パスが正しいか確認してください
- `★ngrok`フォルダに`ngrok.exe`が存在するか確認してください

### エラー: "指定されたパスが見つかりません"

- フォルダ名に特殊文字（★）が含まれているため、パスを確認してください
- シンプルなバッチファイル（`start_ngrok_simple.bat`）を使用してください

### ngrokが起動しない

- 別のプログラムがポート5000を使用していないか確認してください
- 管理者権限で実行してみてください

