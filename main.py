'''from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print('1')
    print(categor(userText))
    return str(userText)


if __name__ == "__main__":
    app.run()
'''
from categor import opts,cmds,categor_cmds,categor
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    print(request.args.get('msg'))


if __name__ == "__main__":
    app.run()

