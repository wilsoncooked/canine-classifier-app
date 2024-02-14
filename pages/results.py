import streamlit as st
import requests
import time # Just for testing purpose

st.set_page_config(layout='wide',initial_sidebar_state='collapsed')

if 'cropped_pic' not in st.session_state:
    st.switch_page("upload.py")

st.title("Canine Classifier 🐶")
st.write("## Identify your dogs breed! :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog:")


def identify(cropped_pic):
    url = f"{st.secrets['CANINE_API_URL']}/upload_image"
    files = {'img': cropped_pic}
    container = st.empty()
    message, gif = container.columns(2)
    message.write("Please wait...")
    gif_runner = gif.image("./pages/searching.gif")
    time.sleep(5) # Testing
    resp = requests.post(url, files=files, timeout=10000)
    container.empty()
    data = resp.json()
    st.session_state.complete = True
    col1, col2 = st.columns(2)
    col1.image(cropped_pic)
    col2.write(f"Your dogs recognized breeds are:")
    for breed in data:
        col2.write(f"{breed['breedNames']}: {breed['prob']}%")

if 'complete' not in st.session_state:
    try:
        identify(st.session_state.cropped_pic)
    except Exception as e:
        st.write("Please do the previous steps.")


if st.button("🐕 Rerun", use_container_width=True): # Streamlit is very strange, it reruns the whole page on click so that it makes another api request, workaround needed
    st.switch_page("upload.py")
