from flask import Flask,render_template

app = Flask(__name__)

@app.route("/<name>")
@app.route("/")
def index(name=None):
    if name:
        return "Hello "+name
    else:
        return "Hello"

if __name__ == '__main__':
    app.run(debug=True)
