import streamlit as st

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="공포 선택지 게임",
    layout="wide"
)

# -----------------------------------
# 스타일
# -----------------------------------
st.markdown("""
<style>
.stApp{
    background-color:black;
    color:white;
}

.story-box{
    background-color:#111111;
    border:1px solid #333333;
    padding:18px;
    border-radius:8px;
    color:white;
    font-size:17px;
    line-height:1.8;
    margin-bottom:20px;
}

section[data-testid="stSidebar"]{
    background-color:#0a0a0a;
}

.stButton > button{
    width:100%;
    background-color:#1a1a1a;
    color:white;
    border:1px solid #444444;
}

.stButton > button:hover{
    background-color:#2a2a2a;
    border:1px solid #666666;
}

.fear-text{
    color:#ff3333;
    font-size:24px;
    font-weight:bold;
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

    st.markdown(
        f'<p class="fear-text">공포심 : {st.session_state.fear}</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.write("아이템")
    st.write("없음")

# -----------------------------------
# 시작 장면
# -----------------------------------
if st.session_state.scene == "start":

    st.markdown("""
    <div class="story-box">
    당신은 어두운 골목길을 걷고있습니다. 오늘 아침에 본 "연쇄살인사건" 이라는 뉴스를 봐서인지 오늘따라 골목길이 스산합니다.
    걸어가던중 골목 깊은곳에서 쿠당탕거리는 소리와 함께 어떠한 잔상이 스쳐지나간것 같습니다.
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
    쓰레기통속에 있던 고양이가 깜짝놀라서 도망칩니다. 그 소리에 주변에 살던 인근주민들이 시끄럽다며 화를냅니다.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="story-box">
    하지만 분명 당신이 본 잔상은 고양이가 아니라 성인 남성에 흡사한 덩치였습니다...
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("선택지 1"):
            st.session_state.scene = "scene1"

    with col2:
        if st.button("선택지 2"):
            st.session_state.scene = "scene2"

    with col3:
        if st.button("선택지 3"):
            st.session_state.scene = "scene3"

# -----------------------------------
# 2번 장면
# -----------------------------------
elif st.session_state.scene == "run":

    st.markdown("""
    <div class="story-box">
    공포심 +10

    당신은 너무 무서워서 골목을 빠져나오기로 했습니다. 
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="story-box">
    오늘은 어쩔 수 없다며 생각을 한 후 택시를 부르기로 했습니다.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("선택지 4"):
            st.session_state.scene = "scene4"

    with col2:
        if st.button("선택지 5"):
            st.session_state.scene = "scene5"

    with col3:
        if st.button("선택지 6"):
            st.session_state.scene = "scene6"

# -----------------------------------
# 3번 장면
# -----------------------------------
elif st.session_state.scene == "alley":

    st.markdown("""
    <div class="story-box">
    골목 안쪽엔 취객 한명이 쓰러져 있습니다. 취객이 넘어지며 큰 소리가 난 것 같습니다.
    
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="story-box">
     그 취객의 옆을 지나쳐 가자  매우 심한 악취에 인상이 찌푸려집니다
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("선택지 7"):
            st.session_state.scene = "scene7"

    with col2:
        if st.button("선택지 8"):
            st.session_state.scene = "scene8"

    with col3:
        if st.button("선택지 9"):
            st.session_state.scene = "scene9"

# -----------------------------------
# 이후 장면들
# -----------------------------------
elif st.session_state.scene.startswith("scene"):

    st.markdown("""
    <div class="story-box">
    글을 입력하세요
    </div>
    """, unsafe_allow_html=True)
