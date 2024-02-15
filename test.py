import streamlit as st
import requests

st.set_page_config(
    page_title="Canine Classifier 🐶",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="collapsed"
)

id = 'B12BnxcVQ' # B12BnxcVQ


try:
    if id is None:
        resp = requests.get(
            f"https://api.api-ninjas.com/v1/dogs?name=Poodle (Standard)",
            headers={"X-Api-Key": f"{st.secrets['NINJA_DOGS_API_KEY']}"},
            timeout=10000)
        resp.raise_for_status()  # Raise an exception if the request was not successful
        data = resp.json()
        st.write(data)
        st.image(data[0]['image_link'])

    if id is not None:
        resp = requests.get(
            f"https://api.thedogapi.com/v1/images/{id}",
            headers={"Authorization": f"Bearer {st.secrets['THE_DOG_API_KEY']}"},
            timeout=10000)
        resp.raise_for_status()  # Raise an exception if the request was not successful
        data = resp.json()
        breed = data['breeds'][0]

        st.caption(f"Bred for: {breed['bred_for']}")
        st.caption(f"Temperament: {breed['temperament']}")
        st.caption(f"Life span: {breed['life_span']}")
        st.caption(f"Breed group: {breed['breed_group']}")
        st.caption(f"Weight: {breed['weight']['metric']}kg")
        st.caption(f"Height: {breed['height']['metric']}cm")
        st.image(data['url'])

except requests.exceptions.RequestException as e:
   print(e)
