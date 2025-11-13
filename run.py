from app import create_app

app = create_app()

if __name__ == "__main__":
    # 5000 포트로 개발모드 실행
    app.run(host="127.0.0.1", port=5000, debug=True)
