import streamlit as st
from PIL import Image

st.header('Pneumonia Classification')
st.subheader('Group 5')

image_file = st.file_uploader("Upload a X-ray", type=["png","jpg","jpeg"])
if image_file is not None:
     
     # To See details
     file_details = {"filename":image_file.name, "filetype":image_file.type,
     "filesize":image_file.size}
     
     curret_xray = Image.open(image_file)

     # To View Uploaded Image
     st.image(curret_xray, width=250)
