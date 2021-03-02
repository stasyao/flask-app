from flask import Flask


app = Flask('hello')


@app.route('/')
def hello_world():
    return 'У меня получилось!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
