"""
LINE通知機能の対話型テストスクリプト
トークンを直接入力してテストできます
"""

from core.line_notifier import LineNotifier


def test_line_notify_interactive():
    """LINE通知機能を対話型でテスト"""
    
    print("=" * 60)
    print("LINE通知機能 - 対話型テスト")
    print("=" * 60)
    print()
    
    # トークンの入力
    print("📝 LINE Messaging APIの設定情報を入力してください")
    print("（未取得の場合は、LINE Developers Consoleで取得してください）")
    print()
    
    channel_access_token = input("LINE_CHANNEL_ACCESS_TOKEN: ").strip()
    user_id = input("LINE_USER_ID: ").strip()
    
    if not channel_access_token:
        print("❌ Channel Access Tokenが入力されていません")
        return False
    
    if not user_id:
        print("❌ User IDが入力されていません")
        return False
    
    print()
    print(f"✅ Channel Access Tokenを受け取りました: {channel_access_token[:10]}...")
    print(f"✅ User IDを受け取りました: {user_id[:10]}...")
    print()
    
    # LineNotifierのインスタンスを作成
    notifier = LineNotifier(channel_access_token=channel_access_token, user_id=user_id)
    
    # テスト通知を送信
    print("📤 テスト通知を送信しています...")
    print()
    
    test_message = """🧪 Todo Listアプリからのテスト通知です

この通知が表示されれば、LINE連携は正常に動作しています！

✅ 接続テスト成功
📅 期日リマインダー機能も利用可能です"""
    
    success = notifier.send_notification(test_message)
    
    print()
    if success:
        print("=" * 60)
        print("✅ テスト通知の送信に成功しました！")
        print("=" * 60)
        print()
        print("📱 LINEアプリで通知を確認してください。")
        print()
        print("💡 ヒント:")
        print("   - 通知が届かない場合は、Channel Access TokenとUser IDが正しいか確認してください")
        print("   - Channel Access Tokenは LINE Developers Console で確認できます")
        print("   - User IDは、LINE公式アカウントにメッセージを送信した際のWebhookで取得できます")
        print()
    else:
        print("=" * 60)
        print("❌ テスト通知の送信に失敗しました")
        print("=" * 60)
        print()
        print("🔍 確認事項:")
        print("   1. トークンが正しく入力されているか")
        print("   2. トークンが有効期限内か（再発行が必要な場合があります）")
        print("   3. インターネット接続が正常か")
        print()
    
    # リマインダー機能のテスト（オプション）
    print("📋 リマインダー機能もテストしますか？ (y/n): ", end="")
    test_reminder = input().strip().lower()
    
    if test_reminder == 'y':
        print()
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
    try:
        test_line_notify_interactive()
    except KeyboardInterrupt:
        print("\n\nテストが中断されました")
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()

