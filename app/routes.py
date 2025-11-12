from flask import Blueprint, request, jsonify
from app.services.analytics_service import calculate_weights

api = Blueprint("api", __name__)

@api.route("/weights", methods=["POST"])
def get_weights():
    data = request.get_json(silent=True) or {}

    # 예: 프론트에서 보내는 payload 그대로 받는 구조라면
    # {"model": "...", "assets":[...], "allow_short": false}
    # 위 형식이라 가정
    if "assets" not in data:
        return jsonify({"error": "assets is required"}), 400

    result = calculate_weights(data)   # data 전체 넘기는 예시
    return jsonify(result)
