import streamlit as st
from streamlit_cropperjs import st_cropperjs

st.set_page_config(layout='wide',initial_sidebar_state='collapsed')

if 'upload' not in st.session_state:
    st.switch_page("upload.py")

st.title("Canine Classifier 🐶")
st.write("## Identify your dogs breed! :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog:")

container = st.empty()
def select_borders(upload):
    st.write("Please draw borders around your dog")
    cropped_pic = st_cropperjs(pic=st.session_state.upload, btn_text="Identify my dog!")
    if cropped_pic:
        st.session_state.cropped_pic = cropped_pic
        container.empty()
        st.switch_page("/pages/results.py")

try:
    select_borders(st.session_state.upload)
except Exception as e:
    st.switch_page("upload.py")


if st.button("🐕 Rerun", use_container_width=True):
    st.switch_page("upload.py")
