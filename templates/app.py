# if 문으로 python 실행 해도 되고, 터미널(ctrl + `)을 열고 cd templates 이동 후 flask run을 하면 된다.
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()