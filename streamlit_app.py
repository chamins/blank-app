import streamlit as st  # 1. Streamlit 라이브러리 import
import pandas as pd  # 2. 데이터 처리를 위한 pandas 라이브러리
import numpy as np  # 3. 수치 계산을 위한 numpy 라이브러리

# 1. 페이지 제목 설정
st.title("🎈 Streamlit 요소 예시 페이지")  # 페이지의 주요 제목

# 2. 일반 텍스트 요소
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)  # 기본 텍스트 및 마크다운 지원

# 3. 헤더와 서브헤더
st.header("📋 텍스트 요소들")  # 섹션 헤더
st.subheader("부제목 예시")  # 부제목
st.text("일반 텍스트: 마크다운을 지원하지 않는 순수 텍스트입니다.")  # 순수 텍스트
st.markdown("**마크다운** 텍스트: *이탤릭*, ~~취소선~~, `코드`, 링크 등을 지원합니다.")  # 마크다운 지원
st.caption("캡션: 작은 텍스트로 설명을 추가할 때 사용됩니다.")  # 작은 글씨 캡션

# 4. 데이터 시각화 요소
st.header("📊 데이터 시각화")
# DataFrame 표시
sample_data = pd.DataFrame({
    "이름": ["Alice", "Bob", "Charlie"],
    "나이": [25, 30, 35],
    "점수": [85, 90, 78]
})
st.write("**DataFrame 표시:**")
st.dataframe(sample_data)  # 대화형 DataFrame 표시

st.write("**Table (정적 테이블):**")
st.table(sample_data)  # 정적 테이블 표시

# 메트릭 표시
col1, col2, col3 = st.columns(3)  # 3개의 열 생성
with col1:
    st.metric(label="온도", value="25°C", delta="2°C")  # 메트릭 카드
with col2:
    st.metric(label="습도", value="65%", delta="-5%")
with col3:
    st.metric(label="기압", value="1013 hPa", delta="3 hPa")

# 5. 입력 요소
st.header("🎛️ 입력 요소")

# 텍스트 입력
user_name = st.text_input("이름을 입력하세요:")  # 한 줄 텍스트 입력
if user_name:
    st.write(f"안녕하세요, {user_name}님!")

# 텍스트 영역
user_comment = st.text_area("의견을 작성하세요:")  # 여러 줄 텍스트 입력
if user_comment:
    st.write("입력하신 의견:", user_comment)

# 숫자 입력
age = st.number_input("나이를 입력하세요:", min_value=0, max_value=120, value=25)  # 숫자 입력
st.write(f"입력된 나이: {age}")

# 슬라이더
slider_value = st.slider("슬라이더로 값을 선택하세요:", 0, 100, 50)  # 슬라이더
st.write(f"슬라이더 값: {slider_value}")

# 선택 상자
selected_option = st.selectbox("옵션을 선택하세요:", ["옵션 1", "옵션 2", "옵션 3"])  # 드롭다운 선택
st.write(f"선택된 옵션: {selected_option}")

# 멀티셀렉트
selected_options = st.multiselect("여러 옵션을 선택하세요:", ["A", "B", "C", "D"])  # 다중 선택
st.write(f"선택된 항목: {selected_options}")

# 라디오 버튼
radio_choice = st.radio("하나를 선택하세요:", ("예", "아니오", "잘 모르겠어요"))  # 라디오 버튼
st.write(f"선택: {radio_choice}")

# 체크박스
is_agreed = st.checkbox("약관에 동의합니다.")  # 체크박스
if is_agreed:
    st.write("✅ 약관에 동의했습니다.")

# 6. 버튼과 상호작용
st.header("🔘 버튼 및 상호작용")

if st.button("클릭해보세요!"):  # 일반 버튼
    st.write("🎉 버튼을 클릭했습니다!")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("버튼 1"):
        st.success("✅ 성공!")  # 성공 메시지
with col2:
    if st.button("버튼 2"):
        st.info("ℹ️ 정보 메시지")  # 정보 메시지
with col3:
    if st.button("버튼 3"):
        st.warning("⚠️ 경고 메시지")  # 경고 메시지

# 에러 메시지 표시
try:
    if st.button("에러 테스트"):
        st.error("❌ 에러가 발생했습니다!")  # 에러 메시지
except:
    pass

# 7. 차트 및 그래프
st.header("📈 차트")

# 라인 차트
chart_data = pd.DataFrame(
    np.random.randn(20, 3),  # 20행, 3열의 난수
    columns=["A", "B", "C"]
)
st.line_chart(chart_data)  # 라인 차트

# 바 차트
bar_data = pd.DataFrame({
    "범주": ["A", "B", "C", "D"],
    "값": [10, 24, 36, 18]
})
st.bar_chart(bar_data.set_index("범주"))  # 바 차트

# 8. 레이아웃 요소
st.header("📐 레이아웃")

# 컬럼 레이아웃
col1, col2 = st.columns(2)
with col1:
    st.write("**왼쪽 컬럼**")
    st.write("컬럼을 사용하여 요소를 나란히 배치할 수 있습니다.")
with col2:
    st.write("**오른쪽 컬럼**")
    st.write("이렇게 여러 컬럼으로 레이아웃을 구성할 수 있습니다.")

# 익스팬더 (접을 수 있는 섹션)
with st.expander("자세히 보기"):  # 접을 수 있는 상자
    st.write("이 내용은 처음에는 숨겨져 있고, 버튼을 클릭하면 표시됩니다.")
    st.write("토글 가능한 섹션에 추가 정보를 담을 때 유용합니다.")

# 컨테이너
with st.container():  # 그룹화된 섹션
    st.write("컨테이너로 관련된 요소들을 그룹화할 수 있습니다.")
    st.write("이렇게 구조를 정리하면 코드가 깔끔해집니다.")

# 9. 파일 업로드
st.header("📁 파일 처리")
uploaded_file = st.file_uploader("파일을 업로드하세요:", type=["csv", "txt"])  # 파일 업로드
if uploaded_file is not None:
    st.write("파일이 업로드되었습니다!")
    st.write(f"파일명: {uploaded_file.name}")

# 10. 진행 상황 표시
st.header("⏳ 진행 상황 표시")
progress_bar = st.progress(0)  # 진행 바 초기화
status_text = st.empty()  # 상태 텍스트 표시 영역

# 진행 상황 업데이트 시뮬레이션
import time
for i in range(101):
    progress_bar.progress(i)  # 진행 바 업데이트
    status_text.text(f"진행률: {i}%")  # 상태 텍스트 업데이트
    if i == 100:
        status_text.text("✅ 완료되었습니다!")
        break
    time.sleep(0.01)  # 0.01초 대기

# 11. 사이드바 요소
st.sidebar.title("🔧 사이드바")  # 사이드바 제목
sidebar_option = st.sidebar.radio("메뉴 선택:", ["홈", "설정", "정보"])  # 사이드바 라디오
st.sidebar.write(f"선택된 메뉴: {sidebar_option}")

# 12. 피드백 및 마무리
st.header("✨ 마무리")
st.success("이것이 Streamlit에서 사용할 수 있는 주요 요소들입니다!")  # 성공 메시지
