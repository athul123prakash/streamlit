import streamlit as st
st.title("Read all Book Records")

from librarydb import BookListCreateRetrieveUpdateDelete
c=BookListCreateRetrieveUpdateDelete()
record=c.list()
# print(record)
st.table(record)

