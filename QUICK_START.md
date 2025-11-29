# クイックスタートガイド

## 🚀 アプリケーションの起動方法

### 1. 依存パッケージのインストール

```bash
cd todo_list_app
pip install -r requirements.txt
```

### 2. 環境変数ファイルの作成

`.env.example`をコピーして`.env`ファイルを作成してください。

**Windowsの場合:**
```bash
copy .env.example .env
```

**Mac/Linuxの場合:**
```bash
cp .env.example .env
```

**注意**: `.env.example`ファイルが存在しない場合は、以下の内容で`.env`ファイルを手動で作成してください：

```env
# Google Sheets API 認証ファイルのパス
GOOGLE_CREDENTIALS_PATH=configs/credentials.json

# GoogleスプレッドシートID（後で設定）
SPREADSHEET_ID=

# シート名
SHEET_NAME=Sheet1
```

### 3. アプリケーションの起動

```bash
python main.py
```

### 4. ブラウザでアクセス

ブラウザで以下のURLを開いてください：
- http://localhost:5000

「Hello World」が表示されれば成功です！

---

## ⚠️ 現在の状態

現在は**タスク1完了**の状態です。以下の機能はまだ実装されていません：

- ❌ Google Sheets API連携
- ❌ Todoデータの保存・読み取り
- ❌ Todo一覧表示
- ❌ Todo登録・編集

次のタスク（タスク2: Google Sheets API連携の実装）に進む前に、Google Sheets APIの設定が必要です。

詳細は [USER_SETUP_GUIDE.md](USER_SETUP_GUIDE.md) を参照してください。

