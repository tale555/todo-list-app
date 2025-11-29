"""
LINE Messaging APIのUser IDを取得するスクリプト
WebhookイベントからUser IDを取得します
"""

import os
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, request, jsonify

app = Flask(__name__)

# 取得したUser IDを保存
captured_user_ids = []

@app.route('/line/webhook', methods=['POST'])
def webhook():
    """Webhookエンドポイント"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'status': 'error', 'message': 'Invalid request'}), 400
        
        events = data.get('events', [])
        
        for event in events:
            if event.get('type') == 'message':
                user_id = event.get('source', {}).get('userId')
                if user_id and user_id not in captured_user_ids:
                    captured_user_ids.append(user_id)
                    print("=" * 60)
                    print("✅ User IDを取得しました！")
                    print("=" * 60)
                    print(f"User ID: {user_id}")
                    print()
                    print("このUser IDを.envファイルのLINE_USER_IDに設定してください：")
                    print(f"LINE_USER_ID={user_id}")
                    print("=" * 60)
        
        return jsonify({'status': 'ok'})
        
    except Exception as e:
        print(f"エラー: {e}")
        return jsonify({'status': 'error', 'error': str(e)}), 500

@app.route('/line/user-ids')
def show_user_ids():
    """取得したUser IDを表示"""
    if not captured_user_ids:
        return jsonify({
            'message': 'まだUser IDが取得されていません',
            'instructions': 'LINE公式アカウントにメッセージを送信してください'
        })
    
    return jsonify({
        'user_ids': captured_user_ids,
        'latest': captured_user_ids[-1] if captured_user_ids else None
    })

if __name__ == '__main__':
    print("=" * 60)
    print("LINE User ID取得サーバー")
    print("=" * 60)
    print()
    print("📝 使い方:")
    print("1. このサーバーを起動したままにします")
    print("2. LINE Developers ConsoleでWebhook URLを設定:")
    print("   http://your-domain/line/webhook")
    print("   （ローカル開発の場合はngrokなどで公開URLを取得）")
    print("3. LINE公式アカウントを友だち追加")
    print("4. 公式アカウントにメッセージを送信")
    print("5. このコンソールにUser IDが表示されます")
    print()
    print("💡 ヒント: ngrokを使用する場合:")
    print("   ngrok http 5001")
    print("   表示されたURLをWebhook URLに設定")
    print()
    print("🚀 サーバーを起動します...")
    print()
    
    app.run(host='0.0.0.0', port=5001, debug=True)

