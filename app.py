from waitress import serve
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/test/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    print("running!")
    serve(app, host="0.0.0.0", port=3010)
