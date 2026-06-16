import streamlit as st

# =========================
# 초기화
# =========================

if "fear" not in st.session_state:
    st.session_state.fear = 0
    st.session_state.money = 30000
    st.session_state.actions = 0
    st.session_state.day = 1

    st.session_state.inventory = []
    st.session_state.capacity = 10

    st.session_state.taxi = 2
    st.session_state.alley_passed = False

# =========================
# 함수
# =========================

def add_fear(amount):
    st.session_state.fear += amount

    if st.session_state.fear >= 100:
        st.error("💀 극심한 공포 엔딩")
        st.stop()

def spend_action():
    st.session_state.actions += 1

    if st.session_state.actions >= 10:
        nightmare()

def nightmare():
    st.warning("악몽이 시작된다...")

    add_fear(25)

    st.session_state.day += 1
    st.session_state.actions = 0
    st.session_state.alley_passed = False

def add_item(item):
    if len(st.session_state.inventory) < st.session_state.capacity:
        st.session_state.inventory.append(item)
    else:
        st.error("가방이 가득 찼다.")

# =========================
# 사이드바
# =========================

with st.sidebar:

    st.title("상태")

    st.write(f"📅 Day {st.session_state.day}")
    st.write(f"😨 공포심 : {st.session_state.fear}/100")
    st.write(f"💰 돈 : {st.session_state.money}원")
    st.write(f"🎒 수납 : {len(st.session_state.inventory)}/{st.session_state.capacity}")
    st.write(f"🚕 택시 : {st.session_state.taxi}회")

    st.write("---")

    st.write("소지품")

    for item in st.session_state.inventory:
        st.write(f"- {item}")

# =========================
# 메인
# =========================

st.title("골목의 끝")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "골목",
    "편의점",
    "백화점",
    "알바",
    "루트"
])

# =========================
# 골목
# =========================

with tab1:

    st.header("골목")

    st.write("[글을 적으시오]")

    if st.button("골목 통과"):

        st.session_state.alley_passed = True

        add_fear(5)

        spend_action()

        st.success("골목을 지나갔다.")

# =========================
# 편의점
# =========================

with tab2:

    st.header("편의점")

    if st.button("생수 구매 (1000원)"):

        if st.session_state.money >= 1000:

            st.session_state.money -= 1000
            st.session_state.fear = max(
                0,
                st.session_state.fear - 5
            )

    if st.button("초콜릿 구매 (2000원)"):

        if st.session_state.money >= 2000:

            st.session_state.money -= 2000
            st.session_state.fear = max(
                0,
                st.session_state.fear - 10
            )

    if st.button("과자 구매 (3000원)"):

        if st.session_state.money >= 3000:

            st.session_state.money -= 3000
            st.session_state.fear = max(
                0,
                st.session_state.fear - 15
            )

    if st.button("손전등 구매 (8000원)"):

        if st.session_state.money >= 8000:

            st.session_state.money -= 8000

            add_item("손전등")

# =========================
# 백화점
# =========================

with tab3:

    st.header("백화점")

    if st.button("작은 가방 구매 (20000원)"):

        if st.session_state.money >= 20000:

            st.session_state.money -= 20000
            st.session_state.capacity = 15

    if st.button("큰 가방 구매 (50000원)"):

        if st.session_state.money >= 50000:

            st.session_state.money -= 50000
            st.session_state.capacity = 20

    if st.button("버려진 가방 줍기"):

        st.session_state.capacity = max(
            st.session_state.capacity,
            15
        )

        add_fear(5)

        add_item("낡은 사진")

# =========================
# 알바
# =========================

with tab4:

    st.header("알바")

    if st.button("알바하기"):

        st.session_state.money += 5000

        st.info("피곤하다... 집으로 돌아가 잠든다.")

        nightmare()

# =========================
# 루트
# =========================

with tab5:

    st.header("루트")

    route = st.selectbox(
        "선택",
        [
            "루트1 목격자",
            "루트2 실종자 파일",
            "루트3 거울 속 사람",
            "루트4 검은 우산",
            "루트5 진엔딩",
            "루트6 시선"
        ]
    )

    if route == "루트1 목격자":

        st.write("[글을 적으시오]")

    elif route == "루트2 실종자 파일":

        st.write("[글을 적으시오]")

    elif route == "루트3 거울 속 사람":

        st.write("[글을 적으시오]")

    elif route == "루트4 검은 우산":

        st.write("[글을 적으시오]")

    elif route == "루트5 진엔딩":

        st.write("[글을 적으시오]")

    elif route == "루트6 시선":

        st.write("[글을 적으시오]")
