import streamlit as st
from streamlit_cropperjs import st_cropperjs
st.title("Canine Classifier 🐶")
st.write("## Identify your dogs breed! :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog:")
def select_borders(upload):
    st.write("Please draw borders around your dog")
    #upload = upload.read()
    cropped_pic = st_cropperjs(pic=upload, btn_text="Identify my dog!")
    if cropped_pic:
        st.session_state.cropped_pic = cropped_pic
        st.switch_page("/pages/results.py")
        
select_borders(st.session_state.upload)

