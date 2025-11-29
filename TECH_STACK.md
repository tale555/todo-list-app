# 使用技術スタック

## 📋 このTodo Listアプリで使用した技術一覧

### 🐍 言語

- **Python 3.x**
  - メインのプログラミング言語
  - バックエンドロジック、データ処理、API連携に使用

### 🖼️ フレームワーク

- **Flask 3.0.0以上**
  - Webアプリケーションフレームワーク
  - ルーティング、テンプレートレンダリング、リクエスト処理に使用

### 💾 データベース・データストア

- **Google Sheets API**
  - データベースとしてGoogleスプレッドシートを使用
  - Todoデータの永続化に使用
  - 以下のライブラリを使用：
    - `google-api-python-client` (Google APIクライアント)
    - `google-auth` (Google認証)
    - `google-auth-oauthlib` (OAuth認証)
    - `google-auth-httplib2` (HTTP認証)

### 🔧 その他ツール・ライブラリ

#### 環境変数管理
- **python-dotenv**
  - `.env`ファイルから環境変数を読み込む

#### HTTP通信
- **requests**
  - LINE Messaging APIとの通信に使用
  - HTTPリクエスト送信

#### 日時処理
- **python-dateutil**
  - 日付・時刻の処理、計算に使用

#### 本番環境用サーバー
- **gunicorn**
  - 本番環境でのWSGIサーバー（デプロイ時）

### 📱 外部API・サービス

- **LINE Messaging API**
  - Todoの期日リマインダー通知に使用
  - Push Message APIでメッセージ送信

- **Google Sheets API**
  - データストアとして使用
  - CRUD操作を実装

### 🎨 フロントエンド技術

- **HTML5**
  - ページ構造の定義

- **CSS3**
  - スタイリング、レスポンシブデザイン
  - Flexbox、Gridレイアウト
  - アニメーション、トランジション

- **JavaScript (ES6+)**
  - クライアントサイドの動的処理
  - DOM操作
  - Fetch API（非同期通信）
  - HTML5 Drag and Drop API（順番変更機能）
  - LocalStorage API（一時保存機能）

### 🛠️ 開発ツール

- **ngrok**
  - ローカル開発環境をインターネットに公開
  - LINE Webhookのテストに使用

- **Git**
  - バージョン管理（想定）

### 📦 パッケージ管理

- **pip**
  - Pythonパッケージのインストール・管理
  - `requirements.txt`で依存関係を管理

## 📊 技術構成図

```
┌─────────────────────────────────────┐
│        フロントエンド                │
│  HTML5 + CSS3 + JavaScript          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│      Flask (Python Web Framework)   │
│  - ルーティング                     │
│  - テンプレートレンダリング          │
│  - リクエスト処理                    │
└──────┬──────────────┬───────────────┘
       │              │
       ▼              ▼
┌─────────────┐  ┌──────────────┐
│ Google      │  │ LINE         │
│ Sheets API  │  │ Messaging API│
│ (データ保存) │  │ (通知送信)   │
└─────────────┘  └──────────────┘
```

## 🔑 主要な依存関係

```txt
flask>=3.0.0
google-api-python-client>=2.108.0
google-auth>=2.23.4
google-auth-oauthlib>=1.1.0
google-auth-httplib2>=0.1.1
python-dotenv>=1.0.0
python-dateutil>=2.8.2
requests>=2.31.0
gunicorn>=21.2.0
```

## 📝 まとめ

- **言語**: Python
- **フレームワーク**: Flask
- **データベース**: Google Sheets API（データストアとして）
- **主要ライブラリ**: requests, python-dotenv, python-dateutil
- **外部API**: LINE Messaging API, Google Sheets API
- **フロントエンド**: HTML5, CSS3, JavaScript
- **開発ツール**: ngrok

