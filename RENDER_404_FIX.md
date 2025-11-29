# Renderで「Not Found」エラーが表示される場合の対処法

## ❌ 問題

アプリにアクセスすると「Not Found」エラーが表示される

## 🔍 原因

1. **Procfileの設定が正しくない**
2. **Renderの設定（Start Command）が正しくない**
3. **アプリが正しく起動していない**

## ✅ 解決方法

### ステップ1: Renderの設定を確認

1. Renderのダッシュボードでサービスを開く
2. 「Settings」タブをクリック
3. 「Start Command」を確認

**正しい設定**:
```
gunicorn main:app --bind 0.0.0.0:$PORT
```

### ステップ2: Procfileを確認

`Procfile`の内容を確認：

```
web: gunicorn main:app --bind 0.0.0.0:$PORT
```

### ステップ3: ログを確認

1. Renderのダッシュボードで「Logs」タブを開く
2. エラーメッセージがないか確認
3. アプリが正常に起動しているか確認

### ステップ4: 手動で再デプロイ

1. 「Manual Deploy」→「Deploy latest commit」をクリック
2. デプロイが完了するまで待つ

## 🔧 よくある問題と解決方法

### 問題1: Start Commandが間違っている

**間違い**:
```
gunicorn main:app
```

**正しい**:
```
gunicorn main:app --bind 0.0.0.0:$PORT
```

### 問題2: Root Directoryの設定が間違っている

- Root Directoryが空欄になっているか確認
- または、正しいパス（`todo_list_app`）が設定されているか確認

### 問題3: アプリが起動していない

ログを確認して、以下のメッセージが表示されているか確認：
- `環境変数から認証ファイルを作成しました`
- `Google Sheets API認証が成功しました`
- `Available at your primary URL`

## 📋 確認チェックリスト

- [ ] Start Commandが正しいか確認
- [ ] Procfileが正しいか確認
- [ ] Root Directoryが正しいか確認
- [ ] ログにエラーがないか確認
- [ ] アプリが正常に起動しているか確認

## 💡 デバッグ方法

1. **ログを確認**
   - Renderの「Logs」タブで詳細なログを確認
   - エラーメッセージを探す

2. **URLを確認**
   - 正しいURLにアクセスしているか確認
   - `https://todo-list-app-hoza.onrender.com/`（末尾のスラッシュを確認）

3. **手動で再デプロイ**
   - 「Manual Deploy」→「Deploy latest commit」をクリック

