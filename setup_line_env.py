"""
LINE API設定を対話型で設定するスクリプト
"""

import os
from pathlib import Path

def setup_line_env():
    """LINE API設定を対話型で設定"""
    
    print("=" * 60)
    print("LINE Messaging API設定")
    print("=" * 60)
    print()
    
    # .envファイルのパス
    env_path = Path(__file__).parent / '.env'
    
    # 既存の.envファイルを読み込む
    existing_vars = {}
    if env_path.exists():
        print(f"📄 既存の.envファイルが見つかりました: {env_path}")
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    existing_vars[key.strip()] = value.strip()
        
        if existing_vars:
            print("\n既存の設定:")
            for key, value in existing_vars.items():
                if 'TOKEN' in key or 'ID' in key:
                    print(f"  {key}: {value[:20]}...")
                else:
                    print(f"  {key}: {value}")
        print()
    
    # Channel Access Tokenの入力
    print("📝 LINE Messaging APIの設定情報を入力してください")
    print("（未入力の場合は既存の値を使用します）")
    print()
    
    channel_access_token = input(f"LINE_CHANNEL_ACCESS_TOKEN [{existing_vars.get('LINE_CHANNEL_ACCESS_TOKEN', '')[:20]}...]: ").strip()
    if not channel_access_token:
        channel_access_token = existing_vars.get('LINE_CHANNEL_ACCESS_TOKEN', '')
    
    user_id = input(f"LINE_USER_ID [{existing_vars.get('LINE_USER_ID', '')[:20]}...]: ").strip()
    if not user_id:
        user_id = existing_vars.get('LINE_USER_ID', '')
    
    print()
    
    # 既存の.envファイルを読み込む（LINE設定以外も保持）
    env_lines = []
    if env_path.exists():
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line_stripped = line.strip()
                # LINE設定の行はスキップ（後で追加する）
                if line_stripped.startswith('LINE_CHANNEL_ACCESS_TOKEN') or line_stripped.startswith('LINE_USER_ID'):
                    continue
                env_lines.append(line.rstrip('\n'))
    
    # LINE設定を追加
    if channel_access_token:
        env_lines.append(f"LINE_CHANNEL_ACCESS_TOKEN={channel_access_token}")
    if user_id:
        env_lines.append(f"LINE_USER_ID={user_id}")
    
    # .envファイルを書き込み
    with open(env_path, 'w', encoding='utf-8') as f:
        for line in env_lines:
            f.write(line + '\n')
    
    print("=" * 60)
    print("✅ .envファイルを更新しました！")
    print("=" * 60)
    print()
    print(f"📄 ファイルの場所: {env_path}")
    print()
    
    if channel_access_token:
        print(f"✅ LINE_CHANNEL_ACCESS_TOKEN: 設定済み ({channel_access_token[:20]}...)")
    else:
        print("⚠️  LINE_CHANNEL_ACCESS_TOKEN: 未設定")
    
    if user_id:
        print(f"✅ LINE_USER_ID: 設定済み ({user_id[:20]}...)")
    else:
        print("⚠️  LINE_USER_ID: 未設定")
        print()
        print("💡 User IDの取得方法:")
        print("   1. LINE公式アカウントを友だち追加")
        print("   2. Webhookを使用してUser IDを取得")
        print("   3. 詳細は LINE_SETUP_FROM_SCRATCH.md を参照")
    
    print()
    print("=" * 60)
    print("設定完了！")
    print("=" * 60)
    print()
    print("次のステップ:")
    if channel_access_token and user_id:
        print("  python test_line_notify.py  # テスト実行")
    elif channel_access_token:
        print("  1. User IDを取得してください")
        print("  2. python setup_line_env.py  # 再度実行してUser IDを設定")
    else:
        print("  1. Channel Access TokenとUser IDを取得してください")
        print("  2. python setup_line_env.py  # 再度実行して設定")


if __name__ == "__main__":
    try:
        setup_line_env()
    except KeyboardInterrupt:
        print("\n\n設定が中断されました")
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()

