from flask import Flask, render_template, request, jsonify

from llama import ask_llama2

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/prompt', methods=['POST'])
def prompt():
    data = request.json
    question = data.get('prompt')
    response = ask_llama2(question)
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
