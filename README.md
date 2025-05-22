# Software-Engineering  
소프트웨어 공학 과제  
컴퓨터공학과 / 20190035 / 나상준

---

## 📌 과제 개요

- **주제**: 일상 속 소프트웨어 사용 사례 모델링 및 샘플 코드 구현  
- **목표**: 실생활에서 사용되는 시스템을 시퀀스 다이어그램으로 모델링하고, 해당 흐름을 샘플 코드로 구현하여 모듈 구조를 분석함으로써 소프트웨어 공학 원칙을 체험

---

## 🖼️ 사용 사례: **카페 키오스크 시스템**

요즘 카페에 자주 도입된 **무인 키오스크 시스템**을 모델링 대상으로 삼았습니다.  
사용자는 키오스크 화면을 통해 원하는 음료를 고르고, 시스템은 해당 주문을 처리하여 응답합니다.

---

## 🧭 시퀀스 다이어그램

> 아래는 Mermaid 문법을 활용하여 작성한 시퀀스 다이어그램입니다.

```mermaid
sequenceDiagram
    participant User
    participant WebClient as Browser
    participant FlaskApp
    participant OrderManager

    User->>WebClient: 키오스크 페이지 접속
    WebClient->>FlaskApp: GET /
    FlaskApp-->>WebClient: kiosk.html 렌더링 (메뉴, 이미지, 가격)
    User->>WebClient: 메뉴 선택
    WebClient->>FlaskApp: POST /order (선택한 항목 전송)
    FlaskApp->>OrderManager: 주문 처리 요청
    OrderManager-->>FlaskApp: 주문 처리 로그 반환
    FlaskApp-->>WebClient: JSON 응답 (주문 완료 메시지)
