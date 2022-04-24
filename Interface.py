import streamlit as st
st.header('Pneumonia Classification')
st.subheader('Group 5')

uploaded_file = st.file_uploader("Choose a X-ray")
if uploaded_file is not None:
     input_image = uploaded_file.getvalue()
