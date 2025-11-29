"""
ローカルでWebhookエンドポイントをテストするスクリプト
"""

import requests
import json

def test_webhook_endpoint():
    """Webhookエンドポイントをテスト"""
    
    print("=" * 60)
    print("Webhookエンドポイント ローカルテスト")
    print("=" * 60)
    print()
    
    # ローカルのWebhook URL
    webhook_url = "http://localhost:5000/line/webhook"
    
    print(f"📤 テストURL: {webhook_url}")
    print()
    
    # GETリクエスト（LINEの検証用）
    print("1. GETリクエスト（検証用）を送信...")
    try:
        response = requests.get(webhook_url, timeout=5)
        print(f"   ステータスコード: {response.status_code}")
        print(f"   レスポンス: {response.text[:100]}")
        
        if response.status_code == 200:
            print("   ✅ GETリクエストは成功しました")
        else:
            print(f"   ❌ GETリクエストが失敗しました（期待: 200, 実際: {response.status_code}）")
    except requests.exceptions.ConnectionError:
        print("   ❌ 接続エラー: アプリが起動していない可能性があります")
        print("      python main.py でアプリを起動してください")
    except Exception as e:
        print(f"   ❌ エラー: {e}")
    
    print()
    
    # POSTリクエスト（LINEのイベント用）
    print("2. POSTリクエスト（イベント用）を送信...")
    test_event = {
        "events": [
            {
                "type": "message",
                "source": {
                    "userId": "test_user_id"
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
            webhook_url,
            json=test_event,
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        print(f"   ステータスコード: {response.status_code}")
        print(f"   レスポンス: {response.text[:100]}")
        
        if response.status_code == 200:
            print("   ✅ POSTリクエストは成功しました")
        else:
            print(f"   ❌ POSTリクエストが失敗しました（期待: 200, 実際: {response.status_code}）")
    except requests.exceptions.ConnectionError:
        print("   ❌ 接続エラー: アプリが起動していない可能性があります")
        print("      python main.py でアプリを起動してください")
    except Exception as e:
        print(f"   ❌ エラー: {e}")
    
    print()
    print("=" * 60)
    print("テスト完了")
    print("=" * 60)
    print()
    print("💡 ヒント:")
    print("   - アプリが起動していることを確認してください")
    print("   - ngrokを使用する場合、ngrokのURL + /line/webhook を設定してください")
    print("   - 例: https://xxxx-xxxx.ngrok-free.app/line/webhook")


if __name__ == "__main__":
    test_webhook_endpoint()

