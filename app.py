import random
import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 메뉴 추천", page_icon="🍽️")

# 2. 제목 및 설명
st.title("🍽️ 오늘 뭐 먹지? 점심 메뉴 추천기")
st.write("고민될 땐 버튼을 눌러 운명에 맡겨보세요!")

# 3. 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "비빔밥",
    "짜장면",
    "짬뽕",
    "초밥",
    "라멘",
    "파스타",
    "햄버거",
    "쌀국수",
    "순대국밥",
    "떡볶이",
    "마라탕",
    "샐러드",
    "샌드위치",
    "카레라이스",
]

# 4. 버튼 생성 및 랜덤 추천 로직
if st.button("🎲 오늘의 점심 메뉴 뽑기!", use_container_width=True):
  selected_menu = random.choice(lunch_menus)

  # 결과 출력 및 축하 효과
  st.success(f"오늘의 추천 점심 메뉴는 **{selected_menu}**입니다! 🎉")
  st.balloons()
