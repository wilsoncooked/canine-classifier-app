import streamlit as st
st.title("Canine Classifier 🐶")
st.write("## Identify your dogs breed! :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog: :dog:")

def identify(cropped_pic):
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

identify(st.session_state.cropped_pic)