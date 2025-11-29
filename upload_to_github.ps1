# GitHubへのアップロードスクリプト
# PowerShellで実行してください

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "GitHubへのアップロード準備" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 現在のディレクトリを確認
$currentDir = Get-Location
Write-Host "現在のディレクトリ: $currentDir" -ForegroundColor Yellow

# todo_list_appフォルダに移動
if (Test-Path "todo_list_app") {
    Set-Location "todo_list_app"
    Write-Host "✅ todo_list_appフォルダに移動しました" -ForegroundColor Green
} else {
    Write-Host "❌ todo_list_appフォルダが見つかりません" -ForegroundColor Red
    Write-Host "このスクリプトをtodo_list_appフォルダの親ディレクトリで実行してください" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ステップ1: Gitリポジトリの初期化" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Gitがインストールされているか確認
try {
    $gitVersion = git --version
    Write-Host "✅ Gitがインストールされています: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Gitがインストールされていません" -ForegroundColor Red
    Write-Host "Gitをインストールしてください: https://git-scm.com/" -ForegroundColor Yellow
    exit 1
}

# Gitリポジトリを初期化
if (Test-Path ".git") {
    Write-Host "⚠️  Gitリポジトリは既に初期化されています" -ForegroundColor Yellow
} else {
    git init
    Write-Host "✅ Gitリポジトリを初期化しました" -ForegroundColor Green
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ステップ2: ファイルのステージング" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# .gitignoreが存在するか確認
if (Test-Path ".gitignore") {
    Write-Host "✅ .gitignoreが存在します" -ForegroundColor Green
} else {
    Write-Host "⚠️  .gitignoreが存在しません" -ForegroundColor Yellow
}

# ファイルをステージング
git add .
Write-Host "✅ ファイルをステージングしました" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ステップ3: コミット" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# コミット
git commit -m "Initial commit: Todo List App with LINE integration"
Write-Host "✅ コミットしました" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ステップ4: メインブランチの設定" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# メインブランチに設定
git branch -M main
Write-Host "✅ メインブランチに設定しました" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "次のステップ" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. GitHubでリポジトリを作成してください" -ForegroundColor Yellow
Write-Host "   https://github.com/new" -ForegroundColor Yellow
Write-Host ""
Write-Host "2. リポジトリを作成したら、以下のコマンドを実行してください:" -ForegroundColor Yellow
Write-Host ""
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git" -ForegroundColor Cyan
Write-Host "   git push -u origin main" -ForegroundColor Cyan
Write-Host ""
Write-Host "   (YOUR_USERNAMEとYOUR_REPO_NAMEを置き換えてください)" -ForegroundColor Yellow
Write-Host ""
Write-Host "詳細は GITHUB_UPLOAD_GUIDE.md を参照してください" -ForegroundColor Yellow
Write-Host ""

