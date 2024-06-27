import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

from website.const import HOME_CONTENT_I, HOME_CONTENT_II, ROCKET_URL
from website.utils import load_lottie_animation


@st.cache_data
def render_home_section():
    with st.container():
        img, txt, empty = st.columns((1,2, 1))
        with img:
            logo = Image.open('images/logo.png')
            st.image(image=logo, use_column_width="auto")
        with txt:
            st.title("Hi I am Marcin :wave:")
            st.header("A Software Engineer from Poland :desktop_computer:")
            st.write(HOME_CONTENT_I)
        with empty:
            st.empty()

    with st.container():
        st.markdown("---")
        img, txt = st.columns((1, 2))

        with img:
            rocket_animation = load_lottie_animation(ROCKET_URL)
            st_lottie(rocket_animation, height=350, key="rocket")

        with txt:
            st.header("Structure of this website :books:")
            st.write(HOME_CONTENT_II)

