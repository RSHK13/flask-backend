from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)
model = whisper.load_model('large')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    audio_file = request.files['audio']
    file_path = 'temp_audio.wav'
    audio_file.save(file_path)
    
    result = model.transcribe(file_path, task='translate')
    
    # Clean up the temporary file
    os.remove(file_path)
    
    return jsonify({'language': result['language'], 'text': result['text']})

if __name__ == '__main__':
    app.run(debug=True)