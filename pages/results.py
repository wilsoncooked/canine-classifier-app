import streamlit as st
import requests

st.title("Canine Classifier 🐶")
st.write("## Identify your dogs breed! :dog: :dog: :dog:")

def identify(cropped_pic):
    url = "http://127.0.0.1:8000/upload_image"
    files = {'img': cropped_pic}
    resp = requests.post(url, files=files)
    st.write(resp.json())
    #data = resp.json()
    data = {"German shepherd": 80.32,
            "Chihuaha": 10.83,
            "Dachshund": 5.17,
            "Corgie": 2.00,
            "Tibetan Mastiff": 1.94}
    col1, col2 = st.columns(2)
    col1.image(cropped_pic)
    col2.write(f"Your dogs recognized breeds are:")
    for k in data.keys():
        col2.write(f"{k}: {data[k]}%")

identify(st.session_state.cropped_pic)