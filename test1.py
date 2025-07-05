import streamlit as st

st.title("My Frontend App with Streamlit")
st.subheader("Please enter your details")

name=st.text_input("Enter your name:")
address=st.text_input("Enter your address")
gender=st.text_input("Enter your gender:")
phone=st.text_input("Enter your phone number:")
country=st.text_input("Enter country name:") 
age=st.slider("Select your age",15,30,70)
st.write(f"Your age is {age}")

if st.button("ENTER"):
   st.success(f"Welcome {name}, You have successfully registered.")
   




