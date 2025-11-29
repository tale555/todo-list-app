"""
Google Sheets API を使用してスプレッドシートにデータを送信・読み取りするモジュール
Todo List App用にカスタマイズ
"""

import os
from typing import List, Dict, Any, Optional
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from configs.config import GOOGLE_CREDENTIALS_PATH, SPREADSHEET_ID, SHEET_NAME


class SheetsManager:
    """Google Sheets API を使用してスプレッドシートにデータを送信・読み取りするクラス"""
    
    def __init__(self, credentials_path: Optional[str] = None, 
                 spreadsheet_id: Optional[str] = None,
                 sheet_name: Optional[str] = None):
        """
        初期化
        
        Args:
            credentials_path (str, optional): サービスアカウントのJSON認証ファイルのパス
                                              未指定の場合はconfig.pyから読み込む
            spreadsheet_id (str, optional): スプレッドシートID
                                            未指定の場合はconfig.pyから読み込む
            sheet_name (str, optional): シート名
                                        未指定の場合はconfig.pyから読み込む
        """
        # 認証ファイルのパスを決定（相対パスを絶対パスに変換）
        if credentials_path:
            # 指定されたパスが相対パスの場合、プロジェクトルートからの相対パスとして扱う
            if os.path.isabs(credentials_path):
                self.credentials_path = credentials_path
            else:
                # core/sheets_manager.py から見て、プロジェクトルート（todo_list_app）は1階層上
                current_file_dir = os.path.dirname(os.path.abspath(__file__))
                project_root = os.path.dirname(current_file_dir)
                self.credentials_path = os.path.join(project_root, credentials_path)
        else:
            # プロジェクトルートからの相対パスを絶対パスに変換
            # core/sheets_manager.py から見て、プロジェクトルート（todo_list_app）は1階層上
            current_file_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(current_file_dir)
            credentials_rel_path = GOOGLE_CREDENTIALS_PATH
            
            # 既に絶対パスの場合はそのまま使用
            if os.path.isabs(credentials_rel_path):
                self.credentials_path = credentials_rel_path
            else:
                self.credentials_path = os.path.join(project_root, credentials_rel_path)
        
        self.spreadsheet_id = spreadsheet_id or SPREADSHEET_ID
        self.sheet_name = sheet_name or SHEET_NAME
        self.service = None
        self._authenticate()
    
    def _authenticate(self):
        """サービスアカウントで認証を行う"""
        import json
        
        try:
            # 認証ファイルの存在確認
            if not os.path.exists(self.credentials_path):
                raise FileNotFoundError(
                    f"認証ファイルが見つかりません: {self.credentials_path}\n"
                    f"USER_SETUP_GUIDE.mdを参照してGoogle Sheets APIの設定を行ってください。"
                )
            
            # 認証ファイルの形式を確認
            try:
                with open(self.credentials_path, 'r', encoding='utf-8') as f:
                    creds_data = json.load(f)
                
                # サービスアカウントのJSONファイルに必要なフィールドを確認
                required_fields = ['type', 'project_id', 'private_key_id', 'private_key', 'client_email', 'token_uri']
                missing_fields = [field for field in required_fields if field not in creds_data]
                
                if missing_fields:
                    raise ValueError(
                        f"認証ファイルの形式が正しくありません。\n"
                        f"不足しているフィールド: {', '.join(missing_fields)}\n"
                        f"このファイルはサービスアカウントのJSONファイルではない可能性があります。\n"
                        f"USER_SETUP_GUIDE.mdを参照して、正しいサービスアカウントのJSONファイルをダウンロードしてください。"
                    )
                
                # サービスアカウントタイプか確認
                if creds_data.get('type') != 'service_account':
                    raise ValueError(
                        f"認証ファイルのタイプが正しくありません。\n"
                        f"現在のタイプ: {creds_data.get('type')}\n"
                        f"期待されるタイプ: service_account\n"
                        f"OAuth2.0の認証ファイルではなく、サービスアカウントのJSONファイルを使用してください。"
                    )
                    
            except json.JSONDecodeError as e:
                raise ValueError(
                    f"認証ファイルが正しいJSON形式ではありません: {str(e)}\n"
                    f"ファイルが破損している可能性があります。"
                )
            
            # 認証情報を読み込み
            credentials = service_account.Credentials.from_service_account_file(
                self.credentials_path,
                scopes=['https://www.googleapis.com/auth/spreadsheets']
            )
            
            # Google Sheets API サービスを構築
            self.service = build('sheets', 'v4', credentials=credentials)
            print("✅ Google Sheets API認証が成功しました。")
            
        except FileNotFoundError as e:
            raise FileNotFoundError(str(e))
        except ValueError as e:
            raise ValueError(str(e))
        except Exception as e:
            error_msg = str(e)
            if 'MalformedError' in error_msg or 'missing fields' in error_msg:
                raise ValueError(
                    f"認証ファイルの形式が正しくありません。\n"
                    f"エラー詳細: {error_msg}\n\n"
                    f"💡 解決方法:\n"
                    f"1. Google Cloud ConsoleでサービスアカウントのJSONファイルを再ダウンロードしてください\n"
                    f"2. ファイルが正しいサービスアカウントのJSONファイルであることを確認してください\n"
                    f"3. OAuth2.0の認証ファイル（client_secrets.json等）ではなく、サービスアカウントのJSONファイルを使用してください\n"
                    f"4. USER_SETUP_GUIDE.mdを参照して設定を確認してください"
                )
            raise Exception(f"認証に失敗しました: {error_msg}")
    
    def get_spreadsheet_info(self) -> Dict[str, Any]:
        """
        スプレッドシートの情報を取得
        
        Returns:
            Dict[str, Any]: スプレッドシートの情報
        """
        if not self.spreadsheet_id:
            raise ValueError("スプレッドシートIDが設定されていません。.envファイルでSPREADSHEET_IDを設定してください。")
        
        try:
            sheet_metadata = self.service.spreadsheets().get(
                spreadsheetId=self.spreadsheet_id
            ).execute()
            
            return {
                'title': sheet_metadata.get('properties', {}).get('title'),
                'sheets': [
                    {
                        'title': sheet.get('properties', {}).get('title'),
                        'sheet_id': sheet.get('properties', {}).get('sheetId'),
                        'grid_properties': sheet.get('properties', {}).get('gridProperties', {})
                    }
                    for sheet in sheet_metadata.get('sheets', [])
                ]
            }
        except HttpError as e:
            raise Exception(f"スプレッドシート情報の取得に失敗しました: {str(e)}")
    
    def create_spreadsheet(self, title: str) -> str:
        """
        新しいスプレッドシートを作成
        
        Args:
            title (str): スプレッドシートのタイトル
            
        Returns:
            str: 作成されたスプレッドシートのID
        """
        try:
            spreadsheet_body = {
                'properties': {
                    'title': title
                }
            }
            
            spreadsheet = self.service.spreadsheets().create(
                body=spreadsheet_body,
                fields='spreadsheetId'
            ).execute()
            
            spreadsheet_id = spreadsheet.get('spreadsheetId')
            print(f"✅ スプレッドシートが作成されました: {title} (ID: {spreadsheet_id})")
            return spreadsheet_id
            
        except HttpError as e:
            raise Exception(f"スプレッドシートの作成に失敗しました: {str(e)}")
    
    def write_data(self, 
                   range_name: str, 
                   values: List[List[Any]], 
                   value_input_option: str = 'RAW') -> Dict[str, Any]:
        """
        スプレッドシートにデータを書き込み
        
        Args:
            range_name (str): 書き込む範囲 (例: 'A1:C3' または 'Sheet1!A1:C3')
            values (List[List[Any]]): 書き込むデータ（2次元配列）
            value_input_option (str): 値の入力形式 ('RAW' または 'USER_ENTERED')
            
        Returns:
            Dict[str, Any]: 更新結果
        """
        if not self.spreadsheet_id:
            raise ValueError("スプレッドシートIDが設定されていません。")
        
        try:
            # シート名が含まれていない場合は追加
            if '!' not in range_name:
                range_name = f"{self.sheet_name}!{range_name}"
            
            body = {
                'values': values
            }
            
            result = self.service.spreadsheets().values().update(
                spreadsheetId=self.spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body
            ).execute()
            
            updated_cells = result.get('updatedCells', 0)
            print(f"✅ {updated_cells}個のセルが更新されました。")
            
            return result
            
        except HttpError as e:
            raise Exception(f"データの書き込みに失敗しました: {str(e)}")
    
    def append_data(self, 
                    range_name: str, 
                    values: List[List[Any]], 
                    value_input_option: str = 'RAW') -> Dict[str, Any]:
        """
        スプレッドシートの末尾にデータを追加
        
        Args:
            range_name (str): 追加する範囲 (例: 'A:C' または 'Sheet1!A:C')
            values (List[List[Any]]): 追加するデータ（2次元配列）
            value_input_option (str): 値の入力形式 ('RAW' または 'USER_ENTERED')
            
        Returns:
            Dict[str, Any]: 追加結果
        """
        if not self.spreadsheet_id:
            raise ValueError("スプレッドシートIDが設定されていません。")
        
        try:
            # シート名が含まれていない場合は追加
            if '!' not in range_name:
                range_name = f"{self.sheet_name}!{range_name}"
            
            body = {
                'values': values
            }
            
            result = self.service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body
            ).execute()
            
            updated_cells = result.get('updates', {}).get('updatedCells', 0)
            print(f"✅ {updated_cells}個のセルが追加されました。")
            
            return result
            
        except HttpError as e:
            raise Exception(f"データの追加に失敗しました: {str(e)}")
    
    def read_data(self, range_name: str) -> List[List[Any]]:
        """
        スプレッドシートからデータを読み取り
        
        Args:
            range_name (str): 読み取る範囲 (例: 'A1:C10' または 'Sheet1!A1:C10')
            
        Returns:
            List[List[Any]]: 読み取ったデータ（2次元配列）
        """
        if not self.spreadsheet_id:
            raise ValueError("スプレッドシートIDが設定されていません。")
        
        try:
            # シート名が含まれていない場合は追加
            if '!' not in range_name:
                range_name = f"{self.sheet_name}!{range_name}"
            
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_name
            ).execute()
            
            values = result.get('values', [])
            print(f"✅ {len(values)}行のデータを読み取りました。")
            
            return values
            
        except HttpError as e:
            raise Exception(f"データの読み取りに失敗しました: {str(e)}")
    
    def clear_data(self, range_name: str) -> Dict[str, Any]:
        """
        スプレッドシートの指定範囲をクリア
        
        Args:
            range_name (str): クリアする範囲 (例: 'A1:C10' または 'Sheet1!A1:C10')
            
        Returns:
            Dict[str, Any]: クリア結果
        """
        if not self.spreadsheet_id:
            raise ValueError("スプレッドシートIDが設定されていません。")
        
        try:
            # シート名が含まれていない場合は追加
            if '!' not in range_name:
                range_name = f"{self.sheet_name}!{range_name}"
            
            result = self.service.spreadsheets().values().clear(
                spreadsheetId=self.spreadsheet_id,
                range=range_name
            ).execute()
            
            cleared_range = result.get('clearedRange', '')
            print(f"✅ 範囲 {cleared_range} がクリアされました。")
            
            return result
            
        except HttpError as e:
            raise Exception(f"データのクリアに失敗しました: {str(e)}")
    
    def update_cell(self, 
                    cell: str, 
                    value: Any, 
                    value_input_option: str = 'RAW') -> Dict[str, Any]:
        """
        特定のセルを更新
        
        Args:
            cell (str): セル位置 (例: 'A1' または 'Sheet1!A1')
            value (Any): 更新する値
            value_input_option (str): 値の入力形式 ('RAW' または 'USER_ENTERED')
            
        Returns:
            Dict[str, Any]: 更新結果
        """
        return self.write_data(cell, [[value]], value_input_option)
    
    def get_all_data(self) -> List[List[Any]]:
        """
        シート全体のデータを読み取り
        
        Returns:
            List[List[Any]]: 読み取ったデータ（2次元配列）
        """
        return self.read_data('A:Z')  # A列からZ列まで読み取り


def main():
    """テスト用のメイン関数"""
    try:
        # SheetsManager インスタンスを作成
        manager = SheetsManager()
        
        # スプレッドシート情報を取得
        info = manager.get_spreadsheet_info()
        print(f"スプレッドシート名: {info['title']}")
        print(f"シート一覧: {[s['title'] for s in info['sheets']]}")
        
        # データを読み取り（テスト）
        data = manager.read_data('A1:Z10')
        print(f"\n読み取ったデータ（最初の5行）:")
        for i, row in enumerate(data[:5], 1):
            print(f"行{i}: {row}")
            
    except FileNotFoundError as e:
        print(f"❌ エラー: {e}")
        print("\n💡 解決方法:")
        print("1. USER_SETUP_GUIDE.mdを参照してGoogle Sheets APIの設定を行ってください")
        print("2. .envファイルに認証ファイルのパスとスプレッドシートIDを設定してください")
    except ValueError as e:
        print(f"❌ エラー: {e}")
        print("\n💡 解決方法:")
        print(".envファイルにSPREADSHEET_IDを設定してください")
    except Exception as e:
        print(f"❌ エラーが発生しました: {str(e)}")


if __name__ == "__main__":
    main()

