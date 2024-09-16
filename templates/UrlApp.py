# p42_p49
# flask --app UrlApp run
# http://127.0.0.1:5000/user/JohnDoe

# profile() 함수 내부의 url_for("index") 코드를 수정할 필요가 없음
# 'index'라는 함수 이름으로 라우트를 찾고, 해당 함수에 매핑된 최신 URL 반환
# URL이 /home으로 변경되어도 url_for("index")는 자동으로 /home을 반환
# http://127.0.0.1:5000/home 실행시 "홈페이지에 오신 것을 환영합니다!"


from flask import Flask, url_for

app = Flask(__name__)

# 기본 홈페이지 경로
@app.route('/home') # / 에서 /home으로 변경 # 
def index():
    return '홈페이지에 오신 것을 환영합니다!'

# 사용자 정보 페이지 경로
@app.route('/user/<username>')
def profile(username):
    # url_for()를 사용하여 'index' 뷰 함수의 URL을 생성합니다.
    return f'''{username}님의 프로필 페이지입니다.
    홈으로 가기: {url_for("index")}'''