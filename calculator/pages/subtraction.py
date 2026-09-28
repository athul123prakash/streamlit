import streamlit as st
st.title("Subtraction")
num1=st.number_input("enter number1",min_value=0)
print(num1)
num2=st.number_input("enter number2",min_value=0)
print(num2)
btn=st.button("subtract")
if btn:
     result=num1+num2
     print(result)
     st.write("Difference is",result)