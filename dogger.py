import streamlit as st
from streamlit_cropperjs import st_cropperjs
# Failed attempt to have it all in one file, problem is that st_cropperjs 
# cannot be applied to a container that can be emptied
upload = st.empty()
col1, col2 = upload.columns(2)
cam = col1.camera_input("Take a picture of your dog", label_visibility="visible")
file = col2.file_uploader("Upload an image of your dog", type=["png", "jpg", "jpeg"])
if cam is not None or file is not None:
    if cam is not None:
        dog = cam.read()
    if file is not None:
        dog = file.read()
    upload.empty()
    crop_cont = st.empty()
    cropped_pic = st_cropperjs(pic=dog, btn_text="Identify my dog!")
    
    if cropped_pic is not None:
        crop_cont.empty()
        url = "https://snoop_dog_endpoint/identify"
        files = {'dog': cropped_pic}
        #resp = requests.post(url, files=files)
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
        