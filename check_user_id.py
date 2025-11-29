"""
FlaskアプリのログからUser IDを確認するスクリプト
または、メッセージを送信してUser IDを取得する
"""

import os
from dotenv import load_dotenv

load_dotenv()

from configs.config import LINE_USER_ID

def check_user_id():
    """User IDの設定状況を確認"""
    
    print("=" * 60)
    print("LINE User ID確認")
    print("=" * 60)
    print()
    
    if LINE_USER_ID:
        print(f"✅ LINE_USER_IDが設定されています: {LINE_USER_ID}")
        print()
        print("このUser IDでテストできます:")
        print("  python test_line_notify.py")
    else:
        print("❌ LINE_USER_IDが設定されていません")
        print()
        print("💡 User IDを取得する方法:")
        print("   1. Flaskアプリのターミナルを確認してください")
        print("   2. 友だち追加後、以下のようなメッセージが表示されます:")
        print("      ✅ 友だち追加イベントを受信しました！")
        print("         User ID: U1234567890abcdefghijklmnopqrstuvw")
        print()
        print("   3. もし表示されない場合は、公式アカウントにメッセージを送信してください")
        print("      （例: 「テスト」と送信）")
        print()
        print("   4. それでも表示されない場合は、以下を確認してください:")
        print("      - Flaskアプリが起動しているか")
        print("      - ngrokが起動しているか")
        print("      - LINE Developers ConsoleでWebhook URLが正しく設定されているか")
        print("      - 「Webhookの利用」がONになっているか")
    
    print()
    print("=" * 60)


if __name__ == "__main__":
    check_user_id()

