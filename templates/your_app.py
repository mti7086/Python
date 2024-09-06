# 파일명이 app.py가 아닌 경우에는 flask --app your_app.py run /// 당연하게도 cd templates 한 후 실행(flask run 상세 사용법)
# --reload옵션: 실행 중인 코드를 수정 후 저장하면 재실행 없이 바로 수정 사항 반영
# flask --app your_app run --host=0.0.0.0 --port=8000 --reload
# IP 주소: 인터넷 프로토콜 주소는 네트워크상에서 컴퓨터나 서버를 식별하는 주소
# 포트: IP 주소가 '아파트 단지'라면, 포트는 '아파트 동호수'와 같은 역할, 여러 애플리케이션을 동시에 실행할 수 있음
from flask import Flask
app = Flask(__name__)

@app.route('/') 
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)