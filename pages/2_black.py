import streamlit as st

# 페이지 구성 설정
st.set_page_config(page_title="Interior", layout="centered")
st.title("Black")
st.write("다크톤의 인테리어")

# 수평선
st.markdown("---")

# 예시 사진들 표시 (가로로 배치)
col1, col2 = st.columns(2)

with col1:
    st.image("images/black(1).jpg", caption="black ton", width=300)

with col2:
    st.image("images/black(2).jpg", caption="black ton", width=300)

st.image("images/black(3).jpg", caption="black ton", width=300)
