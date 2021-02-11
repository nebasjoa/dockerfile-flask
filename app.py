from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

@app.route('/about')
def about():
    return 'About page.'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')