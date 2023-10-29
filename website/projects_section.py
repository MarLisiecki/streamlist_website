import streamlit as st

from website.utils import tempoary_in_progress


def render_projects_section():
    with st.container():
        left, txt, right = st.columns((1, 3, 1))

        with left:
            st.empty()

        with txt:
            st.markdown(
                '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">',
                unsafe_allow_html=True
            )
            st.markdown(
                "<h1 style='text-align: center; color: white;'><a href='https://github.com/MarLisiecki' target='_blank'><i class='fab fa-github'></i> Github</a></h1>",
                unsafe_allow_html=True
            )
            st.markdown(
                "<h1 style='text-align: center; color: white;'> More coming soon</a></h1>",
                unsafe_allow_html=True
            )
        with right:
            st.empty()

    tempoary_in_progress()
