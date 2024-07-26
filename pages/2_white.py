import streamlit as st

# 페이지 구성 설정
st.set_page_config(page_title="Interior", layout="centered")
st.title("White")
st.write("화이트톤의 인테리어")

# 수평선
st.markdown("---")

# 예시 사진들 표시 (가로로 배치)
col1, col2 = st.columns(2)

with col1:
    st.image("images/white(1).jpg", caption="white ton", width=300)

with col2:
    st.image("images/white(2).jpg", caption="white ton", width=300)

col3, col4 = st.columns(2)

with col3:
    st.image("images/white(3).jpg", caption="white ton", width=300)

with col4:
    st.image("images/white(4).jpg", caption="white ton", width=300)

