import streamlit as st
st.title("My first streamlit app created by Priyanka")
st.write("Welcome this app calulates the square of number:")
st.header("select a number:")
number=st.slider("Pick anumber:",0,100,25)
st.subheader("result")
square_number=number * number
st.write(f"The square of {number} is {square_number}")
