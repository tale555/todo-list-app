"""
LINE Messaging APIの簡単なテストスクリプト
最小限のリクエストでテストします
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

from configs.config import LINE_CHANNEL_ACCESS_TOKEN, LINE_USER_ID


def test_simple():
    """シンプルなテスト"""
    
    print("=" * 60)
    print("LINE Messaging API シンプルテスト")
    print("=" * 60)
    print()
    
    if not LINE_CHANNEL_ACCESS_TOKEN:
        print("❌ Channel Access Tokenが設定されていません")
        return
    
    if not LINE_USER_ID:
        print("❌ User IDが設定されていません")
        return
    
    print(f"✅ Channel Access Token: {LINE_CHANNEL_ACCESS_TOKEN[:20]}...")
    print(f"✅ User ID: {LINE_USER_ID}")
    print()
    
    # 最小限のリクエスト
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    data = {
        "to": LINE_USER_ID,
        "messages": [
            {
                "type": "text",
                "text": "テストメッセージ"
            }
        ]
    }
    
    print("📤 リクエストを送信しています...")
    print(f"   URL: {url}")
    print(f"   User ID: {LINE_USER_ID}")
    print()
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        print(f"📥 レスポンス: {response.status_code}")
        print(f"   レスポンス本文: {response.text}")
        print()
        
        if response.status_code == 200:
            print("✅ 成功！LINEアプリでメッセージを確認してください")
        else:
            print("❌ 失敗")
            try:
                error_json = response.json()
                print(f"   エラー: {error_json}")
            except:
                pass
            
            print()
            print("🔍 確認事項:")
            print("   1. LINE公式アカウントを友だち追加していますか？")
            print("   2. User IDが正しいですか？")
            print("   3. Channel Access Tokenが有効ですか？")
            
    except Exception as e:
        print(f"❌ エラー: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_simple()

