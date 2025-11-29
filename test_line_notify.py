"""
LINE Messaging API通知機能のテストスクリプト
"""

import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

from core.line_notifier import LineNotifier
from configs.config import LINE_CHANNEL_ACCESS_TOKEN, LINE_USER_ID


def test_line_notify():
    """LINE通知機能をテスト"""
    
    print("=" * 60)
    print("LINE Messaging API通知機能テスト")
    print("=" * 60)
    
    # トークンの確認
    if not LINE_CHANNEL_ACCESS_TOKEN:
        print("❌ エラー: LINE_CHANNEL_ACCESS_TOKENが設定されていません")
        print("\n.envファイルに以下を追加してください:")
        print("LINE_CHANNEL_ACCESS_TOKEN=your_channel_access_token_here")
        return False
    
    if not LINE_USER_ID:
        print("❌ エラー: LINE_USER_IDが設定されていません")
        print("\n.envファイルに以下を追加してください:")
        print("LINE_USER_ID=your_user_id_here")
        return False
    
    print(f"✅ Channel Access Tokenが設定されています: {LINE_CHANNEL_ACCESS_TOKEN[:10]}...")
    print(f"✅ User IDが設定されています: {LINE_USER_ID[:10]}...")
    print()
    
    # LineNotifierのインスタンスを作成
    notifier = LineNotifier()
    
    # テスト通知を送信
    print("📤 テスト通知を送信しています...")
    test_message = "🧪 Todo Listアプリからのテスト通知です\n\nこの通知が表示されれば、LINE Messaging API連携は正常に動作しています！"
    
    success = notifier.send_notification(test_message)
    
    if success:
        print("✅ テスト通知の送信に成功しました！")
        print("LINEアプリで通知を確認してください。")
    else:
        print("❌ テスト通知の送信に失敗しました")
        print("以下を確認してください:")
        print("  - Channel Access Tokenが正しいか")
        print("  - User IDが正しいか")
        print("  - LINE公式アカウントが友だち追加されているか")
    
    print()
    
    # リマインダー機能のテスト
    print("📋 リマインダー機能をテストしています...")
    count = notifier.check_and_send_reminders()
    
    if count > 0:
        print(f"✅ {count}件のリマインダー通知を送信しました")
    else:
        print("ℹ️  通知対象のTodoはありませんでした")
        print("（期日が3日前・前日・当日の未完了Todoがある場合に通知が送信されます）")
    
    print()
    print("=" * 60)
    print("テスト完了")
    print("=" * 60)
    
    return success


if __name__ == "__main__":
    test_line_notify()

