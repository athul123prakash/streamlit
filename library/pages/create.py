import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete

st.title("Add New Book Records")
title=st.text_input("Enter the title")
author=st.text_input("Enter the name")
price=st.number_input("Enter the price")
page=st.number_input("Enter the page")
language=st.text_input("Enter the language")
btn=st.button("Add")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.create(title,author,price,page,language)
    st.success("Records created successfully")


