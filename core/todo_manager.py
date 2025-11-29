"""
Todo管理ロジック
Google Sheetsを使用してTodoアイテムを管理
"""

import uuid
from datetime import datetime
from typing import List, Dict, Optional, Any
from core.sheets_manager import SheetsManager


class TodoItem:
    """Todoアイテムのデータモデル"""
    
    def __init__(self, todo_id: str, title: str, content: str, due_date: str, created_at: Optional[str] = None, order: Optional[int] = None, is_completed: Optional[bool] = None, category: Optional[str] = None, enable_line_notification: Optional[bool] = None):
        """
        Todoアイテムを初期化
        
        Args:
            todo_id (str): Todoの一意ID
            title (str): タイトル
            content (str): 内容
            due_date (str): 期日（YYYY-MM-DD形式）
            created_at (str, optional): 作成日時（YYYY-MM-DD HH:MM:SS形式）
            order (int, optional): 表示順序
            is_completed (bool, optional): 完了状態（デフォルト: False）
            category (str, optional): カテゴリ（デフォルト: ''）
            enable_line_notification (bool, optional): LINE通知を有効にするか（デフォルト: True）
        """
        self.id = todo_id
        self.title = title
        self.content = content
        self.due_date = due_date
        self.created_at = created_at or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.order = order if order is not None else 0
        self.is_completed = is_completed if is_completed is not None else False
        self.category = category if category else ''
        self.enable_line_notification = enable_line_notification if enable_line_notification is not None else True
    
    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換"""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'due_date': self.due_date,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TodoItem':
        """辞書からTodoItemを作成"""
        return cls(
            todo_id=data.get('id', ''),
            title=data.get('title', ''),
            content=data.get('content', ''),
            due_date=data.get('due_date', ''),
            created_at=data.get('created_at', '')
        )
    
    @classmethod
    def from_row(cls, row: List[str]) -> Optional['TodoItem']:
        """スプレッドシートの行からTodoItemを作成"""
        if len(row) < 4:
            return None
        
        # 順序を取得（F列、存在しない場合は0）
        order = 0
        if len(row) > 5 and row[5]:
            try:
                order = int(row[5])
            except (ValueError, TypeError):
                order = 0
        
        # 完了状態を取得（G列、存在しない場合はFalse）
        is_completed = False
        if len(row) > 6 and row[6]:
            is_completed = str(row[6]).lower() in ('true', '1', 'yes', '完了')
        
        # カテゴリを取得（H列、存在しない場合は空文字）
        category = ''
        if len(row) > 7 and row[7]:
            category = str(row[7]).strip()
        
        # LINE通知フラグを取得（I列、存在しない場合はTrue）
        enable_line_notification = True
        if len(row) > 8 and row[8]:
            enable_line_notification = str(row[8]).lower() in ('true', '1', 'yes', '有効')
        
        return cls(
            todo_id=row[0] if row[0] else str(uuid.uuid4()),
            title=row[1] if len(row) > 1 else '',
            content=row[2] if len(row) > 2 else '',
            due_date=row[3] if len(row) > 3 else '',
            created_at=row[4] if len(row) > 4 else None,
            order=order,
            is_completed=is_completed,
            category=category,
            enable_line_notification=enable_line_notification
        )
    
    def to_row(self) -> List[str]:
        """スプレッドシートの行形式に変換"""
        return [
            self.id,
            self.title,
            self.content,
            self.due_date,
            self.created_at,
            str(self.order),
            'true' if self.is_completed else 'false',
            self.category,
            'true' if self.enable_line_notification else 'false'
        ]


class TodoManager:
    """Todo管理クラス"""
    
    # スプレッドシートのヘッダー行
    HEADER_ROW = ['ID', 'タイトル', '内容', '期日', '作成日時', '順序', '完了', 'カテゴリ', 'LINE通知']
    
    def __init__(self, sheets_manager: Optional[SheetsManager] = None):
        """
        TodoManagerを初期化
        
        Args:
            sheets_manager (SheetsManager, optional): SheetsManagerインスタンス
                                                      未指定の場合は新規作成
        """
        self.sheets_manager = sheets_manager or SheetsManager()
        self._initialize_sheet()
    
    def _initialize_sheet(self):
        """スプレッドシートを初期化（ヘッダー行を設定）"""
        try:
            # 既存のデータを読み取り
            existing_data = self.sheets_manager.read_data('A1:I1')
            
            # ヘッダー行が存在しない、または異なる場合は設定
            if not existing_data or existing_data[0] != self.HEADER_ROW:
                self.sheets_manager.write_data('A1:I1', [self.HEADER_ROW])
                print("✅ スプレッドシートを初期化しました（ヘッダー行を設定）")
        except Exception as e:
            # エラーが発生した場合（データが存在しない等）、ヘッダー行を設定
            try:
                self.sheets_manager.write_data('A1:I1', [self.HEADER_ROW])
                print("✅ スプレッドシートを初期化しました（ヘッダー行を設定）")
            except Exception as init_error:
                print(f"⚠️  スプレッドシートの初期化中にエラーが発生しました: {init_error}")
    
    def create_todo(self, title: str, content: str, due_date: str, category: Optional[str] = None, enable_line_notification: Optional[bool] = True) -> TodoItem:
        """
        新しいTodoを作成
        
        Args:
            title (str): タイトル
            content (str): 内容
            due_date (str): 期日（YYYY-MM-DD形式）
            category (str, optional): カテゴリ
            enable_line_notification (bool, optional): LINE通知を有効にするか（デフォルト: True）
            
        Returns:
            TodoItem: 作成されたTodoアイテム
            
        Raises:
            ValueError: バリデーションエラー
        """
        # バリデーション
        if not title or not title.strip():
            raise ValueError("タイトルは必須です")
        # 内容は任意（空でもOK）
        if not due_date or not due_date.strip():
            raise ValueError("期日は必須です")
        
        # 期日の形式を確認（簡易チェック）
        try:
            datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("期日はYYYY-MM-DD形式で入力してください（例: 2024-12-31）")
        
        # 新しいTodoアイテムを作成
        todo_id = str(uuid.uuid4())
        
        # 既存のTodoの最大順序を取得して、その次に設定
        existing_todos = self.get_all_todos()
        max_order = max([t.order for t in existing_todos], default=0) if existing_todos else 0
        
        # 内容が空の場合は空文字列を設定
        content_value = content.strip() if content else ''
        
        todo = TodoItem(
            todo_id=todo_id,
            title=title.strip(),
            content=content_value,
            due_date=due_date.strip(),
            order=max_order + 1,
            category=category.strip() if category else '',
            enable_line_notification=enable_line_notification if enable_line_notification is not None else True
        )
        
        # スプレッドシートに追加
        self.sheets_manager.append_data('A:I', [todo.to_row()])
        
        print(f"✅ Todoを作成しました: {todo.title} (ID: {todo.id})")
        return todo
    
    def get_all_todos(self) -> List[TodoItem]:
        """
        すべてのTodoを取得（順序でソート）
        
        Returns:
            List[TodoItem]: Todoアイテムのリスト（順序でソート済み）
        """
        try:
            # ヘッダー行を除いてデータを読み取り
            data = self.sheets_manager.read_data('A2:I1000')  # 最大1000件まで（I列まで）
            
            todos = []
            for row in data:
                todo = TodoItem.from_row(row)
                if todo:
                    todos.append(todo)
            
            # 順序でソート（順序が同じ場合は作成日時でソート）
            # 順序が0の場合は、作成日時でソート（既存データの互換性のため）
            todos.sort(key=lambda x: (x.order if x.order > 0 else 999999, x.created_at))
            
            print(f"✅ {len(todos)}件のTodoを取得しました")
            return todos
            
        except Exception as e:
            print(f"⚠️  Todoの取得中にエラーが発生しました: {e}")
            return []
    
    def get_todo_by_id(self, todo_id: str) -> Optional[TodoItem]:
        """
        IDでTodoを取得
        
        Args:
            todo_id (str): TodoのID
            
        Returns:
            Optional[TodoItem]: 見つかったTodoアイテム、見つからない場合はNone
        """
        todos = self.get_all_todos()
        for todo in todos:
            if todo.id == todo_id:
                return todo
        return None
    
    def update_todo(self, todo_id: str, title: Optional[str] = None, 
                   content: Optional[str] = None, due_date: Optional[str] = None, category: Optional[str] = None, enable_line_notification: Optional[bool] = None) -> Optional[TodoItem]:
        """
        Todoを更新
        
        Args:
            todo_id (str): TodoのID
            title (str, optional): 新しいタイトル
            content (str, optional): 新しい内容
            due_date (str, optional): 新しい期日（YYYY-MM-DD形式）
            category (str, optional): カテゴリ
            enable_line_notification (bool, optional): LINE通知を有効にするか
            
        Returns:
            Optional[TodoItem]: 更新されたTodoアイテム、見つからない場合はNone
            
        Raises:
            ValueError: バリデーションエラー
        """
        # 既存のTodoを取得
        todo = self.get_todo_by_id(todo_id)
        if not todo:
            return None
        
        # 更新する値があれば適用
        if title is not None:
            if not title.strip():
                raise ValueError("タイトルは空にできません")
            todo.title = title.strip()
        
        if content is not None:
            # 内容は任意（空でもOK）
            todo.content = content.strip() if content else ''
        
        if due_date is not None:
            if not due_date.strip():
                raise ValueError("期日は空にできません")
            # 期日の形式を確認
            try:
                datetime.strptime(due_date, '%Y-%m-%d')
            except ValueError:
                raise ValueError("期日はYYYY-MM-DD形式で入力してください（例: 2024-12-31）")
            todo.due_date = due_date.strip()
        
        if category is not None:
            todo.category = category.strip() if category else ''
        
        if enable_line_notification is not None:
            todo.enable_line_notification = enable_line_notification
        
        # スプレッドシートを更新
        todos = self.get_all_todos()
        rows = [self.HEADER_ROW]  # ヘッダー行
        
        # 更新対象のTodoを置き換え
        updated = False
        for t in todos:
            if t.id == todo_id:
                rows.append(todo.to_row())
                updated = True
            else:
                rows.append(t.to_row())
        
        # 更新対象が見つからなかった場合（念のため）
        if not updated:
            rows.append(todo.to_row())
        
        # 既存のデータをクリアしてから書き込み（重複を防ぐ）
        # まず、既存のデータ範囲をクリア
        try:
            # 十分な範囲をクリア（最大1000行まで、H列まで）
            self.sheets_manager.clear_data('A2:I1000')
        except:
            pass  # クリアに失敗しても続行
        
        # すべてのデータを書き込み
        self.sheets_manager.write_data('A1', rows)
        
        print(f"✅ Todoを更新しました: {todo.title} (ID: {todo.id})")
        return todo
    
    def delete_todo(self, todo_id: str) -> bool:
        """
        Todoを削除
        
        Args:
            todo_id (str): TodoのID
            
        Returns:
            bool: 削除に成功した場合はTrue、見つからない場合はFalse
        """
        todos = self.get_all_todos()
        
        # 削除対象のTodoが存在するか確認
        if not any(t.id == todo_id for t in todos):
            print(f"⚠️  Todoが見つかりませんでした (ID: {todo_id})")
            return False
        
        # 削除対象を除いたリストを作成
        remaining_todos = [t for t in todos if t.id != todo_id]
        
        # 既存のデータをクリアしてから書き込み（重複を防ぐ）
        try:
            # 十分な範囲をクリア（最大1000行まで、H列まで）
            self.sheets_manager.clear_data('A2:I1000')
        except Exception as e:
            print(f"⚠️  データクリア中にエラー: {e}")
            pass  # クリアに失敗しても続行
        
        # スプレッドシートを更新
        rows = [self.HEADER_ROW]  # ヘッダー行
        for todo in remaining_todos:
            rows.append(todo.to_row())
        
        # すべてのデータを書き込み
        if rows:
            self.sheets_manager.write_data('A1', rows)
        else:
            # Todoが0件の場合はヘッダー行のみ
            self.sheets_manager.write_data('A1', [self.HEADER_ROW])
        
        print(f"✅ Todoを削除しました (ID: {todo_id})")
        return True
    
    def update_todo_order(self, todo_orders: List[Dict[str, int]]) -> bool:
        """
        Todoの順序を一括更新
        
        Args:
            todo_orders (List[Dict[str, int]]): [{'id': 'todo_id', 'order': 1}, ...] の形式
            
        Returns:
            bool: 更新に成功した場合はTrue
        """
        try:
            todos = self.get_all_todos()
            
            # 順序のマップを作成
            order_map = {item['id']: item['order'] for item in todo_orders}
            
            # 各Todoの順序を更新
            for todo in todos:
                if todo.id in order_map:
                    todo.order = order_map[todo.id]
            
            # 既存のデータをクリアしてから書き込み
            try:
                self.sheets_manager.clear_data('A2:I1000')
            except:
                pass
            
            # 順序でソート
            todos.sort(key=lambda x: (x.order, x.created_at))
            
            # スプレッドシートを更新
            rows = [self.HEADER_ROW]  # ヘッダー行
            for todo in todos:
                rows.append(todo.to_row())
            
            # すべてのデータを書き込み
            self.sheets_manager.write_data('A1', rows)
            
            print(f"✅ Todoの順序を更新しました ({len(todo_orders)}件)")
            return True
            
        except Exception as e:
            print(f"⚠️  Todoの順序更新中にエラーが発生しました: {e}")
            return False
    
    def toggle_todo_completion(self, todo_id: str) -> Optional[TodoItem]:
        """
        Todoの完了状態を切り替え
        
        Args:
            todo_id (str): TodoのID
            
        Returns:
            Optional[TodoItem]: 更新されたTodoアイテム、見つからない場合はNone
        """
        todo = self.get_todo_by_id(todo_id)
        if not todo:
            return None
        
        # 完了状態を切り替え
        todo.is_completed = not todo.is_completed
        
        # スプレッドシートを更新
        todos = self.get_all_todos()
        rows = [self.HEADER_ROW]  # ヘッダー行
        
        # 更新対象のTodoを置き換え
        updated = False
        for t in todos:
            if t.id == todo_id:
                rows.append(todo.to_row())
                updated = True
            else:
                rows.append(t.to_row())
        
        # 更新対象が見つからなかった場合（念のため）
        if not updated:
            rows.append(todo.to_row())
        
        # 既存のデータをクリアしてから書き込み
        try:
            self.sheets_manager.clear_data('A2:I1000')
        except:
            pass
        
        # すべてのデータを書き込み
        self.sheets_manager.write_data('A1', rows)
        
        print(f"✅ Todoの完了状態を更新しました: {todo.title} (完了: {todo.is_completed})")
        return todo
    
    def get_categories(self) -> List[str]:
        """
        すべてのカテゴリを取得（重複なし）
        
        Returns:
            List[str]: カテゴリのリスト
        """
        todos = self.get_all_todos()
        categories = set()
        for todo in todos:
            if todo.category:
                categories.add(todo.category)
        return sorted(list(categories))


def main():
    """テスト用のメイン関数"""
    try:
        manager = TodoManager()
        
        # テスト用のTodoを作成
        print("\n=== Todo作成テスト ===")
        todo1 = manager.create_todo(
            title="テストTodo 1",
            content="これはテスト用のTodoです",
            due_date="2024-12-31"
        )
        print(f"作成したTodo: {todo1.to_dict()}")
        
        # すべてのTodoを取得
        print("\n=== Todo取得テスト ===")
        todos = manager.get_all_todos()
        print(f"取得したTodo数: {len(todos)}")
        for todo in todos:
            print(f"  - {todo.title} (期日: {todo.due_date})")
        
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

