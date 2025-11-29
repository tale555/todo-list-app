"""
認証ファイルのパスと内容を確認するスクリプト
"""

import os
import json
import sys

# プロジェクトルートをパスに追加
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from configs.config import GOOGLE_CREDENTIALS_PATH


def check_credentials():
    """認証ファイルのパスと内容を確認"""
    print("=" * 60)
    print("認証ファイルの確認")
    print("=" * 60)
    
    # 設定から読み込んだパス
    print(f"\n1. 設定ファイル（config.py）から読み込んだパス:")
    print(f"   {GOOGLE_CREDENTIALS_PATH}")
    
    # プロジェクトルートからの相対パスを絶対パスに変換
    if not os.path.isabs(GOOGLE_CREDENTIALS_PATH):
        abs_path = os.path.join(project_root, GOOGLE_CREDENTIALS_PATH)
    else:
        abs_path = GOOGLE_CREDENTIALS_PATH
    
    print(f"\n2. 絶対パス:")
    print(f"   {abs_path}")
    
    # ファイルの存在確認
    print(f"\n3. ファイルの存在確認:")
    if os.path.exists(abs_path):
        print(f"   ✅ ファイルが存在します")
    else:
        print(f"   ❌ ファイルが見つかりません")
        print(f"\n💡 解決方法:")
        print(f"   1. .envファイルでGOOGLE_CREDENTIALS_PATHを正しいパスに設定してください")
        print(f"   2. または、認証ファイルを正しい場所に配置してください")
        return False
    
    # ファイルの内容確認
    print(f"\n4. ファイルの内容確認:")
    try:
        with open(abs_path, 'r', encoding='utf-8') as f:
            creds_data = json.load(f)
        
        # 必要なフィールドを確認
        required_fields = ['type', 'project_id', 'private_key_id', 'private_key', 'client_email', 'token_uri']
        print(f"   必要なフィールドの確認:")
        all_ok = True
        for field in required_fields:
            if field in creds_data:
                print(f"   ✅ {field}: 存在します")
            else:
                print(f"   ❌ {field}: 存在しません")
                all_ok = False
        
        if not all_ok:
            print(f"\n   ⚠️  必要なフィールドが不足しています")
            return False
        
        # タイプ確認
        if creds_data.get('type') == 'service_account':
            print(f"\n   ✅ タイプ: service_account（正しい）")
        else:
            print(f"\n   ❌ タイプ: {creds_data.get('type')}（service_accountである必要があります）")
            return False
        
        # プロジェクトIDとメールアドレスを表示
        print(f"\n5. 認証情報の詳細:")
        print(f"   プロジェクトID: {creds_data.get('project_id', 'N/A')}")
        print(f"   サービスアカウントメール: {creds_data.get('client_email', 'N/A')}")
        
        print(f"\n" + "=" * 60)
        print("✅ 認証ファイルは正しい形式です！")
        print("=" * 60)
        return True
        
    except json.JSONDecodeError as e:
        print(f"   ❌ JSON形式が正しくありません: {e}")
        return False
    except Exception as e:
        print(f"   ❌ エラー: {e}")
        return False


if __name__ == "__main__":
    success = check_credentials()
    sys.exit(0 if success else 1)

