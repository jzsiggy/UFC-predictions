from predict import make_prediction

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=["POST", "GET"])
def predict_from_post():
  if request.method == "POST":
    prediction = make_prediction(request.data)
    if prediction[0] == 1:
      return "red wins"
    else:
      return "blue wins"
  else:
    return "no post"
