"""
Todo List App - メインアプリケーション
Flaskアプリケーションのエントリーポイント
"""

import os
import json
from datetime import datetime, timedelta
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash

# 環境変数から認証ファイルを作成（Render/Railway/Heroku用）
# 本番環境では認証ファイルを直接アップロードできないため、環境変数から作成
if os.getenv('GOOGLE_CREDENTIALS_JSON'):
    credentials_json = os.getenv('GOOGLE_CREDENTIALS_JSON')
    credentials_path = os.path.join('configs', 'credentials.json')
    os.makedirs('configs', exist_ok=True)
    
    # JSONが文字列形式の場合、パースして再エンコード
    try:
        # 既にJSON形式の文字列か確認
        json.loads(credentials_json)
        # JSON形式の文字列の場合、そのまま書き込み
        with open(credentials_path, 'w', encoding='utf-8') as f:
            f.write(credentials_json)
    except json.JSONDecodeError:
        # base64エンコードされている場合の処理（必要に応じて）
        import base64
        try:
            decoded = base64.b64decode(credentials_json).decode('utf-8')
            with open(credentials_path, 'w', encoding='utf-8') as f:
                f.write(decoded)
        except:
            # そのまま書き込みを試みる
            with open(credentials_path, 'w', encoding='utf-8') as f:
                f.write(credentials_json)
    
    print("✅ 環境変数から認証ファイルを作成しました")

# Flaskアプリケーションを作成
app = Flask(__name__)

# 設定を読み込む
from configs.config import SECRET_KEY
app.config['SECRET_KEY'] = SECRET_KEY


def format_date(date_str: str) -> str:
    """
    日付をフォーマット（YYYY-MM-DD形式から日本語形式に変換、曜日付き）
    
    Args:
        date_str (str): YYYY-MM-DD形式の日付文字列
        
    Returns:
        str: フォーマットされた日付（例: 2024年12月31日(火)）
    """
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        weekday_names = ['月', '火', '水', '木', '金', '土', '日']
        weekday = weekday_names[date_obj.weekday()]
        return date_obj.strftime(f'%Y年%m月%d日({weekday})')
    except:
        return date_str


def format_datetime(datetime_str: str) -> str:
    """
    日時をフォーマット（YYYY-MM-DD HH:MM:SS形式から日本語形式に変換）
    
    Args:
        datetime_str (str): YYYY-MM-DD HH:MM:SS形式の日時文字列
        
    Returns:
        str: フォーマットされた日時（例: 2024年12月31日 12:00）
    """
    try:
        dt_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        return dt_obj.strftime('%Y年%m月%d日 %H:%M')
    except:
        try:
            # YYYY-MM-DD形式の場合
            date_obj = datetime.strptime(datetime_str, '%Y-%m-%d')
            return date_obj.strftime('%Y年%m月%d日')
        except:
            return datetime_str


def is_overdue(due_date: str) -> bool:
    """
    期日が過ぎているかチェック
    
    Args:
        due_date (str): YYYY-MM-DD形式の期日
        
    Returns:
        bool: 期限切れの場合True
    """
    try:
        due = datetime.strptime(due_date, '%Y-%m-%d').date()
        today = datetime.now().date()
        return due < today
    except:
        return False


def is_due_today(due_date: str) -> bool:
    """
    期日が今日かチェック
    
    Args:
        due_date (str): YYYY-MM-DD形式の期日
        
    Returns:
        bool: 今日の場合True
    """
    try:
        due = datetime.strptime(due_date, '%Y-%m-%d').date()
        today = datetime.now().date()
        return due == today
    except:
        return False


def is_due_tomorrow(due_date: str) -> bool:
    """
    期日が明日かチェック
    
    Args:
        due_date (str): YYYY-MM-DD形式の期日
        
    Returns:
        bool: 明日の場合True
    """
    try:
        due = datetime.strptime(due_date, '%Y-%m-%d').date()
        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        return due == tomorrow
    except:
        return False


def is_due_soon(due_date: str, days: int = 3) -> bool:
    """
    期日が近いかチェック（指定日数以内、ただし明日は除く）
    
    Args:
        due_date (str): YYYY-MM-DD形式の期日
        days (int): 何日以内を「間近」とするか（デフォルト: 3日）
        
    Returns:
        bool: 期限間近の場合True（明日は除く）
    """
    try:
        from datetime import timedelta
        due = datetime.strptime(due_date, '%Y-%m-%d').date()
        today = datetime.now().date()
        days_until_due = (due - today).days
        # 明日（1日後）は除く
        return 2 <= days_until_due <= days
    except:
        return False


@app.route('/')
def index():
    """Todo詳細一覧ページ（デフォルト表示）"""
    try:
        from core.todo_manager import TodoManager
        
        manager = TodoManager()
        todos = manager.get_all_todos()
        
        # Todoアイテムに表示用の情報を追加
        for todo in todos:
            todo.formatted_due_date = format_date(todo.due_date)
            todo.formatted_created_at = format_datetime(todo.created_at)
            todo.is_overdue = is_overdue(todo.due_date)
            todo.is_due_today = is_due_today(todo.due_date) and not todo.is_overdue
            todo.is_due_tomorrow = is_due_tomorrow(todo.due_date) and not todo.is_overdue and not todo.is_due_today
            todo.is_due_soon = is_due_soon(todo.due_date) and not todo.is_overdue and not todo.is_due_today and not todo.is_due_tomorrow
        
        # カテゴリ一覧を取得
        categories = manager.get_categories()
        
        return render_template('index.html', todos=todos, categories=categories)
        
    except Exception as e:
        flash(f'エラーが発生しました: {str(e)}', 'error')
        return render_template('index.html', todos=[])


@app.route('/list')
def simple_list():
    """Todo簡易一覧ページ（タイトルと期日のみ）"""
    try:
        from core.todo_manager import TodoManager
        
        manager = TodoManager()
        todos = manager.get_all_todos()
        
        # Todoアイテムに表示用の情報を追加
        for todo in todos:
            todo.formatted_due_date = format_date(todo.due_date)
            todo.is_overdue = is_overdue(todo.due_date)
            todo.is_due_today = is_due_today(todo.due_date) and not todo.is_overdue
            todo.is_due_tomorrow = is_due_tomorrow(todo.due_date) and not todo.is_overdue and not todo.is_due_today
            todo.is_due_soon = is_due_soon(todo.due_date) and not todo.is_overdue and not todo.is_due_today and not todo.is_due_tomorrow
        
        return render_template('simple_list.html', todos=todos)
        
    except Exception as e:
        flash(f'エラーが発生しました: {str(e)}', 'error')
        return render_template('simple_list.html', todos=[])


@app.route('/detail/<todo_id>')
def detail_todo(todo_id):
    """Todo詳細ページ"""
    try:
        from core.todo_manager import TodoManager
        
        manager = TodoManager()
        todo = manager.get_todo_by_id(todo_id)
        
        if not todo:
            flash('Todoが見つかりませんでした', 'error')
            return redirect(url_for('index'))
        
        todos = [todo]  # 詳細ページでも同じ構造を使用
        
        # Todoアイテムに表示用の情報を追加
        for t in todos:
            t.formatted_due_date = format_date(t.due_date)
            t.formatted_created_at = format_datetime(t.created_at)
            t.is_overdue = is_overdue(t.due_date)
            t.is_due_today = is_due_today(t.due_date) and not t.is_overdue
            t.is_due_tomorrow = is_due_tomorrow(t.due_date) and not t.is_overdue and not t.is_due_today
            t.is_due_soon = is_due_soon(t.due_date) and not t.is_overdue and not t.is_due_today and not t.is_due_tomorrow
        
        return render_template('detail.html', todos=todos)
        
    except Exception as e:
        flash(f'エラーが発生しました: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/drafts')
def drafts():
    """一時保存データ専用ページ"""
    return render_template('drafts.html')


@app.route('/delete/<todo_id>', methods=['POST'])
def delete_todo(todo_id):
    """Todoを削除"""
    try:
        from core.todo_manager import TodoManager
        
        # todo_idが正しく取得できているか確認
        if not todo_id:
            flash('Todo IDが指定されていません', 'error')
            return redirect(url_for('index'))
        
        manager = TodoManager()
        success = manager.delete_todo(todo_id)
        
        if success:
            flash('Todoを削除しました', 'success')
        else:
            flash('Todoが見つかりませんでした', 'error')
            
    except Exception as e:
        import traceback
        print(f"削除エラー: {str(e)}")
        traceback.print_exc()
        flash(f'削除中にエラーが発生しました: {str(e)}', 'error')
    
    return redirect(url_for('index'))


@app.route('/create', methods=['GET', 'POST'])
def create_todo():
    """Todo作成ページ"""
    if request.method == 'POST':
        try:
            from core.todo_manager import TodoManager
            
            title = request.form.get('title', '').strip()
            content = request.form.get('content', '').strip()
            due_date = request.form.get('due_date', '').strip()
            category = request.form.get('category', '').strip()
            enable_line_notification = request.form.get('enable_line_notification') == 'on'
            
            # バリデーション
            errors = []
            if not title:
                errors.append('タイトルは必須です')
            # 内容は任意（バリデーション不要）
            if not due_date:
                errors.append('期日は必須です')
            elif due_date:
                try:
                    datetime.strptime(due_date, '%Y-%m-%d')
                except ValueError:
                    errors.append('期日はYYYY-MM-DD形式で入力してください（例: 2024-12-31）')
            
            if errors:
                manager = TodoManager()
                categories = manager.get_categories()
                return render_template('edit.html', todo=None, errors=errors, categories=categories)
            
            # Todoを作成
            manager = TodoManager()
            todo = manager.create_todo(title, content, due_date, category, enable_line_notification)
            
            flash('Todoを作成しました', 'success')
            return redirect(url_for('index'))
            
        except ValueError as e:
            return render_template('edit.html', todo=None, errors=[str(e)])
        except Exception as e:
            flash(f'作成中にエラーが発生しました: {str(e)}', 'error')
            return render_template('edit.html', todo=None, errors=[])
    
    # GETリクエスト: フォームを表示
    from core.todo_manager import TodoManager
    manager = TodoManager()
    categories = manager.get_categories()
    return render_template('edit.html', todo=None, errors=[], categories=categories)


@app.route('/edit/<todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    """Todo編集ページ"""
    try:
        from core.todo_manager import TodoManager
        
        manager = TodoManager()
        
        if request.method == 'POST':
            # 更新処理
            title = request.form.get('title', '').strip()
            content = request.form.get('content', '').strip()
            due_date = request.form.get('due_date', '').strip()
            category = request.form.get('category', '').strip()
            enable_line_notification = request.form.get('enable_line_notification') == 'on'
            
            # バリデーション
            errors = []
            if not title:
                errors.append('タイトルは必須です')
            # 内容は任意（バリデーション不要）
            if not due_date:
                errors.append('期日は必須です')
            elif due_date:
                try:
                    datetime.strptime(due_date, '%Y-%m-%d')
                except ValueError:
                    errors.append('期日はYYYY-MM-DD形式で入力してください（例: 2024-12-31）')
            
            if errors:
                # エラーがある場合、既存のTodoを取得してフォームに表示
                todo = manager.get_todo_by_id(todo_id)
                if not todo:
                    flash('Todoが見つかりませんでした', 'error')
                    return redirect(url_for('index'))
                categories = manager.get_categories()
                return render_template('edit.html', todo=todo, errors=errors, categories=categories)
            
            # Todoを更新
            updated_todo = manager.update_todo(todo_id, title=title, content=content, due_date=due_date, category=category, enable_line_notification=enable_line_notification)
            
            if updated_todo:
                flash('Todoを更新しました', 'success')
                return redirect(url_for('index'))
            else:
                flash('Todoが見つかりませんでした', 'error')
                return redirect(url_for('index'))
        
        # GETリクエスト: 既存のTodoを取得してフォームに表示
        todo = manager.get_todo_by_id(todo_id)
        if not todo:
            flash('Todoが見つかりませんでした', 'error')
            return redirect(url_for('index'))
        
        categories = manager.get_categories()
        return render_template('edit.html', todo=todo, errors=[], categories=categories)
        
    except Exception as e:
        flash(f'エラーが発生しました: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/update-order', methods=['POST'])
def update_order():
    """Todoの順序を更新"""
    try:
        from core.todo_manager import TodoManager
        
        data = request.get_json()
        if not data or 'orders' not in data:
            return jsonify({'success': False, 'error': '無効なリクエストです'}), 400
        
        todo_orders = data['orders']
        if not isinstance(todo_orders, list):
            return jsonify({'success': False, 'error': '無効なデータ形式です'}), 400
        
        manager = TodoManager()
        success = manager.update_todo_order(todo_orders)
        
        if success:
            return jsonify({'success': True, 'message': '順序を更新しました'})
        else:
            return jsonify({'success': False, 'error': '順序の更新に失敗しました'}), 500
            
    except Exception as e:
        import traceback
        print(f"順序更新エラー: {str(e)}")
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/toggle-completion/<todo_id>', methods=['POST'])
def toggle_completion(todo_id):
    """Todoの完了状態を切り替え"""
    try:
        from core.todo_manager import TodoManager
        
        manager = TodoManager()
        todo = manager.toggle_todo_completion(todo_id)
        
        if todo:
            return jsonify({
                'success': True, 
                'message': '完了状態を更新しました',
                'is_completed': todo.is_completed
            })
        else:
            return jsonify({'success': False, 'error': 'Todoが見つかりませんでした'}), 404
            
    except Exception as e:
        import traceback
        print(f"完了状態更新エラー: {str(e)}")
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/send-line-notifications', methods=['POST'])
def send_line_notifications():
    """LINE通知を送信（手動実行用）"""
    try:
        from core.line_notifier import LineNotifier
        
        notifier = LineNotifier()
        count = notifier.check_and_send_reminders()
        
        if count > 0:
            return jsonify({
                'success': True,
                'message': f'{count}件の通知を送信しました'
            })
        else:
            return jsonify({
                'success': True,
                'message': '通知対象のTodoはありませんでした'
            })
            
    except Exception as e:
        import traceback
        print(f"LINE通知エラー: {str(e)}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/test-sheets')
def test_sheets():
    """Google Sheets API接続のテストエンドポイント（開発用）"""
    try:
        from core.sheets_manager import SheetsManager
        
        manager = SheetsManager()
        info = manager.get_spreadsheet_info()
        
        return jsonify({
            'status': 'success',
            'spreadsheet_title': info['title'],
            'sheets': [s['title'] for s in info['sheets']],
            'message': 'Google Sheets API接続成功'
        })
    except FileNotFoundError as e:
        return jsonify({
            'status': 'error',
            'error': '認証ファイルが見つかりません',
            'message': str(e),
            'help': 'USER_SETUP_GUIDE.mdを参照してGoogle Sheets APIの設定を行ってください'
        }), 500
    except ValueError as e:
        return jsonify({
            'status': 'error',
            'error': '設定エラー',
            'message': str(e),
            'help': '.envファイルにSPREADSHEET_IDを設定してください'
        }), 500
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': '接続エラー',
            'message': str(e)
        }), 500


@app.route('/line/webhook', methods=['GET', 'POST'])
def line_webhook():
    """LINE Webhookエンドポイント（User ID取得用）"""
    # GETリクエスト（LINEのWebhook検証用）
    if request.method == 'GET':
        print("\n" + "=" * 60)
        print("✅ Webhook検証リクエストを受信しました (GET)")
        print("=" * 60 + "\n")
        return 'OK', 200
    
    # POSTリクエスト（イベント受信用）
    try:
        # デバッグ: リクエスト情報をログ出力
        print("\n" + "=" * 60)
        print("📥 POSTリクエストを受信しました")
        print(f"   リモートアドレス: {request.remote_addr}")
        print(f"   ユーザーエージェント: {request.headers.get('User-Agent', 'N/A')}")
        print("=" * 60)
        
        # リクエストボディを取得
        data = request.get_json()
        
        if not data:
            print("⚠️  Webhook: リクエストボディが空です")
            print("   生データ:", request.data[:200] if request.data else "なし")
            print("=" * 60 + "\n")
            return 'OK', 200  # LINEは常に200を期待する
        
        print("✅ リクエストボディを取得しました")
        
        # イベントを処理
        events = data.get('events', [])
        print(f"   イベント数: {len(events)}")
        
        user_ids = []
        
        for i, event in enumerate(events, 1):
            event_type = event.get('type')
            print(f"\n   イベント #{i}:")
            print(f"     タイプ: {event_type}")
            
            # ソース情報を取得
            source = event.get('source', {})
            user_id = source.get('userId')
            print(f"     User ID: {user_id if user_id else '(なし)'}")
            
            # 友だち追加イベント
            if event_type == 'follow':
                user_id = event.get('source', {}).get('userId')
                if user_id:
                    user_ids.append(user_id)
                    print("=" * 60)
                    print("✅ 友だち追加イベントを受信しました！")
                    print(f"   User ID: {user_id}")
                    print("   このUser IDを.envファイルのLINE_USER_IDに設定してください")
                    print("=" * 60)
            
            # メッセージイベント
            elif event_type == 'message':
                user_id = event.get('source', {}).get('userId')
                if user_id:
                    user_ids.append(user_id)
                    print("=" * 60)
                    print("✅ メッセージイベントを受信しました！")
                    print(f"   User ID: {user_id}")
                    print("   このUser IDを.envファイルのLINE_USER_IDに設定してください")
                    print("=" * 60)
        
        # LINEは常に200を期待する（エラーでも200を返す）
        return 'OK', 200
            
    except Exception as e:
        import traceback
        print(f"⚠️  Webhookエラー: {str(e)}")
        traceback.print_exc()
        # エラーでも200を返す（LINEの要件）
        return 'OK', 200


@app.route('/line/get-user-id')
def get_user_id_info():
    """User ID取得方法の説明ページ"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>LINE User ID取得方法</title>
        <meta charset="UTF-8">
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
            h1 { color: #333; }
            .step { background: #f5f5f5; padding: 15px; margin: 10px 0; border-radius: 5px; }
            .code { background: #e8e8e8; padding: 10px; border-radius: 3px; font-family: monospace; }
        </style>
    </head>
    <body>
        <h1>📱 LINE User ID取得方法</h1>
        
        <div class="step">
            <h2>方法1: 対話型テストスクリプトを使用（推奨）</h2>
            <p>以下のコマンドを実行して、User IDを直接入力できます：</p>
            <div class="code">python test_line_interactive.py</div>
        </div>
        
        <div class="step">
            <h2>方法2: Webhookを使用して取得</h2>
            <p>1. LINE Developers ConsoleでWebhook URLを設定</p>
            <p>2. LINE公式アカウントを友だち追加</p>
            <p>3. 公式アカウントにメッセージを送信</p>
            <p>4. サーバーログでUser IDを確認</p>
        </div>
        
        <p><a href="/">← トップページに戻る</a></p>
    </body>
    </html>
    """
    return html


if __name__ == '__main__':
    # 開発サーバーを起動
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    print("🚀 Todo List App サーバーを起動...")
    print(f"📍 アクセス: http://localhost:{port}")
    print("⚠️  開発モードで実行中です")
    
    app.run(host='0.0.0.0', port=port, debug=debug)

