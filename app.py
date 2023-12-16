import os

import streamlit as st

from embedchain import Pipeline as App

app = App()
app.add("https://en.wikipedia.org/wiki/Elon_Musk")


def get_answer(question):
    print(f"Received question {question}")
    return app.query(question)


st.title('Qna App')
st.write('Type something and click send to get answer!')

input_text = st.text_input("Type something here...")
if st.button('Send'):
    result = get_answer(input_text)
    st.write(result)
