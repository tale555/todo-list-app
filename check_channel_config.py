"""
LINE Developers Consoleのチャネル設定を確認するスクリプト
現在の設定と、どのチャネルを使っているか確認します
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

from configs.config import LINE_CHANNEL_ACCESS_TOKEN, LINE_USER_ID


def check_channel_info():
    """チャネル情報を確認"""
    
    print("=" * 60)
    print("LINE Developers Console チャネル設定確認")
    print("=" * 60)
    print()
    
    if not LINE_CHANNEL_ACCESS_TOKEN:
        print("❌ Channel Access Tokenが設定されていません")
        return
    
    print(f"✅ Channel Access Token: {LINE_CHANNEL_ACCESS_TOKEN[:30]}...")
    print()
    
    # LINE Messaging APIでチャネル情報を取得
    url = "https://api.line.me/v2/bot/info"
    headers = {
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            channel_info = response.json()
            print("✅ チャネル情報を取得しました")
            print()
            print("📋 チャネル情報:")
            print(f"   チャネルID: {channel_info.get('channelId', 'N/A')}")
            print(f"   チャネル名: {channel_info.get('displayName', 'N/A')}")
            print(f"   チャネル説明: {channel_info.get('description', 'N/A')}")
            print()
            print("💡 このチャネルIDを使って、LINE Developers Consoleで")
            print("   正しいチャネルのWebhook URLを設定してください")
            print()
            print("🔍 確認手順:")
            print("   1. LINE Developers Consoleにアクセス")
            print("   2. 上記のチャネルIDでチャネルを探す")
            print("   3. そのチャネルの「Messaging API」タブを開く")
            print("   4. Webhook URLを設定")
            print()
        elif response.status_code == 401:
            print("❌ 認証エラー: Channel Access Tokenが無効です")
            print("   Channel Access Tokenを再発行してください")
        else:
            print(f"❌ エラー: {response.status_code}")
            print(f"   レスポンス: {response.text}")
            
    except Exception as e:
        print(f"❌ エラー: {e}")
        import traceback
        traceback.print_exc()


def check_webhook_url():
    """Webhook URLの設定を確認"""
    
    print("=" * 60)
    print("Webhook URL設定確認")
    print("=" * 60)
    print()
    
    if not LINE_CHANNEL_ACCESS_TOKEN:
        print("❌ Channel Access Tokenが設定されていません")
        return
    
    # LINE Messaging APIでWebhook URLを取得
    url = "https://api.line.me/v2/bot/channel/webhook/endpoint"
    headers = {
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            webhook_info = response.json()
            endpoint = webhook_info.get('endpoint', 'N/A')
            active = webhook_info.get('active', False)
            
            print("✅ Webhook設定を取得しました")
            print()
            print(f"   Webhook URL: {endpoint}")
            print(f"   有効: {'はい' if active else 'いいえ'}")
            print()
            
            if endpoint == 'N/A' or not endpoint:
                print("⚠️  Webhook URLが設定されていません")
            elif 'your-domain.com' in endpoint:
                print("⚠️  Webhook URLがプレースホルダーのままです")
                print("   正しいURLを設定してください")
            elif not active:
                print("⚠️  Webhookが無効になっています")
                print("   LINE Developers Consoleで「Webhookの利用」をONにしてください")
            else:
                print("✅ Webhook URLは正しく設定されています")
                
        elif response.status_code == 401:
            print("❌ 認証エラー: Channel Access Tokenが無効です")
        else:
            print(f"❌ エラー: {response.status_code}")
            print(f"   レスポンス: {response.text}")
            
    except Exception as e:
        print(f"❌ エラー: {e}")


if __name__ == "__main__":
    print()
    check_channel_info()
    print()
    check_webhook_url()
    print()
    print("=" * 60)
    print("確認完了")
    print("=" * 60)

