from flask import Flask, request, jsonify
import chatbot

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    d = {}
    inputchr = str(request.args['queri'])
    ints = chatbot.predict_class(inputchr)
    answer = chatbot.get_response(ints, chatbot.intents)
    d['output'] = answer
    return d


if __name__ == "__main__":
    app.run()
