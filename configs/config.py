"""
Todo List App - 設定ファイル
環境変数から設定を読み込む
"""

import os
import re
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()


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
    # 例: https://docs.google.com/spreadsheets/d/1A2B3C4D5E6F7G8H9I0J/edit
    url_pattern = r'/spreadsheets/d/([a-zA-Z0-9-_]+)'
    match = re.search(url_pattern, spreadsheet_id_or_url)
    if match:
        return match.group(1)
    
    # 既にID形式の場合はそのまま返す
    return spreadsheet_id_or_url.strip()


# Google Sheets API 設定
# 既存の認証ファイル（../configs/silent-life-473721-e2-bd839ba557ad.json）を使用可能
# または、configs/credentials.jsonに新しい認証ファイルを配置
GOOGLE_CREDENTIALS_PATH = os.getenv(
    'GOOGLE_CREDENTIALS_PATH',
    'configs/credentials.json'  # 既存ファイルを使用する場合は '../configs/silent-life-473721-e2-bd839ba557ad.json' に変更
)

# スプレッドシートID（URLから自動抽出）
_raw_spreadsheet_id = os.getenv('SPREADSHEET_ID', '')
SPREADSHEET_ID = extract_spreadsheet_id(_raw_spreadsheet_id)

# シート名
SHEET_NAME = os.getenv('SHEET_NAME', 'Sheet1')

# Flask設定
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# LINE Messaging API設定
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', '')
LINE_USER_ID = os.getenv('LINE_USER_ID', '')

