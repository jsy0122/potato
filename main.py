import streamlit as st

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="공포 선택지 게임",
    layout="wide"
)

# -----------------------------------
# 검은 배경
# -----------------------------------
st.markdown("""
<style>
.stApp{
    background-color:black;
    color:white;
}

.story-box{
    background-color:#111111;
    border:1px solid #444444;
    padding:20px;
    border-radius:10px;
    color:white;
    font-size:20px;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# 세션 상태
# -----------------------------------
if "fear" not in st.session_state:
    st.session_state.fear = 0

if "scene" not in st.session_state:
    st.session_state.scene = "start"

# -----------------------------------
# 사이드바
# -----------------------------------
with st.sidebar:
    st.title("공포심")

    st.metric(
        label="현재 공포심",
        value=st.session_state.fear
    )

    st.markdown("---")

    st.subheader("아이템")
    st.write("아직 없음")

# -----------------------------------
# 시작 장면
# -----------------------------------
if st.session_state.scene == "start":

    st.markdown("""
    <div class="story-box">
    글을 적어주세요
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("1. 누구냐고 소리를 지르기"):
            st.session_state.scene = "shout"
            st.rerun()

    with col2:
        if st.button("2. 도망치기"):
            st.session_state.fear += 10
            st.session_state.scene = "run"
            st.rerun()

    with col3:
        if st.button("3. 무시하고 골목으로 들어가기"):
            st.session_state.scene = "alley"
            st.rerun()

# -----------------------------------
# 1번 장면
# -----------------------------------
elif st.session_state.scene == "shout":

    st.markdown("""
    <div class="story-box">
    1번 선택 후 장면 글을 적어주세요
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------
# 2번 장면
# -----------------------------------
elif st.session_state.scene == "run":

    st.markdown("""
    <div class="story-box">
    공포심 +10

    2번 선택 후 장면 글을 적어주세요
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------
# 3번 장면
# -----------------------------------
elif st.session_state.scene == "alley":

    st.markdown("""
    <div class="story-box">
    3번 선택 후 장면 글을 적어주세요
    </div>
    """, unsafe_allow_html=True)
