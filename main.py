import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="🌙 미연시 게임",
    layout="wide"
)

# -----------------------------
# 다크 모드 스타일
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #111111;
    color: white;
}

h1, h2, h3, p, div {
    color: white !important;
}

.stButton > button {
    width: 100%;
    background-color: #333333;
    color: white;
    border-radius: 10px;
    height: 60px;
    font-size: 18px;
}

.stButton > button:hover {
    background-color: #555555;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 상태 저장
# -----------------------------
if "scene" not in st.session_state:
    st.session_state.scene = 1

if "fear" not in st.session_state:
    st.session_state.fear = 0

# -----------------------------
# 사이드바
# -----------------------------
with st.sidebar:
    st.title("😱 상태창")
    st.metric("공포심", st.session_state.fear)

# -----------------------------
# 장면 1
# -----------------------------
if st.session_state.scene == 1:

    st.title("🌙 프롤로그")

    st.write("""
    (당신은 매우 어두운 골목길을 걸어가고있습니다 )

    (저 멀리서 부스럭 소리와 함께 무언가가 있는 기분이 물씬 풍겨옵니다)
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📢 누구냐고 소리치기"):
            st.session_state.scene = 2
            st.rerun()

    with col2:
        if st.button("🏃 도망치기"):
            st.session_state.fear += 10
            st.session_state.scene = 3
            st.rerun()

    with col3:
        if st.button("🚶 무시하고 걷기"):
            st.session_state.scene = 4
            st.rerun()

# -----------------------------
# 누구냐고 소리치기
# -----------------------------
elif st.session_state.scene == 2:

    st.title("📢 누구냐고 소리쳤다")

    st.write("""
    (내용을 적으시오)

    (내용을 적으시오)

    (내용을 적으시오)
    """)

    if st.button("다음"):
        st.session_state.scene = 5
        st.rerun()

# -----------------------------
# 도망치기
# -----------------------------
elif st.session_state.scene == 3:

    st.title("🏃 도망쳤다")

    st.write("""
    공포심이 10 증가했다!

    (내용을 적으시오)

    (내용을 적으시오)

    (내용을 적으시오)
    """)

    if st.button("다음"):
        st.session_state.scene = 5
        st.rerun()

# -----------------------------
# 무시하고 걷기
# -----------------------------
elif st.session_state.scene == 4:

    st.title("🚶 무시하고 걸었다")

    st.write("""
    (내용을 적으시오)

    (내용을 적으시오)

    (내용을 적으시오)
    """)

    if st.button("다음"):
        st.session_state.scene = 5
        st.rerun()

# -----------------------------
# 공통 다음 장면
# -----------------------------
elif st.session_state.scene == 5:

    st.title("🌑 다음 이야기")

    st.write("""
    (내용을 적으시오)

    (내용을 적으시오)

    (내용을 적으시오)

    (내용을 적으시오)
    """)

    if st.button("🔄 처음부터"):
        st.session_state.scene = 1
        st.session_state.fear = 0
        st.rerun()
