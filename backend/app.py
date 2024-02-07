from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='./build')

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/data')
def serve_data():
    # Put the data you want to send here
    return {"data": "Hello, World!"}

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True, host='0.0.0.0')