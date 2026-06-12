import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="야호",
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
    당신은 집에가기위해 골목길을 걷고있습니다. 평소에도 스산하고 무서운 분위기였지만 오늘 아침 뉴스에서본 "연쇄살인"이란 문구가 생각이나 더욱 무서운 기분이 듭니다.

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

   고양이는 하악질을 하며 도망을 칩니다.

    하지만 분명 당신이 본 스쳐지나간 잔상은 큰 성인 남성의 덩치와 비슷해보였습니다.
    """)

      if st.button("다음"):
        st.session_state.scene = 5
        st.rerun()

# -----------------------------
# 장면 5
# -----------------------------
elif st.session_state.scene == 5:

    st.title("골목길의 끝")

    st.write("""
    
    조금 전의 일은 단순한 착각이었을지도 모릅니다.

    하지만 어째서인지 뒤를 돌아볼 용기가 나지 않습니다.

    """)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("전화를 받는다"):
            st.session_state.scene = 6
            st.rerun()

    with col2:
        if st.button("무시한다"):
            st.session_state.scene = 7
            st.rerun()

# -----------------------------
# 장면 6
# -----------------------------
elif st.session_state.scene == 6:

    st.title("수상한 전화")

    st.write("""
    조심스럽게 통화 버튼을 누릅니다.

    잠시 정적이 흐릅니다.

    '......'

    아무런 소리도 들리지 않습니다.

    전화를 끊으려는 순간.

    낮고 쉰 목소리가 들려옵니다.

    '뒤를 돌아보지 마.'

    순간 온몸에 소름이 돋습니다.

    당신은 무의식적으로 걸음을 멈춥니다.

    그리고 그 목소리는 마지막 말을 남깁니다.

    '그 사람이 아직 널 보고 있어.'

    통화는 그대로 끊어져 버립니다.
    """)

    st.session_state.fear += 10

    if st.button("뒤를 돌아본다"):
        st.session_state.scene = 8
        st.rerun()

# -----------------------------
# 장면 7
# -----------------------------
elif st.session_state.scene == 7:

    st.title("무시했다")

    st.write("""
    당신은 괜한 장난전화라고 생각하며 휴대전화를 다시 주머니에 넣습니다.

    하지만 이상합니다.

    전화는 끊겼는데도 휴대전화의 진동은 계속되고 있습니다.

    화면을 확인합니다.

    이번에는 문자메시지 하나가 도착해 있습니다.

    [뒤를 돌아보지 마.]

    단 한 줄의 메시지.

    보낸 사람은 확인되지 않습니다.

    당신의 심장이 점점 빠르게 뛰기 시작합니다.
    """)

    st.session_state.fear += 5

    if st.button("뒤를 돌아본다"):
        st.session_state.scene = 8
        st.rerun()

# -----------------------------
# 장면 8
# -----------------------------
elif st.session_state.scene == 8:

    st.title("누군가 있다")

    st.write("""
    결국 참지 못하고 뒤를 돌아봅니다.

    텅 빈 골목길.

    아무도 없습니다.

    하지만 분명 무언가가 있었습니다.

    당신은 확신할 수 있습니다.

    그 순간.

    골목길 벽에 붙어있는 거울 조각이 눈에 들어옵니다.

    거울 속에는 당신의 모습이 비칩니다.

    그리고 그 뒤.

    검은 후드를 뒤집어쓴 사람이 서 있습니다.

    놀라 다시 뒤를 돌아보지만 아무도 없습니다.

    다시 거울을 봅니다.

    여전히 그 사람은 당신의 바로 뒤에 서 있습니다.
    """)

    st.session_state.fear += 15

    col1, col2 = st.columns(2)

    with col1:
        if st.button("도망친다"):
            st.session_state.scene = 9
            st.rerun()

    with col2:
        if st.button("거울을 부순다"):
            st.session_state.scene = 10
            st.rerun()

# -----------------------------
# 장면 9
# -----------------------------
elif st.session_state.scene == 9:

    st.title("질주")

    st.write("""
    당신은 미친 듯이 달리기 시작합니다.

    숨이 턱 끝까지 차오릅니다.

    뒤에서 누군가 따라오는 것 같은 발소리가 들립니다.

    하지만 감히 확인할 수 없습니다.

    몇 분을 달렸을까.

    밝은 대로변이 보입니다.

    사람들의 모습이 보이자 겨우 안도의 한숨을 내쉽니다.
    """)

    if st.button("계속"):
        st.session_state.scene = 11
        st.rerun()

# -----------------------------
# 장면 10
# -----------------------------
elif st.session_state.scene == 10:

    st.title("깨진 거울")

    st.write("""
    근처에 있던 돌을 집어 거울을 향해 던집니다.

    쨍그랑!

    거울이 산산조각 나며 깨집니다.

    그런데 깨진 조각 속 모든 반사면에서

    검은 후드의 남자가 동시에 당신을 바라보고 있습니다.

    그리고 조각들은 하나둘 검게 물들기 시작합니다.
    """)

    st.session_state.fear += 20

    if st.button("계속"):
        st.session_state.scene = 11
        st.rerun()

# -----------------------------
# 장면 11
# -----------------------------
elif st.session_state.scene == 11:

    if st.session_state.fear >= 40:

        st.title("배드 엔딩")

        st.write(f"""
        당신은 집에 도착했지만 끝내 잠들지 못했습니다.

        창밖에서 누군가가 지켜보는 기분이 들었기 때문입니다.

        현재 공포심 : {st.session_state.fear}

        당신은 끝내 진실을 알지 못했습니다.
        """)

    else:

        st.title("노멀 엔딩")

        st.write(f"""
        우여곡절 끝에 집에 도착했습니다.

        오늘 있었던 일은 모두 우연이었을까요?

        아니면 정말 누군가가 당신을 노리고 있었던 걸까요?

        현재 공포심 : {st.session_state.fear}

        진실은 아직 밝혀지지 않았습니다.
        """)

    if st.button("처음부터"):
        st.session_state.scene = 1
        st.session_state.fear = 0
        st.rerun()
