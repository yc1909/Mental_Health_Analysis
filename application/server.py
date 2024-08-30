from flask import Flask, request, render_template, jsonify
import requests
import utils

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/assistant')
def assistant():
    return render_template('assistant.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = request.get_json()
            text_input = data["text"]
            result = utils.prediction(text_input)
            return jsonify(result=result)
        except Exception as e:
            return jsonify(error=str(e)), 500

@app.route('/mental_health_chat', methods=['POST'])
def mental_health_chat():
    try:
        input_text = request.json['input_text']
        response = requests.post(
            "http://localhost:8000/chat/invoke",
            json={'input': {'question': input_text}}
        )
        content = response.json()['output']
        return jsonify(content=content)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    utils.load_artifacts()
    app.run(host='0.0.0.0', port=5000, debug=True)
