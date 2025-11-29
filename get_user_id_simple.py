"""
LINE User IDを簡単に取得するスクリプト
Webhookイベントを待機してUser IDを表示します
"""

import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# 取得したUser IDを保存
captured_user_ids = set()

@app.route('/line/webhook', methods=['POST'])
def webhook():
    """Webhookエンドポイント"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'status': 'error', 'message': 'Invalid request'}), 400
        
        events = data.get('events', [])
        
        for event in events:
            event_type = event.get('type')
            
            # 友だち追加イベント
            if event_type == 'follow':
                user_id = event.get('source', {}).get('userId')
                if user_id:
                    captured_user_ids.add(user_id)
                    print("=" * 60)
                    print("✅ 友だち追加イベントを受信しました！")
                    print("=" * 60)
                    print(f"User ID: {user_id}")
                    print()
                    print("このUser IDを.envファイルのLINE_USER_IDに設定してください：")
                    print(f"LINE_USER_ID={user_id}")
                    print("=" * 60)
            
            # メッセージイベント
            elif event_type == 'message':
                user_id = event.get('source', {}).get('userId')
                if user_id:
                    captured_user_ids.add(user_id)
                    print("=" * 60)
                    print("✅ メッセージイベントを受信しました！")
                    print("=" * 60)
                    print(f"User ID: {user_id}")
                    print()
                    print("このUser IDを.envファイルのLINE_USER_IDに設定してください：")
                    print(f"LINE_USER_ID={user_id}")
                    print("=" * 60)
        
        return jsonify({'status': 'ok'})
        
    except Exception as e:
        print(f"エラー: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'status': 'error', 'error': str(e)}), 500

@app.route('/line/user-ids')
def show_user_ids():
    """取得したUser IDを表示"""
    if not captured_user_ids:
        return jsonify({
            'message': 'まだUser IDが取得されていません',
            'instructions': 'LINE公式アカウントを友だち追加するか、メッセージを送信してください'
        })
    
    return jsonify({
        'user_ids': list(captured_user_ids),
        'latest': list(captured_user_ids)[-1] if captured_user_ids else None
    })

if __name__ == '__main__':
    print("=" * 60)
    print("LINE User ID取得サーバー")
    print("=" * 60)
    print()
    print("📝 使い方:")
    print("1. このサーバーを起動したままにします")
    print("2. LINE Developers ConsoleでWebhook URLを設定:")
    print("   - ローカル開発の場合: ngrokなどで公開URLを取得")
    print("   - 例: https://xxxx-xxxx.ngrok-free.app/line/webhook")
    print("3. 「Webhookの利用」をONにする")
    print("4. LINE公式アカウントを友だち追加")
    print("5. または、公式アカウントにメッセージを送信")
    print("6. このコンソールにUser IDが表示されます")
    print()
    print("💡 ngrokがインストールされていない場合:")
    print("   - 方法1: ngrokをインストール（https://ngrok.com/）")
    print("   - 方法2: クラウドサービス（Heroku、Railway等）にデプロイ")
    print()
    print("🚀 サーバーを起動します...")
    print("   ポート: 5001（メインアプリと競合しないように）")
    print()
    
    app.run(host='0.0.0.0', port=5001, debug=True)

