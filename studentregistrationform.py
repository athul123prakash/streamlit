import streamlit as st
from datetime import date
st.title("Student Registration Form")
name=st.text_input("enter your name")
age=st.number_input("enter your age")
DOB=st.date_input("enter your DOB",min_value=date(2000,1,1),max_value=date.today(),
                  value=date.today())

email=st.text_input("enter your email")
gender=st.radio("select your gender",["Male","Female"])
courses=st.selectbox("select courses",["python","java","dotnet","testing"])
btn=st.button("submit")
if btn:
    st.write("name:"+name)
    st.write("age:"+str(age))
    st.write("DOB:"+str(DOB))
    st.write("email:"+email)
    st.write("gender:"+gender)
    st.write("courses:"+courses)