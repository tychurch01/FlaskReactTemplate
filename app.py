from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/load-data')
def load_data():
    # Call your function from services.py and return the data.
    data = services.load_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5050)


