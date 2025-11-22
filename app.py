import streamlit as st

st.write("Hello World!")
x = st.text_input("What is your name?")
st.button("Click me!")
st.write(f"Hello {x}!")

import pandas as pd

df = pd.read_csv('data.csv')
st.write(df)

file = st.file_uploader("Upload a CSV")

from numpy.random import default_rng as rng
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.bar_chart(df)

st.set_page_config(
    page_title="Dashboard Template",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

# if (file):
    # df = pd.read_csv(file)
    # st.write(df)
    # df = df[['age', 'major', 'year']]
    # st.bar_chart(df, x='year', y='age', color='major', stack=False)