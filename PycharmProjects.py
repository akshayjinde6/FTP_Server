from flask import Flask
import pysftp as sftp

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello word!'


if __name__ == '__main__':
    app.run()
