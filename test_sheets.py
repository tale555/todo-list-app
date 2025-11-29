"""
Google Sheets API連携のテストスクリプト
動作確認用
"""

import sys
import os

# プロジェクトルートをパスに追加
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from core.sheets_manager import SheetsManager


def test_sheets_connection():
    """Google Sheets API接続のテスト"""
    print("=" * 50)
    print("Google Sheets API 接続テスト")
    print("=" * 50)
    
    try:
        # 認証ファイルのパスを表示
        from configs.config import GOOGLE_CREDENTIALS_PATH
        print(f"\n認証ファイルのパス: {GOOGLE_CREDENTIALS_PATH}")
        
        # SheetsManager インスタンスを作成
        print("\n1. SheetsManagerを初期化中...")
        manager = SheetsManager()
        print("   ✅ 初期化成功")
        
        # スプレッドシート情報を取得
        print("\n2. スプレッドシート情報を取得中...")
        info = manager.get_spreadsheet_info()
        print(f"   ✅ スプレッドシート名: {info['title']}")
        print(f"   ✅ シート一覧: {[s['title'] for s in info['sheets']]}")
        
        # データを読み取り（テスト）
        print("\n3. データを読み取り中...")
        data = manager.read_data('A1:Z10')
        print(f"   ✅ {len(data)}行のデータを読み取りました")
        
        if data:
            print("\n   読み取ったデータ（最初の5行）:")
            for i, row in enumerate(data[:5], 1):
                print(f"   行{i}: {row}")
        else:
            print("   ⚠️  データがありません（空のスプレッドシートです）")
        
        print("\n" + "=" * 50)
        print("✅ すべてのテストが成功しました！")
        print("=" * 50)
        
    except FileNotFoundError as e:
        print(f"\n❌ エラー: {e}")
        print("\n💡 解決方法:")
        print("1. USER_SETUP_GUIDE.mdを参照してGoogle Sheets APIの設定を行ってください")
        print("2. .envファイルに認証ファイルのパスを設定してください")
        print("   GOOGLE_CREDENTIALS_PATH=configs/credentials.json")
        return False
        
    except ValueError as e:
        print(f"\n❌ エラー: {e}")
        print("\n💡 解決方法:")
        print(".envファイルにSPREADSHEET_IDを設定してください")
        print("   SPREADSHEET_ID=your_spreadsheet_id_here")
        return False
        
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    
    return True


if __name__ == "__main__":
    success = test_sheets_connection()
    sys.exit(0 if success else 1)

