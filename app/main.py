from flask import Flask
app = Flask(__name__)


version = "4"

@app.route("/")
def hello():
    return "Hello World version: " + version 

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
