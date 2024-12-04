import streamlit as st
import time

st.title("Streamlit basics")
st.write("hello world")

col1, col2 = st.columns(2)

with col1:
    st.write("列１がここに表示されます")

with col2:
    st.write("列２がここに表示されます")

st.sidebar.write("hello world")

st.text_input("ここに文字が入力できます。")

slider_text = st.slider("スライダーで数字を決定できます", 0, 100, 50)

st.button("ボタン")

x = st.empty()
bar = st.progress(0)

for i in range (100):
    time.sleep(0.1)
    x.text(i)
    bar.progress(i)
    i += 1

st.selectbox("選んでください", ["choice1", "choice2", "choice3"])

output_text = "この文字がダウンロードされます"

st.download_button(label="記事内容 Download",
                data=output_text,
                file_name="out_put.text",
                mime="text/plain")


file_upload = st.file_uploader("ここに音声認識したファイルをアップロードしてください", type=["png", "jpg"])

if (file_upload != None):
    st.image(file_upload)


import numpy as np
import pandas as pd

def rand_df(r=10, c=5):
    df = pd.DataFrame(
        np.random.randn(r, c),
        columns=('col %d' % i for i in range(c)))
    return df
    
dataframe = rand_df(r=10, c=3)

st.dataframe(dataframe.head(n=3))
st.line_chart(dataframe)
