# Todoリストアプリ

Python + Flaskで作成したTodoリストWebアプリケーションです。データの保存にはGoogleスプレッドシートを使用します。

## 📋 機能

- ✅ やることを登録・編集できる
- ✅ タイトル・内容・期日の3つを設定できる
- ✅ データの保存にはGoogleスプレッドシートを使用
- ✅ 登録したやることリストを一覧で確認できるページ
- ✅ 検索・フィルター機能（タイトル・内容・期日・カテゴリで検索・フィルター）
- ✅ 完了機能（完了済みTodoの管理）
- ✅ カテゴリ・タグ機能（カテゴリ別の色分け表示）
- ✅ ドラッグ&ドロップで順序変更
- ✅ 一時保存機能（下書き管理）
- ✅ **LINE通知機能**（期日3日前・前日・当日に自動通知）

## 🚀 クイックスタート

### 1. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定

`.env.example`をコピーして`.env`を作成し、必要な値を設定してください。

```bash
# Windowsの場合
copy .env.example .env

# Mac/Linuxの場合
cp .env.example .env
```

### 3. アプリケーションの起動

```bash
python main.py
```

ブラウザで `http://localhost:5000` にアクセスしてください。

### 4. Google Sheets API接続のテスト

Google Sheets APIが正しく設定されているか確認するには：

**方法1: テストスクリプトを実行**
```bash
python test_sheets.py
```

**方法2: ブラウザでテストエンドポイントにアクセス**
```
http://localhost:5000/test-sheets
```

成功すると、スプレッドシートの情報がJSON形式で表示されます。

## 📁 プロジェクト構造

```
todo_list_app/
├── README.md              # このファイル
├── PROJECT_PLAN.md        # 開発計画書
├── SETUP_GUIDE.md         # セットアップガイド（後で作成）
├── requirements.txt       # 依存パッケージ
├── .env.example           # 環境変数テンプレート
├── main.py                # Flaskアプリケーション
├── configs/               # 設定ファイル
├── core/                  # コアロジック
├── templates/             # HTMLテンプレート
└── static/                # 静的ファイル（CSS, JS）
```

## 📚 ドキュメント

- [PROJECT_PLAN.md](PROJECT_PLAN.md) - 開発計画の詳細
- [USER_SETUP_GUIDE.md](USER_SETUP_GUIDE.md) - **ユーザー向けセットアップガイド（開発開始前に読む）**
- [LINE_SETUP_GUIDE.md](LINE_SETUP_GUIDE.md) - **LINE連携セットアップガイド（LINE通知機能の設定方法）**
- [TASK_STATUS.md](TASK_STATUS.md) - タスク進捗管理
- [QUICK_START.md](QUICK_START.md) - クイックスタートガイド
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - **トラブルシューティングガイド（エラーが発生した場合）**
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - **デプロイガイド（サーバーで公開する場合）**

## ⚠️ 注意事項

### Google Sheets APIの設定

Google Sheets APIを使用するには、以下の設定が必要です：

1. **認証ファイルの配置**
   - `configs/credentials.json`にサービスアカウントのJSON認証ファイルを配置
   - または、既存の認証ファイル（`../configs/silent-life-473721-e2-bd839ba557ad.json`）を使用する場合は、`.env`ファイルでパスを指定

2. **スプレッドシートIDの設定**
   - `.env`ファイルに`SPREADSHEET_ID`を設定
   - スプレッドシートのURLから取得: `https://docs.google.com/spreadsheets/d/【ここがスプレッドシートID】/edit`
   - **重要**: 完全なURLではなく、ID部分だけを設定してください
   - 例: URLが `https://docs.google.com/spreadsheets/d/1A2B3C4D5E6F7G8H9I0J/edit` の場合
     - `.env`ファイルには `SPREADSHEET_ID=1A2B3C4D5E6F7G8H9I0J` と設定
   - **注意**: 完全なURLを設定しても自動的にIDが抽出されますが、IDのみを設定することを推奨します

3. **サービスアカウントへの権限付与**
   - 作成したスプレッドシートにサービスアカウントのメールアドレスを共有（編集権限）

詳細は [USER_SETUP_GUIDE.md](USER_SETUP_GUIDE.md) を参照してください。

### LINE通知機能の設定

LINE通知機能を使用するには、LINE Notifyトークンの設定が必要です。

1. **LINE Notifyトークンの取得**
   - [LINE Notify](https://notify-bot.line.me/) にアクセスしてトークンを発行
   
2. **環境変数の設定**
   - `.env`ファイルに`LINE_NOTIFY_TOKEN`を設定

詳細は [LINE_SETUP_GUIDE.md](LINE_SETUP_GUIDE.md) を参照してください。

### エラーが発生した場合

認証エラーなどが発生した場合は、以下を試してください：

1. **認証ファイルの確認**
   ```bash
   python check_credentials.py
   ```

2. **スプレッドシートIDの確認**
   ```bash
   python check_spreadsheet_id.py
   ```

2. **トラブルシューティングガイドを参照**
   - [TROUBLESHOOTING.md](TROUBLESHOOTING.md) を確認

3. **既存の認証ファイルを使用する場合**
   
   `.env`ファイルに以下を追加：
   ```env
   GOOGLE_CREDENTIALS_PATH=../configs/silent-life-473721-e2-bd839ba557ad.json
   ```

## 🔧 必要な環境

- Python 3.8以上
- Googleアカウント（Google Sheets API使用のため）

## 📝 ライセンス

このプロジェクトは個人利用・学習目的で作成されています。

