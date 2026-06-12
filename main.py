import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="미연시 게임",
    layout="wide"
)

# -----------------------------
# 다크 테마
# -----------------------------
st.markdown("""
<style>

/* 전체 배경 */
.stApp {
    background-color: #111111;
}

/* 본문 글씨 */
html, body, [class*="css"] {
    color: white;
}

/* 사이드바 */
[data-testid="stSidebar"] {
    background-color: #111111;
}

/* 사이드바 글씨 */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* 버튼 */
.stButton > button {
    width: 100%;
    height: 60px;
    background-color: #333333;
    color: white;
    border: 1px solid #555555;
    border-radius: 10px;
    font-size: 18px;
}

.stButton > button:hover {
    background-color: #555555;
    color: white;
}

/* Metric 글씨 */
[data-testid="stMetricValue"] {
    color: white;
}

[data-testid="stMetricLabel"] {
    color: white;
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
    st.title("상태창")
    st.metric("공포심", st.session_state.fear)

# -----------------------------
# 장면 1
# -----------------------------
if st.session_state.scene == 1:

    st.title("프롤로그")

    st.write("""
    당신은 집에가기위해 골목길을 걷고있습니다. 평소에도 스산하고 무서운 분위기였지만 오늘 아침 뉴스에서본 "연쇠살인"이란 문구가 생각이나 더욱 무서운 기분이 듭니다.

    어두운 골목길 안쪽에서 부스럭거리는 소리와 함께 무언가가 스쳐지나간것같은 잔상이 보입니다.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("누구냐고 소리치기"):
            st.session_state.scene = 2
            st.rerun()

    with col2:
        if st.button("도망치기"):
            st.session_state.fear += 10
            st.session_state.scene = 3
            st.rerun()

    with col3:
        if st.button("무시하고 걷기"):
            st.session_state.scene = 4
            st.rerun()

# -----------------------------
# 장면 2
# -----------------------------
elif st.session_state.scene == 2:

    st.title("누구냐고 소리쳤다")

    st.write("""
    소리를 치자 안쪽에서 놀란 고양이의 우다다 거리는 소리와 함께 근처에 살던 주민이 시끄럽다며 화를 냅니다. 놀란가슴을 쓸어내리며 다시 골목길을 걸어갑니다

   꺼져가던 가로등에서 불빛이 천천히 들어옵니다.
    """)

    if st.button("다음"):
        st.session_state.scene = 5
        st.rerun()

# -----------------------------
# 장면 3
# -----------------------------
elif st.session_state.scene == 3:

    st.title("도망쳤다")

    st.write("""
    공포심이 10 증가하였습니다.

    당신은 공포심에 못이겨 골목길을 빠져나왔습니다.

    오늘같은날은 어쩔 수 없다며 눈물을 머금고 택시를 부릅니다.

    """)

    if st.button("다음"):
        st.session_state.scene = 5
        st.rerun()

# -----------------------------
# 장면 4
# -----------------------------
elif st.session_state.scene == 4:

    st.title("무시하고 걸었다")

    st.write("""
    무시하고 걸어가자 보인건 쓰레기통을 뒤지던 고양이였습니다.

   고양이는하악질을 하며 도망을 칩니다.

    하지만 분명 당신이 본 스쳐지나간 잔상은 큰 성인 남성의 덩치와 비슷해보였습니다.
    """)

    if st.button("다음"):
        st.session_state.scene = 5
        st.rerun()

# -----------------------------
# 장면 5
# -----------------------------
elif st.session_state.scene == 5:

    st.title("다음 이야기")

    st.write("""
    내용을 적으시오

    내용을 적으시오

    내용을 적으시오

    내용을 적으시오
    """)

    if st.button("처음부터"):
        st.session_state.scene = 1
        st.session_state.fear = 0
        st.rerun()
