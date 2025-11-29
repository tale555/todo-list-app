# RenderのRoot Directoryエラー修正方法

## ❌ エラーの内容

```
==> Service Root Directory "/opt/render/project/src/todo_list_app" is missing.
builder.sh: line 51: cd: /opt/render/project/src/todo_list_app: No such file or directory
```

## 🔍 原因

Renderの設定で「Root Directory」に`todo_list_app`を指定していますが、GitHubリポジトリの構造と一致していない可能性があります。

## ✅ 解決方法

### 方法1: Root Directoryを空にする（推奨）

1. Renderのダッシュボードで、デプロイ中のサービスを開く
2. 「Settings」タブをクリック
3. 「Root Directory」フィールドを**空欄**にする
4. 「Save Changes」をクリック
5. デプロイが自動的に再実行されます

### 方法2: Root Directoryの設定を確認

GitHubリポジトリの構造を確認：

- リポジトリのルートに`todo_list_app`フォルダがある場合 → Root Directory: `todo_list_app`
- リポジトリのルートが既に`todo_list_app`フォルダの場合 → Root Directory: 空欄

## 📋 確認手順

1. GitHubリポジトリ（https://github.com/tale555/todo-list-app）にアクセス
2. リポジトリの構造を確認：
   - `main.py`がルートにあるか
   - `todo_list_app`フォルダがあるか

### パターンA: リポジトリのルートに`todo_list_app`フォルダがある場合

```
todo-list-app/
  ├── todo_list_app/
  │   ├── main.py
  │   ├── requirements.txt
  │   └── ...
  └── README.md
```

→ Root Directory: `todo_list_app`（現在の設定でOK）

### パターンB: リポジトリのルートが既に`todo_list_app`フォルダの場合

```
todo-list-app/
  ├── main.py
  ├── requirements.txt
  └── ...
```

→ Root Directory: **空欄**（設定を変更する必要があります）

## 🔧 修正手順

1. Renderのダッシュボードでサービスを開く
2. 「Settings」タブをクリック
3. 「Root Directory」を確認・修正：
   - パターンAの場合: `todo_list_app`のまま
   - パターンBの場合: **空欄**にする
4. 「Save Changes」をクリック
5. デプロイが自動的に再実行されます

## 💡 推奨設定

GitHubリポジトリの構造に応じて：

- **リポジトリのルートに`todo_list_app`フォルダがある場合**: Root Directory = `todo_list_app`
- **リポジトリのルートが既にアプリのフォルダの場合**: Root Directory = 空欄

## ⚠️ 注意事項

- 設定を変更すると、デプロイが自動的に再実行されます
- デプロイが完了するまで待ってから、再度確認してください

