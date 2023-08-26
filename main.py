from dotenv import load_dotenv
from langchain.llms import OpenAI
import streamlit as st

load_dotenv()
lim = OpenAI()


st.title("AI 초3 일기장")
st.write('ChatGPA로 일기쓰기 :sunglasses:')

diary_title = st.text_input('일기 주제를 제시해주세요.')
st.write('일기 주제는.....' + diary_title + '!!!')

if st.button('일기 작성하기'):
    with st.spinner('일기 작성중......'):
        result = lim.predict(diary_title + "에 대한 초등학교 3학년이 작성한 일기 써줘. 50자정도만!")
        st.write(result)
