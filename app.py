from flask import Flask, request, jsonify, send_file
import requests
from io import BytesIO

app = Flask(__name__)

# Replace this with your actual validation key
VALID_KEY = "1weekkeysforujjaiwal"

@app.route('/avtar-banner', methods=['GET'])
def banner_image():
    uid = request.args.get('uid')
    region = request.args.get('region')
    key = request.args.get('key')

    if not uid or not region or not key:
        return jsonify({'error': 'Missing parameters'}), 400

    if key != VALID_KEY:
        return jsonify({'error': 'Invalid key'}), 403

    # Construct the image URL from Free Fire (you need a real image source here)
    # This is just a placeholder
    banner_url = f"https://aditya-banner-v3op.onrender.com/banner-image?uid={uid}&region={region}"

    try:
        response = requests.get(banner_url)
        if response.status_code != 200:
            return jsonify({'error': 'Failed to fetch banner'}), 500

        return send_file(BytesIO(response.content), mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)