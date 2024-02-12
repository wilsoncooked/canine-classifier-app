import streamlit as st
from streamlit_cropperjs import st_cropperjs

st.set_page_config(layout='wide',initial_sidebar_state='collapsed')
a, b, c = st.columns(3)
a.page_link(page="upload.py", label="Start", icon="🏠", use_container_width=True)
b.page_link(page="/pages/crop.py", label="Crop", icon="✂", use_container_width=True)
c.page_link(page="/pages/results.py", label="Results", icon="💡", use_container_width=True)
   
st.title("Canine Classifier 🐶")
st.write("## Identify your dogs breed! :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog:")
def select_borders(upload):
    st.write("Please draw borders around your dog")
    cropped_pic = st_cropperjs(pic=upload, btn_text="Identify my dog!")
    if cropped_pic:
        st.session_state.cropped_pic = cropped_pic
        st.switch_page("/pages/results.py")

try: 
    select_borders(st.session_state.upload)
except Exception as e:
    st.page_link(page="upload.py", label="Please upload a picture first.")

