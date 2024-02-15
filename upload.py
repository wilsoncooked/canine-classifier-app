import streamlit as st

st.set_page_config(
    page_title="Canine Classifier 🐶",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="collapsed"
)
with open("styles/main.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
MAX_FILE_SIZE = 6 * 1024 * 1024  # 6MB

col1, col2 = st.columns(2, gap="medium")

col1.title("Canine Classifier 🐶")
col1.subheader("Identify your dogs breed!")

for key in st.session_state.keys():
    del st.session_state[key]

upload = col1.file_uploader("Upload an image of your dog", type=["png", "jpg", "jpeg"])
cam = col1.camera_input("Take a picture of your dog", label_visibility="visible")
col2.image("images/orange_doggo.png", use_column_width=True)

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
