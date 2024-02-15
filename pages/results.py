import streamlit as st
import requests

st.set_page_config(
    page_title="Canine Classifier 🐶",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="collapsed"
)

with open("styles/main.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if 'cropped_pic' not in st.session_state:
    st.switch_page("upload.py")
st.session_state.complete = False
row1 = st.columns(2)
with row1[1]:
    row2 = st.columns(2)
    if row2[1].button("Try new 🐕📸", use_container_width=True):
        st.switch_page("upload.py")

with row1[0]:
    st.title("Canine Classifier")

h = st.columns(2)
h[1].write('')

left_co, cent_co, last_co = st.columns(3)
holder_img = cent_co.image("images/searching.gif")

try:
    url = f"{st.secrets['CANINE_API_URL']}/upload_image"
    files = {'img': st.session_state.cropped_pic}
    resp = requests.post(url, files=files, timeout=10000)
    data = resp.json()
    holder_img.empty()
    st.session_state.complete = True
    st.subheader(f"Your dog is:")
    for breed in data:
        col1, col2 = st.columns(2, gap="medium")
        col2.subheader(f"{breed['prob']}%: {breed['breedNames']}")
        if breed['breedNames'] == "Others":
            col1.image("images/question.gif")
        if breed['referenceImageId']:
            resp = requests.get(
                f"https://api.thedogapi.com/v1/images/{breed['referenceImageId']}",
                headers={"Authorization": f"Bearer {st.secrets['THE_DOG_API_KEY']}"},
                timeout=10000)
            resp.raise_for_status()
            data = resp.json()
            if data:
                if 'bred_for' in data['breeds'][0]:
                    col2.write(f"Bred for: {data['breeds'][0]['bred_for']}")
                if 'temperament' in data['breeds'][0]:
                    col2.write(f"Temperament: {data['breeds'][0]['temperament']}")
                if 'life_span' in data['breeds'][0]:
                    col2.write(f"Life span: {data['breeds'][0]['life_span']}")
                if 'breed_group' in data['breeds'][0]:
                    col2.write(f"Breed group: {data['breeds'][0]['breed_group']}")
                if 'weight' in data['breeds'][0]:
                    col2.write(f"Weight: {data['breeds'][0]['weight']['metric']}kg")
                if 'height' in data['breeds'][0]:
                    col2.write(f"Height: {data['breeds'][0]['height']['metric']}cm")
                if 'url' in data:
                    col1.image(data['url'], use_column_width=True)
        if breed['referenceImageId'] == None:
            if breed['breedNames'] == "It doesn't look like a dog!":
                col1.image('images/snoop_dogg.gif')
            else:
                resp = requests.get(
                    f"https://api.api-ninjas.com/v1/dogs?name={breed['breedNames']}",
                    headers={"X-Api-Key": f"{st.secrets['NINJA_DOGS_API_KEY']}"},
                    timeout=10000)
                resp.raise_for_status()
                data = resp.json()
                if data:
                    col1.image(data[0]['image_link'], use_column_width=True)


        st.divider()
except requests.exceptions.RequestException as e:
    print(e)

st.button("🐕 Start over")
