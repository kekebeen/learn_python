from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Heelo World"

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port = 8080)
