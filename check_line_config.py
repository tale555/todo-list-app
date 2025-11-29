"""
LINE Messaging API設定の確認スクリプト
"""

import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

from configs.config import LINE_CHANNEL_ACCESS_TOKEN, LINE_USER_ID


def check_line_config():
    """LINE Messaging API設定を確認"""
    
    print("=" * 60)
    print("LINE Messaging API設定確認")
    print("=" * 60)
    print()
    
    # Channel Access Tokenの確認
    if LINE_CHANNEL_ACCESS_TOKEN:
        print(f"✅ LINE_CHANNEL_ACCESS_TOKEN: 設定済み ({LINE_CHANNEL_ACCESS_TOKEN[:20]}...)")
    else:
        print("❌ LINE_CHANNEL_ACCESS_TOKEN: 未設定")
        print("   .envファイルに以下を追加してください:")
        print("   LINE_CHANNEL_ACCESS_TOKEN=your_channel_access_token_here")
    
    print()
    
    # User IDの確認
    if LINE_USER_ID:
        print(f"✅ LINE_USER_ID: 設定済み ({LINE_USER_ID[:20]}...)")
    else:
        print("❌ LINE_USER_ID: 未設定")
        print("   .envファイルに以下を追加してください:")
        print("   LINE_USER_ID=your_user_id_here")
        print()
        print("   💡 User IDの取得方法:")
        print("   1. LINE公式アカウントを友だち追加")
        print("   2. 公式アカウントにメッセージを送信")
        print("   3. WebhookイベントからUser IDを取得")
    
    print()
    print("=" * 60)
    
    # 設定状況のまとめ
    if LINE_CHANNEL_ACCESS_TOKEN and LINE_USER_ID:
        print("✅ すべての設定が完了しています！")
        print("   test_line_notify.py を実行してテストできます。")
        return True
    else:
        print("⚠️  設定が不完全です。上記の設定を完了してください。")
        return False


if __name__ == "__main__":
    check_line_config()

