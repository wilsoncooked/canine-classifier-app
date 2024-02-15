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


st.title("Canine Classifier 🐶")
st.subheader("Identify your dogs breed!")

container = st.empty()
for key in st.session_state.keys():
    del st.session_state[key]

col1, col2 = container.columns(2, gap="medium")
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

# st.image('images/dog-838281_1920.jpg')
