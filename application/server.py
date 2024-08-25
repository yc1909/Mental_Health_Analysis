from flask import Flask,request,render_template,jsonify
import utils

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/prediction', methods = ['GET','POST'])
def prediction():
    if request.method == 'GET':
        return render_template('home.html')

    else:
        text_input = request.json["text"]
        result = utils.prediction(text_input)
        return jsonify(result = result)


if __name__ == '__main__':
    utils.load_artifacts()
    app.run(host='0.0.0.0', port=5000, debug=False)
