from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'Server is running'

if __name__ == '__main__':
    app.run(port=5000, debug=True)