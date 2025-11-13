import os
import requests
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS  

def get_naver_news(query_word):
    """
    검색어(query_word)를 받아서 네이버 뉴스 API 결과를 반환하는 함수
    """
    client_id = os.getenv("NAVER_CLIENT_ID")
    client_secret = os.getenv("NAVER_CLIENT_SECRET")
    
    if not client_id or not client_secret:
        return {"error": ".env 파일에 API 키가 없습니다."}

    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    params = {
        "query": query_word,
        "display": 5  # 5개만 가져오기
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"API Error: {response.status_code}"}

def create_app():
    load_dotenv() 
    
    app = Flask(__name__)
    CORS(app)  

    @app.route('/')
    def index():
        return "Flask 백엔드 서버가 실행 중입니다."

    @app.route('/search-news')
    def handle_news_search():
        user_query = request.args.get('query')

        if not user_query:
            return jsonify({"error": "검색어가 없습니다."}), 400

        try:
            news_results = get_naver_news(user_query)
            return jsonify(news_results)
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    return app