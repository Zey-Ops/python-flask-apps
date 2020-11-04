from flask import Flask, render_template

app = Flask(__name__)


# using just before the function. Connect the function with path.
@app.route('/')
def hello():
    return "Hello World!!!"


if __name__ == "__main__":
    # show the mistakes while working
    app.run(host='0.0.0.0', port=80)
