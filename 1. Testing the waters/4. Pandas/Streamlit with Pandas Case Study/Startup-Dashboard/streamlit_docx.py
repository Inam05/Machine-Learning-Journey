import streamlit as st
import pandas as pd
import time

# text utilities
st.title("Startup Dashboard")
st.header('This is a header')
st.subheader('This is a subheader')

st.write('This is a normal text')
st.markdown("""
### My Favorite Movies
- Baghban
- Kick
""")

st.code("""
def foo(input):
    return foo**2

x = foo(2)
""")

st.latex("x^2 + y^2 = 0")


df = pd.DataFrame({
    'Name':['Inam','Ukasha','Aniqa'],
    'Marks':[60,70,60],
    'Package':[10,13,12]
})

st.dataframe(df)

st.metric('Revenue',"Rs 3L",'3%')
st.json({
    'Name':['Inam','Ukasha','Aniqa'],
    'Marks':[60,70,60],
    'Package':[10,13,12]
})

st.sidebar.title("Sidebar")
col1, col2 = st.columns(2)
with col1:
    st.dataframe(df)

with col2:
    st.latex("x^2 + y^2 = 0")
    st.latex("x^2 + y^2 + 2 = 0")

st.error("Login Failed")
st.success("Login Successfuly")
st.info("Login")

bar = st.progress(0)
for i in range(1,101):
    time.sleep(0.1)
    # bar.progress(i)

email = st.text_input('Enter your email:')
num = st.number_input('Enter Age :')
st.date_input('Input data: ')

#########
email = st.text_input("Enter email:")
password = st.text_input("Enter password: ")
gender = st.selectbox('Select gender',['Male','Female','Others'])

btn = st.button("Do login")

if btn:
    if email == "inam@gmail.com" and password == '1234':
        st.success("login successful!")
        st.balloons()
        st.write(gender)
    else:
        st.error("Login failed!")

#############

file = st.file_uploader('Upload a csv file')
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())