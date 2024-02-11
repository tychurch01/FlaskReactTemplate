from flask import Flask, send_from_directory
from flask_cors import CORS
import os
import subprocess

# Switch this to False for production mode.
# In production mode, Flask serves the static files.
# In development mode, the React development server is used,
DEV_MODE = True

app = Flask(__name__, static_folder='build')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if DEV_MODE:
        return "Development mode active. This route doesn't serve the app."
    elif path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/data')
def serve_data():
    # Put the data you want to send here
    return {"data": "Hello, World!"}

def start_react():
    if not DEV_MODE:
        return
    try:
        os.chdir('./frontend/reactApp')  # Try to navigate to my-app directory
    except FileNotFoundError:
        print("Could not find directory './frontend/my-app'. Please check that your paths are correct.")
        return  # If we can't find the directory we should not continue trying to start the process

    try:
        subprocess.Popen("npm start", shell=True)  # Try to start the react app
    except Exception as e:
        print("Could not start the React app. Ensure you have npm installed and try again.")
        print("Error:", e)

if DEV_MODE:
    CORS(app, origins=["http://localhost:3000"])

if __name__ == '__main__':
    start_react()
    app.run(use_reloader=True, debug=True, host='127.0.0.1',port=5051)