import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import whisper

app = Flask(__name__)
CORS(app)

model = whisper.load_model('large')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    audio_path = '/tmp/audio.wav'
    audio_file.save(audio_path)

    result = model.transcribe(audio_path, task='translate')
    return jsonify({"language": result['language'], "text": result['text']})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)