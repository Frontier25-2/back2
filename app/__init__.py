# app/__init__.py 파일의 내용

import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

def create_app():
    load_dotenv() 
    
    print("--- ★★★ app/__init__.py 의 create_app()이 호출되었습니다. ★★★ ---")
    
    app = Flask(__name__)
    CORS(app)  # CORS 설정

    # 'app' 패키지 내부의 'routes.py' 파일을 불러와서 app에 등록합니다.
    from . import routes
    
    # "api"가 아니라 "routes.bp"를 등록합니다. (prefix 없음)
    app.register_blueprint(routes.bp) 

    return app