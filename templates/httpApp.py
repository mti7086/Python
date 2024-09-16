#HTTP 메서드 (GET, POST, PUT, DELETE)
#URL 내에서 변수를 사용, flask --app httpApp run 실행 후,
# http://127.0.0.1:5000/login 주소 접속 
#기본 GET 메서드 사용
# POST 메서드는 웹 브라우저의 링크로 테스트 불가
# flask run으로 플라스크 애플리케이션을 실행한 상태
# 터미널 메뉴 오른쪽 상단에 창 분할 아이콘을 클릭해 별도 터미널 오픈
# curl.exe -X POST http://127.0.0.1:5000/login

from flask import Flask, request
app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Logging in..."
    else:
        return "Login Form"
    