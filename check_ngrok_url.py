"""
ngrokのURLを確認するスクリプト
"""

import requests
import json

def check_ngrok_url():
    """ngrokのURLを確認"""
    
    print("=" * 60)
    print("ngrok URL確認")
    print("=" * 60)
    print()
    
    try:
        # ngrokのAPIにアクセス
        response = requests.get("http://127.0.0.1:4040/api/tunnels", timeout=2)
        
        if response.status_code == 200:
            data = response.json()
            tunnels = data.get('tunnels', [])
            
            if tunnels:
                print("✅ ngrokが起動しています！")
                print()
                for tunnel in tunnels:
                    public_url = tunnel.get('public_url', '')
                    config = tunnel.get('config', {})
                    addr = config.get('addr', '')
                    
                    print(f"Public URL: {public_url}")
                    print(f"Forwarding: {public_url} -> {addr}")
                    print()
                
                # Webhook URLを表示
                if tunnels:
                    public_url = tunnels[0].get('public_url', '')
                    webhook_url = f"{public_url}/line/webhook"
                    print("=" * 60)
                    print("📋 LINE Developers Consoleで設定するWebhook URL:")
                    print("=" * 60)
                    print(webhook_url)
                    print("=" * 60)
            else:
                print("⚠️  ngrokは起動していますが、トンネルが見つかりません")
                print("   ngrokのターミナルでエラーが出ていないか確認してください")
        else:
            print(f"❌ ngrok APIへのアクセスに失敗しました: {response.status_code}")
            print("   ngrokが起動しているか確認してください")
            
    except requests.exceptions.ConnectionError:
        print("❌ ngrokが起動していないようです")
        print()
        print("💡 ngrokを起動する方法:")
        print("   1. 新しいターミナルを開く")
        print("   2. 以下を実行:")
        print('      & "C:\\Users\\mhero\\OneDrive\\デスクトップ\\cursor練習\\★ngrok\\ngrok.exe" http 5000')
        print()
        print("   または、バッチファイルを使用:")
        print("      cd todo_list_app")
        print("      start_ngrok.bat")
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        print()
        print("💡 ngrokのターミナル出力を直接確認してください")
        print("   ngrokが起動すると、以下のような表示が出ます:")
        print("   Forwarding  https://xxxx-xxxx.ngrok-free.app -> http://localhost:5000")


if __name__ == "__main__":
    check_ngrok_url()

