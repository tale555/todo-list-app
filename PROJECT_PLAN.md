# Todoリストアプリ - 開発計画書

## 📋 プロジェクト概要

PythonでTodoリストWebアプリケーションを作成し、サーバーで公開します。

### 機能要件
- ✅ やることを登録・編集できる
- ✅ タイトル・内容・期日の3つを設定できる
- ✅ データの保存にはGoogleスプレッドシートを使用
- ✅ 登録したやることリストを一覧で確認できるページ

### 技術スタック
- **バックエンド**: Python + Flask
- **フロントエンド**: HTML + CSS + JavaScript
- **データベース**: Googleスプレッドシート（Google Sheets API）
- **デプロイ**: サーバー公開（Render/Railway/Heroku等）

---

## 📁 プロジェクト構造

```
todo_list_app/
├── README.md                    # プロジェクト説明
├── PROJECT_PLAN.md              # このファイル（開発計画書）
├── SETUP_GUIDE.md               # セットアップガイド（後で作成）
├── requirements.txt             # 依存パッケージ
├── .env.example                 # 環境変数テンプレート
├── main.py                      # Flaskアプリケーション（エントリーポイント）
├── configs/
│   └── config.py                # 設定ファイル
├── core/
│   ├── __init__.py
│   ├── sheets_manager.py        # Google Sheets操作クラス
│   └── todo_manager.py          # Todo管理ロジック
├── templates/
│   ├── base.html                # ベーステンプレート
│   ├── index.html               # 一覧ページ
│   └── edit.html                # 登録・編集ページ
├── static/
│   ├── css/
│   │   └── style.css            # スタイルシート
│   └── js/
│       └── main.js              # JavaScript（必要に応じて）
└── logs/                        # ログファイル（.gitignoreに追加）
```

---

## 🎯 タスク分割

開発は以下の順序で進めます。**各タスクが完了したら、次のタスクに進む前に必ず確認を取ります。**

### タスク1: プロジェクト基盤の構築
**目標**: プロジェクトフォルダと基本ファイルを作成し、Flaskアプリケーションを起動できる状態にする

**作業内容**:
1. `todo_list_app`フォルダを作成
2. 基本的なフォルダ構造を作成（configs, core, templates, static）
3. `requirements.txt`を作成（Flask、Google Sheets API関連パッケージ）
4. `.env.example`ファイルを作成
5. `main.py`でFlaskアプリケーションの基本構造を作成
6. 簡単な「Hello World」ページを表示できるようにする
7. ローカルで動作確認

**完了条件**:
- `python main.py`でFlaskサーバーが起動する
- ブラウザで`http://localhost:5000`にアクセスして「Hello World」が表示される

**ユーザー側の作業**:
- なし（自動で作成されます）

---

### タスク2: Google Sheets API連携の実装
**目標**: Googleスプレッドシートとの読み書きができるようにする

**作業内容**:
1. `configs/config.py`で設定を管理
2. `core/sheets_manager.py`を作成（既存の`google_apis/google_sheets_sender.py`を参考に）
3. Google Sheets APIの認証処理を実装
4. スプレッドシートの作成・読み取り・書き込み機能を実装
5. テスト用のスプレッドシートを作成して動作確認

**完了条件**:
- Google Sheets APIでスプレッドシートにデータを書き込める
- スプレッドシートからデータを読み取れる

**ユーザー側の作業**:
1. Google Cloud Consoleでプロジェクトを作成（既存の認証ファイルがあれば使用可能）
2. Google Sheets APIを有効化
3. サービスアカウントを作成してJSON認証ファイルをダウンロード
4. `.env`ファイルに認証ファイルのパスを設定
5. 作成したスプレッドシートにサービスアカウントのメールアドレスを共有（編集権限）

**詳細な手順**: [USER_SETUP_GUIDE.md](USER_SETUP_GUIDE.md) を参照してください

---

### タスク3: Todoデータモデルと管理ロジックの実装
**目標**: Todoアイテム（タイトル・内容・期日）を管理するロジックを作成

**作業内容**:
1. `core/todo_manager.py`を作成
2. Todoアイテムのデータ構造を定義（タイトル、内容、期日、ID）
3. Google Sheetsへの保存・読み取り・更新・削除機能を実装
4. スプレッドシートの構造を設計（ヘッダー行: ID, タイトル, 内容, 期日, 作成日時）
5. データのバリデーション（必須項目チェック等）

**完了条件**:
- TodoアイテムをGoogle Sheetsに保存できる
- 保存したTodoアイテムを読み取れる
- Todoアイテムを更新・削除できる

**ユーザー側の作業**:
- なし（タスク2で設定済み）

---

### タスク4: 一覧表示ページの実装
**目標**: 登録したTodoリストを一覧で表示するページを作成

**作業内容**:
1. `templates/base.html`を作成（共通レイアウト）
2. `templates/index.html`を作成（一覧ページ）
3. `static/css/style.css`を作成（基本的なスタイル）
4. FlaskルートでTodo一覧を取得してテンプレートに渡す
5. 一覧ページに「新規登録」ボタンを追加
6. 期日の表示（日付フォーマット、期限切れの色分け等）

**完了条件**:
- ブラウザで一覧ページが表示される
- 登録済みのTodoが一覧で表示される
- 期日が正しく表示される

**ユーザー側の作業**:
- なし

---

### タスク5: 登録・編集ページの実装
**目標**: Todoを登録・編集するページを作成

**作業内容**:
1. `templates/edit.html`を作成（登録・編集フォーム）
2. フォームにタイトル・内容・期日の入力欄を追加
3. FlaskルートでPOSTリクエストを受け取り、データを保存
4. 編集機能: 既存のTodoを読み込んでフォームに表示
5. バリデーション（必須項目チェック、日付形式チェック等）
6. 登録・更新後のリダイレクト処理

**完了条件**:
- 新規Todoを登録できる
- 既存のTodoを編集できる
- バリデーションエラーが表示される

**ユーザー側の作業**:
- なし

---

### タスク6: UI/UXの改善
**目標**: 見た目を整え、使いやすくする

**作業内容**:
1. CSSでモダンなデザインを適用
2. レスポンシブデザイン（スマホ対応）
3. 削除機能の追加（一覧ページに削除ボタン）
4. 完了/未完了の切り替え機能（オプション）
5. エラーメッセージの表示改善
6. ローディング表示（必要に応じて）

**完了条件**:
- 見た目が整っている
- スマホでも使いやすい
- 削除機能が動作する

**ユーザー側の作業**:
- なし

---

### タスク7: サーバーへのデプロイ
**目標**: アプリケーションをサーバーで公開する

**作業内容**:
1. `Procfile`を作成（Render/Heroku用）
2. `runtime.txt`を作成（Pythonバージョン指定）
3. 環境変数の設定方法をドキュメント化
4. デプロイ手順を`SETUP_GUIDE.md`に追加
5. デプロイ後の動作確認

**完了条件**:
- サーバーでアプリケーションが起動する
- 公開URLからアクセスできる
- すべての機能が動作する

**ユーザー側の作業**:
1. Render/Railway/Heroku等のアカウントを作成（事前準備: [USER_SETUP_GUIDE.md](USER_SETUP_GUIDE.md) 参照）
2. 新しいプロジェクトを作成
3. GitHubリポジトリに接続（または直接デプロイ）
4. 環境変数を設定（Google Sheets認証情報等）
5. デプロイを実行

**詳細な手順**: 後で`SETUP_GUIDE.md`に記載します

---

## 📝 既存リソースの活用

### 使用可能な既存ファイル
- `google_apis/google_sheets_sender.py` - Google Sheets API操作の参考
- `configs/config.py` - 設定ファイルの参考
- `configs/silent-life-473721-e2-bd839ba557ad.json` - 既存の認証ファイル（使用可能な場合）

### 既存の認証ファイルを使用する場合
既存のGoogleサービスアカウント認証ファイル（`configs/silent-life-473721-e2-bd839ba557ad.json`）が使用可能な場合は、それを流用できます。

---

## 🔧 開発環境の要件

### 必要なもの
- Python 3.8以上
- Googleアカウント（Google Sheets API使用のため）
- サーバーアカウント（Render/Railway/Heroku等、無料プラン可）

### インストールが必要なパッケージ（主要なもの）
- Flask（Webフレームワーク）
- google-api-python-client（Google Sheets API）
- google-auth（認証）
- python-dotenv（環境変数管理）

---

## 📌 開発の進め方

### 重要なルール
1. **一つのタスクが完了してから次のタスクに進む**
2. **各タスク完了時に「タスク○完了」と報告**
3. **次のタスクに進む前に必ずユーザーの確認を取る**
4. **ユーザー側の作業が必要な場合は、初心者でもわかりやすく説明**

### タスク完了の報告形式
各タスク完了時には以下のような形式で報告します：
```
✅ タスク1完了: プロジェクト基盤の構築が完了しました。
- Flaskアプリケーションが起動できる状態になりました
- 次のタスク（Google Sheets API連携）に進みますか？
```

---

## 🎨 デザイン方針

- シンプルで使いやすいUI
- モダンなデザイン（Bootstrap等のCSSフレームワークは使用可）
- レスポンシブデザイン（スマホ対応）
- 期日が近い/期限切れのTodoは色分け表示

---

## 📚 参考資料

### このプロジェクトのドキュメント
- [README.md](README.md) - プロジェクト概要
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - このファイル（開発計画書）
- [USER_SETUP_GUIDE.md](USER_SETUP_GUIDE.md) - **ユーザー向けセットアップガイド（開発開始前に読む）**
- [TASK_STATUS.md](TASK_STATUS.md) - タスク進捗管理
- [SETUP_GUIDE.md](SETUP_GUIDE.md) - セットアップガイド（開発開始後に作成）

### 既存のドキュメント
- `dify_line_bot/SETUP_GUIDE.md` - セットアップガイドの参考
- `docs/README_Google_Sheets.md` - Google Sheets APIの説明（存在する場合）

### 外部リソース
- Flask公式ドキュメント: https://flask.palletsprojects.com/
- Google Sheets API: https://developers.google.com/sheets/api

---

## ⚠️ 注意事項

1. **認証情報の管理**: `.env`ファイルや認証JSONファイルは`.gitignore`に追加して、Gitにコミットしないようにする
2. **エラーハンドリング**: 適切なエラーメッセージを表示する
3. **セキュリティ**: 本番環境では適切なセキュリティ設定を行う

---

## 📅 次のステップ

明日から開発を開始する際は、**タスク1から順番に進めていきます**。

準備ができたら、以下のコマンドで開発を開始できます：
```bash
# プロジェクトフォルダに移動
cd todo_list_app

# 依存パッケージをインストール
pip install -r requirements.txt

# アプリケーションを起動
python main.py
```

---

**作成日**: 2024年（今日の日付）
**最終更新**: 開発開始前の準備段階

