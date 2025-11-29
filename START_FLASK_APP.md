# Flaskアプリの起動方法

## 🚀 正しい起動方法

### ステップ1: todo_list_appフォルダに移動

```bash
cd todo_list_app
```

### ステップ2: Flaskアプリを起動

```bash
python main.py
```

## ✅ 起動確認

正常に起動すると、以下のような表示が出ます：

```
🚀 Todo List App サーバーを起動...
アクセス: http://localhost:5000
▲ 開発モードで実行中です
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

## 📋 ワンライナー（一度に実行）

```bash
cd todo_list_app && python main.py
```

PowerShellの場合：

```powershell
cd todo_list_app; python main.py
```

## ⚠️ エラーが出た場合

### エラー: "can't open file 'main.py'"

→ `todo_list_app`フォルダに移動してから実行してください。

### エラー: "No module named 'flask'"

→ 依存パッケージをインストールしてください：
```bash
pip install -r requirements.txt
```

