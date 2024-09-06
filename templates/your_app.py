# 파일명이 app.py가 아닌 경우에는 flask --app your_app.py run /// 당연하게도 cd templates 한 후 실행(flask run 상세 사용법)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)