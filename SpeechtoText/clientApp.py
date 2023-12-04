from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from com_in_utils.utils import decodeSound
from speechtoText import speech2Text

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['sound']
    decodeSound(image, "Audio123.wav")
    result = speech2Text("Audio123.wav")
    return jsonify({"Result" : str(result)})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
