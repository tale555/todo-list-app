"""
Webhookエンドポイントのデバッグ用スクリプト
すべてのリクエストをログに出力
"""

from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/line/webhook', methods=['GET', 'POST'])
def line_webhook():
    """デバッグ用Webhookエンドポイント"""
    print("=" * 60)
    print("Webhookリクエストを受信しました")
    print(f"Method: {request.method}")
    print(f"URL: {request.url}")
    print(f"Headers: {dict(request.headers)}")
    print(f"Remote Address: {request.remote_addr}")
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            print(f"JSON Data: {json.dumps(data, indent=2, ensure_ascii=False)}")
        except:
            print(f"Raw Data: {request.data}")
    
    print("=" * 60)
    return 'OK', 200

@app.route('/')
def index():
    return 'Webhook Debug Server', 200

if __name__ == '__main__':
    print("=" * 60)
    print("Webhookデバッグサーバーを起動します")
    print("ポート: 5000")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5000, debug=True)

