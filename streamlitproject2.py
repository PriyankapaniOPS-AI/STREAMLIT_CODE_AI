import streamlit as st 
import pandas as pd
import numpy as np
st.title("my first streamlit app")
st.write("this is a demo app to demonstrate the basic functionalities of streamlit")
st.sidebar.header("user input features")
user_name= st.sidebar.text_input("what is your name?","streamlit user")
age= st.sidebar.slider("select your age",0,100,25)
favorite_color= st.sidebar.selectbox("what is your favorite color",["blue","green","red","pink","yellow"])
st.header(f"welcome!!{user_name}")
st.write(f"you are {age} years old and your favorite color is {favorite_color}")
st.subheader("here some random data")

data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)

if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)
else:
    st.write("Goodbye")
