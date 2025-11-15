import streamlit as st


# 앱 제목
st.title("오늘의 기분으로 보는 명언")

# 질문
st.write("### 오늘 하루 당신의 기분을 알려주세요!")


# 세션 상태에 명언 저장 함수
def set_quote(mood: str, quote: str):
    st.session_state['mood'] = mood
    st.session_state['quote'] = quote


# 기분별 명언 사전
QUOTES = {
    '걱정': '😟 걱정은 내일의 문제를 오늘의 기쁨으로 바꾸지 못합니다. 한 걸음씩 숨을 고르세요.',
    '화남': '😡 화가 날 때는 잠시 멈추고, 말보다 행동으로 평정을 찾으세요.',
    '평온': '😌 독서할 때 당신은 항상 가장 좋은 친구와 함께 있다.',
    '기쁨': '😄 작은 기쁨이 모여 큰 날을 만듭니다. 오늘의 웃음을 소중히 하세요.',
    '만족': '😊 지금 가진 것에 감사하면, 이미 충분히 풍요롭습니다.'
}


# 5개의 버튼을 가로로 배치
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.button('걱정', on_click=set_quote, args=('걱정', QUOTES['걱정']))
with col2:
    st.button('화남', on_click=set_quote, args=('화남', QUOTES['화남']))
with col3:
    st.button('평온', on_click=set_quote, args=('평온', QUOTES['평온']))
with col4:
    st.button('기쁨', on_click=set_quote, args=('기쁨', QUOTES['기쁨']))
with col5:
    st.button('만족', on_click=set_quote, args=('만족', QUOTES['만족']))


# 클릭된 기분에 따라 명언 표시
if 'quote' in st.session_state:
    st.markdown(f"**선택한 기분:** {st.session_state.get('mood')}")
    st.info(st.session_state.get('quote'))
else:
    st.write("버튼을 눌러 명언을 확인해보세요.")

