# Simple flask app for testing purposes


from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/bagels')
def bagels():
    name = request.args.get("name", "Fred")
    greeting = "{} likes bagels.".format(name)
    return greeting


if __name__ == "__main__":
    print("Hello, world!")

    app.run('localhost', '5000')
