import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

from website.const import DOCUMENT_URL, MOVIE_URL
from website.utils import load_lottie_animation


def render_resume_section():
    left_empty, img, txt, right_empty = st.columns((1,1,2,1))
    with img:
        video_animation = load_lottie_animation(MOVIE_URL)
        st_lottie(video_animation, height=400, key="video")

    with txt:
        st.title("")
        st.title("")
        st.subheader("Do you want to see an introduction video?")
        st.markdown("[Click here to see more...](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")

    left_empty, img, txt, right_empty = st.columns((1,1,2,1))
    with img:
        document_animation = load_lottie_animation(DOCUMENT_URL)
        st_lottie(document_animation, height=350, key="rocket")

    with txt:
        st.title("")
        st.title("")
        st.subheader("Full version in PDF format")
        st.markdown("[Download from here...](https://www.dropbox.com/scl/fi/ung38j7ld5gwtrtaao5sn/Resume.pdf?rlkey=cd5mlnnpeylsvap7tu2jrjse8&dl=0)")

    empty_left, content, empty_right = st.columns((1,3,1))
    with open('static/cv.md', 'r') as file:
        resume_content = file.read()
    with content:
        st.markdown(resume_content)
