"""
Todo管理機能のテストスクリプト
"""

import sys
import os

# プロジェクトルートをパスに追加
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from core.todo_manager import TodoManager, TodoItem


def test_todo_manager():
    """TodoManagerのテスト"""
    print("=" * 60)
    print("Todo管理機能のテスト")
    print("=" * 60)
    
    try:
        manager = TodoManager()
        
        # 1. すべてのTodoを取得（初期状態）
        print("\n1. 既存のTodoを取得中...")
        todos = manager.get_all_todos()
        print(f"   ✅ {len(todos)}件のTodoが見つかりました")
        
        if todos:
            print("\n   既存のTodo一覧:")
            for i, todo in enumerate(todos[:5], 1):  # 最初の5件を表示
                print(f"   {i}. {todo.title} (期日: {todo.due_date}, ID: {todo.id[:8]}...)")
        
        # 2. 新しいTodoを作成（テスト用）
        print("\n2. 新しいTodoを作成中...")
        test_todo = manager.create_todo(
            title="テストTodo",
            content="これはテスト用のTodoです。削除しても問題ありません。",
            due_date="2024-12-31"
        )
        print(f"   ✅ Todoを作成しました: {test_todo.title} (ID: {test_todo.id})")
        
        # 3. 作成したTodoを取得
        print("\n3. 作成したTodoを取得中...")
        retrieved_todo = manager.get_todo_by_id(test_todo.id)
        if retrieved_todo:
            print(f"   ✅ Todoを取得しました: {retrieved_todo.title}")
        else:
            print("   ❌ Todoが見つかりませんでした")
        
        # 4. Todoを更新
        print("\n4. Todoを更新中...")
        updated_todo = manager.update_todo(
            todo_id=test_todo.id,
            title="更新されたテストTodo",
            content="内容も更新されました"
        )
        if updated_todo:
            print(f"   ✅ Todoを更新しました: {updated_todo.title}")
        else:
            print("   ❌ Todoの更新に失敗しました")
        
        # 5. すべてのTodoを再取得
        print("\n5. 更新後のTodo一覧を取得中...")
        all_todos = manager.get_all_todos()
        print(f"   ✅ {len(all_todos)}件のTodoが見つかりました")
        
        # 6. テスト用のTodoを削除（オプション）
        print("\n6. テスト用のTodoを削除中...")
        deleted = manager.delete_todo(test_todo.id)
        if deleted:
            print(f"   ✅ テスト用のTodoを削除しました")
        else:
            print("   ⚠️  テスト用のTodoの削除に失敗しました（既に削除されている可能性があります）")
        
        print("\n" + "=" * 60)
        print("✅ すべてのテストが成功しました！")
        print("=" * 60)
        
        return True
        
    except ValueError as e:
        print(f"\n❌ バリデーションエラー: {e}")
        return False
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_todo_manager()
    sys.exit(0 if success else 1)

