from flask import Flask, send_from_directory
import os
import subprocess

app = Flask(__name__, static_folder='./build')

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/data')
def serve_data():
    # Put the data you want to send here
    return {"data": "Hello, World!"}

def start_react():
    try:
        os.chdir('./frontend/reactApp')  # Try to navigate to my-app directory
    except FileNotFoundError:
        print("Could not find directory '.../frontend/my-app'. Please check that your paths are correct.")
        return  # If we can't find the directory we should not continue trying to start the process

    try:
        subprocess.Popen("npm start", shell=True)  # Try to start the react app
    except Exception as e:
        print("Could not start the React app. Ensure you have npm installed and try again.")
        print("Error:", e)


if __name__ == '__main__':
    start_react()
    app.run(use_reloader=True, debug=True, host='0.0.0.0',port=5051)