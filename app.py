import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import whisper

app = Flask(__name__)
CORS(app)

model = whisper.load_model("small")


@app.route("/process_audio", methods=["POST"])
def process_audio():
    print("reached process_audio")
    print(request.content_type)
    data = request.form
    # data["dsf"] = "123123"
    print("data")
    print(data)

    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    audio_path = "/tmp/audio.wav"
    audio_file.save(audio_path)

    result = model.transcribe(audio_path)
    output = {"language": result["language"], "text": result["text"]}
    print("OUTPUT", output)
    return output


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/hell", methods=["POST"])
def hello_post():
    print(request)
    return "Hello World!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
