# if 문으로 python 실행 해도 되고, 터미널(ctrl + `)을 열고 cd templates 이동 후 flask run을 하면 된다.
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True) # debug=True로 디버그 모드 활성화, 코드 변경하고 저장만 해도 플라스크가 자동으로 
                        # 변경 사항을 감지하고 애플리케이션을 재시작한다
                        # 웹페이지에서 발생하는 예외를 직접 볼 수 있다.