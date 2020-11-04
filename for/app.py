from flask import Flask, render_template

app = Flask(__name__)


@app.route('/for')
def for_exp():
    names = ['Alex', 'Sharon', 'Clara']
    return render_template('index.html', isimler=names)


if __name__ == '__main__':
    app.run(debug=True)
