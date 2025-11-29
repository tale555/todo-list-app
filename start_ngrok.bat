@echo off
chcp 65001 >nul
REM ngrokを起動するバッチファイル

echo ========================================
echo ngrok起動中...
echo ========================================
echo.

REM 絶対パスでngrok.exeを実行
set NGROK_PATH=C:\Users\mhero\OneDrive\デスクトップ\cursor練習\★ngrok\ngrok.exe

if exist "%NGROK_PATH%" (
    echo ngrok.exeが見つかりました
    echo 起動しています...
    echo.
    cd /d "C:\Users\mhero\OneDrive\デスクトップ\cursor練習\★ngrok"
    ngrok.exe http 5000
) else (
    echo エラー: ngrok.exeが見つかりません
    echo.
    echo 確認してください: %NGROK_PATH%
    echo.
    pause
    exit /b 1
)

