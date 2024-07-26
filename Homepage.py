import streamlit as st

# 페이지 구성 설정
st.set_page_config(page_title="Interior", layout="centered")

# 큰 글자로 회사 이름 표시
st.title("INTERIOR")

# 설명문 표시
st.write("AI 이미지 랜더링 기반의 기술과 맞춤형 아키텍처를 활용한 공간 인테리어")

# 수평선
st.markdown("---")

# 예시 사진들 표시 (가로로 배치)
col1, col2 = st.columns(2)

with col1:
    st.image("images/20Male(1).jpg", caption="recommend", width=300)

with col2:
    st.image("images/black(3).jpg", caption="black ton", width=300)

col3, col4 = st.columns(2)

with col3:
    st.image("images/white(1).jpg", caption="white ton", width=300)

with col4:
    st.image("images/gaming1.jpg", caption="gaming room", width=300)
