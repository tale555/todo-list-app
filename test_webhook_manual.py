"""
Webhookエンドポイントを手動でテストするスクリプト
"""

import requests
import json

def test_webhook():
    """Webhookエンドポイントをテスト"""
    
    print("=" * 60)
    print("Webhookエンドポイント テスト")
    print("=" * 60)
    print()
    
    # テスト用のイベントデータ
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
    
    url = "http://localhost:5000/line/webhook"
    
    print(f"📤 テストリクエストを送信: {url}")
    print(f"   データ: {json.dumps(test_data, ensure_ascii=False, indent=2)}")
    print()
    
    try:
        response = requests.post(url, json=test_data, timeout=5)
        print(f"✅ レスポンス: {response.status_code}")
        print(f"   内容: {response.text}")
        print()
        print("💡 Flaskアプリのターミナルを確認してください")
        print("   User IDが表示されているはずです")
    except requests.exceptions.ConnectionError:
        print("❌ Flaskアプリに接続できません")
        print("   Flaskアプリが起動しているか確認してください:")
        print("   python main.py")
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")


if __name__ == "__main__":
    test_webhook()

