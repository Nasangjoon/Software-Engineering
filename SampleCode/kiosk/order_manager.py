import time

class OrderManager:
    def __init__(self):
        self.log = []

    def add_log(self, message: str):
        self.log.append(message)

    def process_order(self, item: dict):
        self.log.clear()
        name = item["name"]
        price = item["price"]

        self.add_log(f"🧍 고객: '{name}' 주문합니다. (가격: {price}원)")
        time.sleep(0.5)

        self.add_log("💳 결제 모듈: 결제 처리 중...")
        time.sleep(0.5)

        self.add_log("✅ 결제 완료")
        time.sleep(0.5)

        self.add_log(f"👨‍🍳 주방: 조리 시작 - {name}")
        time.sleep(1)

        self.add_log("☕ 주문 완료! 음료가 준비되었습니다.")

        return self.log.copy()
