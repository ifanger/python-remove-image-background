import io
from flask import Flask, request, jsonify, send_file
from rembg import remove

app = Flask(__name__)

API_KEY = 'changeme123'
MAX_FILE_SIZE_MB = 1
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

def validate_api_key():
    api_key = request.headers.get('X-Api-Key')
    if api_key != API_KEY:
        return False
    return True

@app.route('/remove-background', methods=['POST'])
def remove_background():
    if not validate_api_key():
        return jsonify({"error": "Unauthorized"}), 401

    if 'image' not in request.files:
        return jsonify({"error": "Image resource not found"}), 400

    file = request.files['image']
    input_bytes = file.read()
    file_size = len(input_bytes)

    if file_size > MAX_FILE_SIZE_BYTES:
        return jsonify({"error": "File size exceeds 1MB"}), 413
    file.seek(0)
    
    output_bytes = remove(input_bytes)

    return send_file(
        io.BytesIO(output_bytes),
        mimetype='image/png',
        as_attachment=True,
        download_name='output.png'
    )

if __name__ == '__main__':
    app.run()
