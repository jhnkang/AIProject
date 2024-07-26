
import streamlit as st
import numpy as np

st.title("INTERIOR")
st.markdown("---")
# 사용자 메시지 출력
with st.chat_message("user"):
    st.write("Hello 👋")
    st.write("원하시는 인테리어가 있을까요?")
# 예시 사진들 표시 (가로로 배치)
col1, col2 = st.columns(2)

with col1:
    st.image("images/20Male(1).jpg", width=300)
    st.write("가장 많이 선택하는 디자인")

with col2:
    st.image("images/white(1).jpg", width=300)
    st.write("화이트톤의 깔끔한 인테리어")

st.markdown("---")

with st.chat_message("user"):
    st.write("Hello 👋")
    st.write("나만의 인테리어 만들기")

st.write("CustomOrder 페이지에서 주문 제작")

# 예시 사진들 표시 (가로로 배치)
col1, col2, col3 = st.columns([1, 0.1, 1])  # 가운데 열을 작게 설정

with col1:
    st.image("images/12.jpg", width=300)
    st.write("기존의 인테리어")

with col2:
    st.markdown('<div style="font-size: 30px; text-align: center;">➡️</div>', unsafe_allow_html=True)

with col3:
    st.image("images/12-1.png", width=300)
    st.write("나만의 방")