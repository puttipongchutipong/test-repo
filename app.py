import streamlit as st
import pandas as pd
import numpy as np

# ตั้งค่าเว็บของเราได้ เช่น ชื่อ ไอคอน รูปแบบ ฯลฯ
st.set_page_config(
    page_title="Resources",
    page_icon="🕹️",
    layout="wide",
    initial_sidebar_state="expanded")


# Hello World
st.write("Hello World!")
x = st.text_input("What is your name?")
st.write(f"Hello {x}!")

# Button
st.button("Simple Button", type="primary")

if st.button("Click me!"):
    st.write("You clicked me!")

# Checkbox
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

# Selectbox
option = st.selectbox('Which major do you like best?', ['CO', 'CI'])
st.write("You've selected: ", option)

# แสดงข้อมูลจาก dataframe
df = pd.read_csv('data.csv')
st.dataframe(df) # st.write(df)
# st.table(df)

from numpy.random import default_rng as rng
# ตัวอย่างกราฟแท่ง จาก Docs
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.bar_chart(df)

# ตัวอย่างกราฟเส้น จาก Docs
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.line_chart(df)

# Column Layout
col1, col2, col3 = st.columns(3)

col1.header("Debian")
col1.image("images/debian.png", width=200)

col2.header("Fedora")
col2.image("images/fedora.png", width=200)

col3.header("Kali")
col3.image("images/kali.png", width=200)

# หรือใช้กับคำว่า "with" ได้
with col1:
    st.header("Redhat")
    st.image("images/redhat.png", width=200)
with col3:
    st.header("Ubuntu")
    st.image("images/ubuntu.png", width=200)


# Container Layout
container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")

container.write("This is inside too")

# อัพโหลดไฟล์
file = st.file_uploader("Upload a CSV")

# สามารถเขียนโค้ดเพื่อ extract ข้อมูลออกมาได้
if (file):
    df = pd.read_csv(file)
    st.write(df)
    df = df[['age', 'major', 'year']]
    st.bar_chart(df, x='year', y='age', color='major', stack=False)