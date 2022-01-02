from flask import Flask, render_template, request, jsonify
import os
import yaml
import joblib
import numpy as np
from prediction_service import prediction

webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        if request.form:
            data_req = dict(request.form)
            response = prediction.form_response(data_req)
            return jsonify(response)

        elif request.json:
            response = prediction.api_response(request.json)
            print(response)
            return jsonify(response)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(port=9654, debug=True)
