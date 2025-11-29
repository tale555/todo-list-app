"""
Webhookの状態を確認するスクリプト
"""

import requests
import json

def check_webhook_status():
    """Webhookの状態を確認"""
    
    print("=" * 60)
    print("Webhook状態確認")
    print("=" * 60)
    print()
    
    # 1. Flaskアプリが起動しているか確認
    print("1. Flaskアプリの状態を確認...")
    try:
        response = requests.get("http://localhost:5000", timeout=2)
        print(f"   ✅ Flaskアプリは起動しています (ステータス: {response.status_code})")
    except requests.exceptions.ConnectionError:
        print("   ❌ Flaskアプリが起動していません")
        print("      python main.py で起動してください")
        return
    except Exception as e:
        print(f"   ⚠️  エラー: {e}")
    
    print()
    
    # 2. Webhookエンドポイントをテスト
    print("2. Webhookエンドポイントをテスト...")
    test_data = {
        "events": [
            {
                "type": "message",
                "source": {
                    "userId": "U1234567890abcdefghijklmnopqrstuvw"
                },
                "message": {
                    "type": "text",
                    "text": "テストメッセージ"
                }
            }
        ]
    }
    
    try:
        response = requests.post(
            "http://localhost:5000/line/webhook",
            json=test_data,
            timeout=5
        )
        print(f"   ✅ Webhookエンドポイントは動作しています (ステータス: {response.status_code})")
        print(f"   レスポンス: {response.text}")
        print()
        print("   💡 Flaskアプリのターミナルを確認してください")
        print("      「📥 POSTリクエストを受信しました」と表示されるはずです")
    except requests.exceptions.ConnectionError:
        print("   ❌ Webhookエンドポイントに接続できません")
    except Exception as e:
        print(f"   ⚠️  エラー: {e}")
    
    print()
    print("=" * 60)
    print("確認完了")
    print("=" * 60)
    print()
    print("💡 次のステップ:")
    print("   1. Flaskアプリのターミナルで「📥 POSTリクエストを受信しました」が表示されるか確認")
    print("   2. LINE公式アカウントにメッセージを送信")
    print("   3. FlaskアプリのターミナルでUser IDが表示されるか確認")


if __name__ == "__main__":
    check_webhook_status()

