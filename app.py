from flask import Flask

app = Flask(__name__)


@app.route('/main')
def main():
    return 'Important stuff!'


@app.route('/health')
def health_check():
    return 'Fit as a horse!'


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)