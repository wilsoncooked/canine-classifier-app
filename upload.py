import streamlit as st
import requests
from streamlit_cropperjs import st_cropperjs

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    
st.title("Canine Classifier 🐶")
st.write("## Identify your dogs breed! :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog:")

container = st.empty()
col1, col2 = container.columns(2)
cam = col1.camera_input("Take a picture of your dog", label_visibility="visible")
upload = col2.file_uploader("Upload an image of your dog", type=["png", "jpg", "jpeg"])

if upload is not None:
    if upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        st.session_state.upload = upload.read()
        
        st.switch_page("/pages/crop.py")
        
if cam is not None:
    if cam.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        st.session_state.upload = cam.read()
        st.switch_page("/pages/crop.py")
