from functools import lru_cache

import requests
import streamlit as st
from streamlit_lottie import st_lottie

from website.const import GEARS_URL


def load_lottie_animation(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        print("Error loading lottie")
    return response.json()


def load_custom_css(filename: str):
    with open(filename) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


@st.cache_data
def tempoary_in_progress():
    with st.container():
        left, animation, right = st.columns((1,3,1))
        with left:
            st.empty()

        with animation:
            st.markdown("<h1 style='text-align: center; color: white;'>In progress</h1>", unsafe_allow_html=True)
            gear_animation = load_lottie_animation(GEARS_URL)
            st_lottie(gear_animation)

        with right:
            st.empty()
