from flask import Flask, render_template, request, jsonify
import os
import yaml
import joblib
import numpy as np

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

@app.route("/")
def index():
    return render_template("index.html")

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    return prediction

def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response": response[0]}
        return response
    except Exception as e:
        print(e)
        error = {"error": "Something went wrong!! Try Again"}
        return error


@app.route('/predict',methods=['POST','GET'])
def result():
    if request.method == "POST":
        try:
            if request.form:
                data = [list(dict(request.form).values())]
                prediction = predict(data)
                print(prediction)
                return jsonify(prediction[0])

            elif request.json:
                response = api_response(request)
                print(response)
                return jsonify(response)

        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!! Try Again"}
            return jsonify(error)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8278, debug= True)
