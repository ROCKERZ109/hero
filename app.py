from flask import Flask, request, jsonify
import chatbot

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def returnascii():
    d = {}
    inputchr = str(request.args['query'])
    ints = chatbot.predict_class(inputchr)
    answer = chatbot.get_response(ints, chatbot.intents)
    # answer = str(ord(inputchr))
    d['output'] = answer
    return d


if __name__ == "__main__":
    app.run()
