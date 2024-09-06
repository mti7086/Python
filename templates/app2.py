#URL 내에서 변수를 사용, flask --app app2 run 실행 후, http://127.0.0.1:5000/user/John 주소 접속
from flask import Flask
app2 = Flask(__name__)

@app2.route("/user/<username>")
def show_user_profile(username):
    return f"User {username}"