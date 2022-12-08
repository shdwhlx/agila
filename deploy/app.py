from model import make_prediction
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def predict():
    text = request.form['text']
    prediction = make_prediction(text)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug = True)
