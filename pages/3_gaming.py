import streamlit as st

# 페이지 구성 설정
st.set_page_config(page_title="Interior", layout="centered")
st.title("Gaming")
st.write("for gamer")

# 수평선
st.markdown("---")

# 예시 사진들 표시 (가로로 배치)
col1, col2 = st.columns(2)

with col1:
    st.image("images/gaming1.jpg", caption="gaming", width=300)

with col2:
    st.image("images/gaming2.jpg", caption="gaming", width=300)

col3, col4 = st.columns(2)

with col3:
    st.image("images/gaming3.jpg", caption="gaming", width=300)

with col4:
    st.image("images/gaming4.jpg", caption="gaming", width=300)

