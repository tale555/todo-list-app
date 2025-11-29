"""
LINE Messaging APIを使用して通知を送信するモジュール
"""

import os
import requests
import json
from typing import Optional, List
from datetime import datetime, timedelta
from core.todo_manager import TodoManager, TodoItem


class LineNotifier:
    """LINE Messaging APIを使用して通知を送信するクラス"""
    
    MESSAGING_API_URL = "https://api.line.me/v2/bot/message/push"
    
    def __init__(self, channel_access_token: Optional[str] = None, user_id: Optional[str] = None):
        """
        初期化
        
        Args:
            channel_access_token (str, optional): LINE Messaging APIのチャネルアクセストークン
                                                  未指定の場合は環境変数から読み込む
            user_id (str, optional): メッセージを送信するユーザーID
                                   未指定の場合は環境変数から読み込む
        """
        self.channel_access_token = channel_access_token or os.getenv('LINE_CHANNEL_ACCESS_TOKEN', '')
        self.user_id = user_id or os.getenv('LINE_USER_ID', '')
    
    def send_notification(self, message: str) -> bool:
        """
        LINE通知を送信（Push Message APIを使用）
        
        Args:
            message (str): 送信するメッセージ
            
        Returns:
            bool: 送信に成功した場合はTrue
        """
        if not self.channel_access_token:
            print("⚠️  LINE Channel Access Tokenが設定されていません")
            return False
        
        if not self.user_id:
            print("⚠️  LINE User IDが設定されていません")
            return False
        
        headers = {
            "Authorization": f"Bearer {self.channel_access_token}",
            "Content-Type": "application/json"
        }
        
        # LINE Messaging APIの形式に合わせてメッセージを分割（最大1000文字）
        messages = []
        if len(message) <= 1000:
            messages.append({
                "type": "text",
                "text": message
            })
        else:
            # 長いメッセージは分割
            chunks = [message[i:i+1000] for i in range(0, len(message), 1000)]
            for chunk in chunks:
                messages.append({
                    "type": "text",
                    "text": chunk
                })
        
        # User IDを文字列に変換（数値の場合があるため）
        user_id_str = str(self.user_id).strip()
        
        data = {
            "to": user_id_str,
            "messages": messages
        }
        
        try:
            # デバッグ用: リクエスト内容をログ出力（トークンは一部のみ表示）
            print(f"   デバッグ: User ID = {user_id_str[:30]}...")
            print(f"   デバッグ: メッセージ数 = {len(messages)}")
            
            response = requests.post(self.MESSAGING_API_URL, headers=headers, json=data)
            if response.status_code == 200:
                print(f"✅ LINE通知を送信しました: {message[:50]}...")
                return True
            else:
                error_text = response.text
                try:
                    error_json = response.json()
                    error_message = error_json.get('message', error_text)
                    error_details = error_json.get('details', [])
                    if error_details:
                        details_text = "\n".join([f"      - {detail.get('message', str(detail))}" for detail in error_details])
                        error_message = f"{error_message}\n   詳細:\n{details_text}"
                except:
                    error_message = error_text
                print(f"⚠️  LINE通知の送信に失敗しました: {response.status_code}")
                print(f"   エラー詳細: {error_message}")
                print(f"   送信先User ID: {user_id_str[:20]}...")
                print(f"   レスポンス全文: {error_text}")
                return False
        except Exception as e:
            print(f"⚠️  LINE通知の送信中にエラーが発生しました: {e}")
            return False
    
    def check_and_send_reminders(self) -> int:
        """
        期日が近いTodoをチェックして通知を送信
        
        Returns:
            int: 送信した通知の数
        """
        if not self.channel_access_token or not self.user_id:
            return 0
        
        manager = TodoManager()
        todos = manager.get_all_todos()
        
        today = datetime.now().date()
        notifications_sent = 0
        
        # 通知対象のTodoを収集
        todos_to_notify = {
            '3days': [],
            '1day': [],
            'today': []
        }
        
        for todo in todos:
            # 完了済みはスキップ
            if todo.is_completed:
                continue
            
            # LINE通知が無効な場合はスキップ
            if not getattr(todo, 'enable_line_notification', True):
                continue
            
            try:
                due_date = datetime.strptime(todo.due_date, '%Y-%m-%d').date()
                days_until_due = (due_date - today).days
                
                if days_until_due == 3:
                    todos_to_notify['3days'].append(todo)
                elif days_until_due == 1:
                    todos_to_notify['1day'].append(todo)
                elif days_until_due == 0:
                    todos_to_notify['today'].append(todo)
            except (ValueError, TypeError):
                continue
        
        # 通知を送信
        if todos_to_notify['3days']:
            message = self._create_message(todos_to_notify['3days'], "3日前")
            if self.send_notification(message):
                notifications_sent += 1
        
        if todos_to_notify['1day']:
            message = self._create_message(todos_to_notify['1day'], "前日")
            if self.send_notification(message):
                notifications_sent += 1
        
        if todos_to_notify['today']:
            message = self._create_message(todos_to_notify['today'], "当日")
            if self.send_notification(message):
                notifications_sent += 1
        
        return notifications_sent
    
    def _create_message(self, todos: List[TodoItem], deadline_label: str) -> str:
        """
        通知メッセージを作成
        
        Args:
            todos (List[TodoItem]): 通知対象のTodoリスト
            deadline_label (str): 期日のラベル（例: "3日後"、"明日"、"本日期限"）
            
        Returns:
            str: 通知メッセージ
        """
        message = f"📋 Todoリマインダー\n\n"
        message += f"【{deadline_label}】のTodoが{len(todos)}件あります\n\n"
        
        for i, todo in enumerate(todos, 1):
            message += f"{i}. {todo.title}\n"
            if todo.category:
                message += f"   カテゴリ: {todo.category}\n"
            message += f"   期日: {todo.due_date}\n"
            if todo.content:
                message += f"   {todo.content[:50]}{'...' if len(todo.content) > 50 else ''}\n"
            message += "\n"
        
        return message

