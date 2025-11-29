@echo off
chcp 65001 >nul
REM ngrokを起動するシンプルなバッチファイル

cd /d "C:\Users\mhero\OneDrive\デスクトップ\cursor練習\★ngrok"
ngrok.exe http 5000

pause

