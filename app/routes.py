# app/routes.py 파일의 내용

import os
import requests
import json
from flask import request, jsonify, Blueprint # Blueprint를 import

# 'main'이라는 이름의 'bp' 객체를 생성합니다.
bp = Blueprint('main', __name__)

# --- 네이버 뉴스 검색 함수 ---
def get_naver_news(query_word):
    client_id = os.getenv("NAVER_CLIENT_ID")
    client_secret = os.getenv("NAVER_CLIENT_SECRET")
    
    if not client_id or not client_secret:
        return {"error": ".env 파일에 API 키가 없습니다."}

    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
    params = {"query": query_word, "display": 5}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"API Error: {response.status_code}"}

# --- 라우트 정의 ---
# @app.route 대신 @bp.route를 사용합니다.

@bp.route('/')
def index():
    return "Flask 백엔드 서버가 실행 중입니다. (app/routes.py에서 응답)"

@bp.route('/search-news')
def handle_news_search():
    user_query = request.args.get('query')
    if not user_query:
        return jsonify({"error": "검색어가 없습니다."}), 400
    try:
        news_results = get_naver_news(user_query)
        return jsonify(news_results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500