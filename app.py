from flask import Flask

app = Flask('python_api')

@app.route("/")
def hello_world():
    return "Hello World! <strong>I am learning Flask</strong>", 200

@app.route("/<name>")
def index(name):
    if name.lower() == "bruno":
        return "Olá {}".format(name), 200
    else:
        return "Not Found", 404

app.run()