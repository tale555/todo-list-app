"""
LINE公式アカウントの友だち追加状態を確認するスクリプト
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

from configs.config import LINE_CHANNEL_ACCESS_TOKEN, LINE_USER_ID


def check_friend_status():
    """友だち追加状態を確認"""
    
    print("=" * 60)
    print("LINE公式アカウント 友だち追加状態確認")
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
    
    # LINE Messaging APIで友だち追加状態を確認
    # 注意: LINE Messaging APIには直接友だち状態を確認するAPIがないため、
    # メッセージを送信してみてエラーで判断します
    
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
                "text": "友だち追加確認テスト"
            }
        ]
    }
    
    print("📤 テストメッセージを送信して状態を確認...")
    print()
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            print("✅ 成功！友だち追加されています")
            print("   LINEアプリでメッセージを確認してください")
        elif response.status_code == 400:
            error_json = response.json()
            error_message = error_json.get('message', '')
            
            if 'Failed to send messages' in error_message:
                print("❌ エラー: メッセージの送信に失敗しました")
                print()
                print("🔍 考えられる原因:")
                print("   1. LINE公式アカウントが友だち追加されていない")
                print("   2. User IDが友だち追加後に取得されていない")
                print("   3. User IDが間違っている")
                print()
                print("💡 解決方法:")
                print("   1. LINE公式アカウントを友だち追加してください")
                print("   2. 友だち追加後、公式アカウントにメッセージを送信")
                print("   3. Webhookイベントから新しいUser IDを取得")
                print("   4. .envファイルのLINE_USER_IDを更新")
        else:
            print(f"❌ エラー: {response.status_code}")
            print(f"   レスポンス: {response.text}")
            
    except Exception as e:
        print(f"❌ エラー: {e}")


if __name__ == "__main__":
    check_friend_status()

