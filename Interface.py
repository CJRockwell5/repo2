import streamlit as st
st.header('Pneumonia Classification')
st.subheader('Group 5')

uploaded_file = st.file_uploader("Upload a X-ray", type=["png","jpg","jpeg"])
if uploaded_file is not None:
     input_image = uploaded_file.getvalue()
     
     # To See details
     file_details = {"filename":image_file.name, "filetype":image_file.type,
     "filesize":image_file.size}
     st.write(file_details)

     # To View Uploaded Image
     st.image(load_image(image_file),width=250)
