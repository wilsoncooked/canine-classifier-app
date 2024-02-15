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
    if row2[1].button("Try another dog", use_container_width=True):
        st.switch_page("upload.py")

with row1[0]:
    st.title("Canine Classifier 🐶")

left_co, cent_co, last_co = st.columns(3)
holder_img = cent_co.image("images/searching.gif")

results_rows = st.columns(2, gap="medium")
try:
    url = f"{st.secrets['CANINE_API_URL']}/upload_image"
    files = {'img': st.session_state.cropped_pic}
    resp = requests.post(url, files=files, timeout=10000)
    data = resp.json()
    holder_img.empty()
    results_rows[0].subheader("Your dogs most likely breeds are:")

    with results_rows[1]:
        st.write("")
        st.write("")
        vision_row = st.columns(2)
        vision_row[0].write("What you see:")
        vision_row[0].image(st.session_state.cropped_pic, use_column_width=True)
        vision_row[1].write(" What can the 💻🧠 sees:")
        vision_row[1].image(f"{st.secrets['CANINE_API_URL']}/{data[0]['gradcam']}" ,use_column_width=True)


    st.session_state.complete = True
    for index, breed in enumerate(data):
        if breed['breedNames'] == "Others":
            if index < 1:
                with results_rows[0].expander(f"{breed['prob']}% {breed['breedNames']}", expanded=True):
                    st.image("images/question.gif")
            else:
                with results_rows[0].expander(f"{breed['prob']}% {breed['breedNames']}"):
                    st.image("images/question.gif")

        if breed['referenceImageId']:
            resp = requests.get(
                f"https://api.thedogapi.com/v1/images/{breed['referenceImageId']}",
                headers={"Authorization": f"Bearer {st.secrets['THE_DOG_API_KEY']}"},
                timeout=10000)
            resp.raise_for_status()
            data = resp.json()
            def show_results(data):
                if 'url' in data:
                    st.image(data['url'], use_column_width=True)
                if 'bred_for' in data['breeds'][0]:
                    st.caption(f"Bred for: {data['breeds'][0]['bred_for']}")
                if 'temperament' in data['breeds'][0]:
                    st.caption(f"Temperament: {data['breeds'][0]['temperament']}")
                if 'life_span' in data['breeds'][0]:
                    st.caption(f"Life span: {data['breeds'][0]['life_span']}")
                if 'breed_group' in data['breeds'][0]:
                    st.caption(f"Breed group: {data['breeds'][0]['breed_group']}")
                if 'weight' in data['breeds'][0]:
                    st.caption(f"Weight: {data['breeds'][0]['weight']['metric']}kg")
                if 'height' in data['breeds'][0]:
                    st.caption(f"Height: {data['breeds'][0]['height']['metric']}cm")


            if index < 1:
                with results_rows[0].expander(f"{breed['prob']}% {breed['breedNames']}", expanded=True):
                    show_results(data)
            else:
                with results_rows[0].expander(f"{breed['prob']}% {breed['breedNames']}"):
                    show_results(data)

        if breed['referenceImageId'] == None:
            if breed['breedNames'] == "It doesn't look like a dog!":
                 with results_rows[0].expander(f"{breed['breedNames']}", expanded=True):
                    st.image('images/snoop_dogg.gif')
            else:
                resp = requests.get(
                    f"https://api.api-ninjas.com/v1/dogs?name={breed['breedNames']}",
                    headers={"X-Api-Key": f"{st.secrets['NINJA_DOGS_API_KEY']}"},
                    timeout=10000)
                resp.raise_for_status()
                data = resp.json()
                def show_results_2(data):
                    st.image(data[0]['image_link'], use_column_width=True)

                if data:
                    if index < 1:
                        with results_rows[0].expander(f"{breed['prob']}% {breed['breedNames']}", expanded=True):
                            show_results_2(data)
                    else:
                        with results_rows[0].expander(f"{breed['prob']}% {breed['breedNames']}"):
                            show_results_2(data)

except requests.exceptions.RequestException as e:
    print(e)

if st.button("🐕 Start over"):
    st.switch_page("upload.py")
