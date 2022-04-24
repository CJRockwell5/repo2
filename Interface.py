import streamlit as st
st.header('Pneumonia Classification')
st.subheader('Group 5')

image_file = st.file_uploader("Upload a X-ray", type=["png","jpg","jpeg"])
if image_file is not None:
     
     # To See details
     file_details = {"filename":image_file.name, "filetype":image_file.type,
     "filesize":image_file.size}
     st.write(file_details)
     
     curret_xray = load_image(image_file)

     # To View Uploaded Image
     st.image(load_image(image_file),width=250)
