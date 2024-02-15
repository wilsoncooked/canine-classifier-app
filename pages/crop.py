import streamlit as st
from streamlit_cropperjs import st_cropperjs

st.set_page_config(
    page_title="Canine Classifier 🐶",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="collapsed"
)
if 'upload' not in st.session_state:
    st.switch_page("upload.py")


# st.session_state.cropped_pic = st.session_state.upload
# st.switch_page("/pages/results.py")

left_co, right_co = st.columns(2)


def select_borders(upload):
    with left_co:
        st.write("Please draw borders around your dog")
        cropped_pic = st_cropperjs(pic=upload, btn_text="Identify dog" )
        if cropped_pic:
                st.session_state.cropped_pic = cropped_pic
                st.switch_page("/pages/results.py")


try:
    select_borders(st.session_state.upload)
except Exception as e:
    st.switch_page("upload.py")


b1 = st.columns(3)
with b1[0]:
    if st.button("🐕 Rerun", use_container_width=True):
        st.switch_page("upload.py")
