import streamlit as st
from streamlit_cropperjs import st_cropperjs

st.set_page_config(
    page_title="Canine Classifier 🐶",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="collapsed"
)
with open("styles/main.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
if 'upload' not in st.session_state:
    st.switch_page("upload.py")

row1 = st.columns(2)
with row1[0]:
    st.title("Canine Classifier 🐶")

# st.session_state.cropped_pic = st.session_state.upload
# st.switch_page("/pages/results.py")

st.write("")

def select_borders(upload):
    st.write("Draw borders around your dog")
    cropped_pic = st_cropperjs(pic=upload, btn_text="Identify dog 🐶", key='cropper' )
    if cropped_pic:
            st.session_state.cropped_pic = cropped_pic
            st.switch_page("/pages/results.py")


try:
    select_borders(st.session_state.upload)
except Exception as e:
    st.switch_page("upload.py")
