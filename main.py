import streamlit as st
import time

st.title("EF Bot")

user_question = st.text_input("Ask a question:")

if st.button("Get Response"):
    st.write("You:", user_question)
    with st.spinner("Generating response..."):
        answer = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        time.sleep(2)
    st.success("***EF Bot:*** " + answer)
    st.write("**Source Document 1:**")
    st.write(answer)
    st.write("**Source Document 2:**")
    st.write(answer)
    st.write("**Source Document 3:**")
    st.write(answer)