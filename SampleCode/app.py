from flask import Flask, render_template, request, jsonify
from kiosk.order_manager import OrderManager

app = Flask(__name__)

MENU = [
    {"name": "아이스 아메리카노", "image": "/static/images/americano.png", "price": 3000},
    {"name": "카페라떼", "image": "/static/images/latte.png", "price": 3500},
    {"name": "바닐라라떼", "image": "/static/images/vanilla_latte.png", "price": 4000},
    {"name": "카푸치노", "image": "/static/images/cappuccino.png", "price": 3700},
]

order_manager = OrderManager()

@app.route("/")
def kiosk():
    return render_template("kiosk.html", menu=MENU)

@app.route("/order", methods=["POST"])
def order():
    data = request.get_json()
    item_name = data.get("item")
    # 메뉴에 있는지 확인
    item = next((m for m in MENU if m["name"] == item_name), None)
    if item is None:
        return jsonify({"error": "잘못된 주문 항목입니다."}), 400

    log = order_manager.process_order(item)
    return jsonify({"log": log})

if __name__ == "__main__":
    app.run(debug=True)
