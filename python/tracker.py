from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello " + request.args.get("name")

if __name__ == "__main__":
    app.run(debug=True)