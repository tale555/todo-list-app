"""
スプレッドシートIDの確認スクリプト
"""

import sys
import os
import re

# プロジェクトルートをパスに追加
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from configs.config import SPREADSHEET_ID, SHEET_NAME


def extract_spreadsheet_id(spreadsheet_id_or_url: str) -> str:
    """
    スプレッドシートIDまたはURLからIDを抽出
    
    Args:
        spreadsheet_id_or_url (str): スプレッドシートIDまたはURL
        
    Returns:
        str: 抽出されたスプレッドシートID
    """
    if not spreadsheet_id_or_url:
        return ''
    
    # URL形式の場合、IDを抽出
    url_pattern = r'/spreadsheets/d/([a-zA-Z0-9-_]+)'
    match = re.search(url_pattern, spreadsheet_id_or_url)
    if match:
        return match.group(1)
    
    # 既にID形式の場合はそのまま返す
    return spreadsheet_id_or_url.strip()


def check_spreadsheet_id():
    """スプレッドシートIDの確認"""
    print("=" * 60)
    print("スプレッドシートIDの確認")
    print("=" * 60)
    
    print(f"\n1. 現在の設定:")
    print(f"   スプレッドシートID: {SPREADSHEET_ID if SPREADSHEET_ID else '(未設定)'}")
    print(f"   シート名: {SHEET_NAME}")
    
    if not SPREADSHEET_ID:
        print("\n❌ スプレッドシートIDが設定されていません")
        print("\n💡 解決方法:")
        print("   .envファイルにSPREADSHEET_IDを設定してください")
        print("   例: SPREADSHEET_ID=1hs3erHyqAyP1dC-CwgjL_4b-rEefVoJfoK_26e3A6EE")
        return False
    
    # IDの形式を確認
    print(f"\n2. スプレッドシートIDの形式確認:")
    if 'http' in SPREADSHEET_ID or 'docs.google.com' in SPREADSHEET_ID:
        print(f"   ⚠️  完全なURLが設定されています")
        extracted_id = extract_spreadsheet_id(SPREADSHEET_ID)
        print(f"   ✅ 抽出されたID: {extracted_id}")
        print(f"\n   💡 推奨: .envファイルでIDのみを設定してください")
        print(f"   SPREADSHEET_ID={extracted_id}")
    else:
        print(f"   ✅ ID形式が正しいです")
    
    # IDの長さを確認（通常は44文字程度）
    if len(SPREADSHEET_ID) < 20:
        print(f"   ⚠️  IDが短すぎる可能性があります（通常は20文字以上）")
    elif len(SPREADSHEET_ID) > 100:
        print(f"   ⚠️  IDが長すぎる可能性があります（URLが設定されている可能性があります）")
    else:
        print(f"   ✅ IDの長さが適切です（{len(SPREADSHEET_ID)}文字）")
    
    print(f"\n" + "=" * 60)
    print("✅ 確認完了")
    print("=" * 60)
    
    return True


if __name__ == "__main__":
    success = check_spreadsheet_id()
    sys.exit(0 if success else 1)

