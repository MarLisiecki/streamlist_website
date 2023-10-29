import streamlit as st
from streamlit_option_menu import option_menu

from website.articles_section import render_articles_section
from website.contact_section import render_contact_section
from website.home_section import render_home_section
from website.projects_section import render_projects_section
from website.resume_section import render_resume_section


# === Navigation section ===


def render_main_page():
    # TODO In the future: https://github.com/TangleSpace/hydralit_components - to consider
    selected = option_menu(
        menu_title=None,
        options=["Home", "Resume", "Projects", "Articles", "Contact"],
        icons=["house", "person-circle", "github", "book", "send"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"background-color": "#1F5673"},
            "nav-link-selected": {"background-color": "#61ABB1"}
        }
    )

    if selected == "Home":
        render_home_section()
    elif selected == "Resume":
        render_resume_section()
    elif selected == "Projects":
        render_projects_section()
    elif selected == "Articles":
        render_articles_section()
    elif selected == "Contact":
        render_contact_section()


if __name__ == "__main__":
    st.set_page_config(page_title="Marcin Lisiecki", page_icon=":alien:", layout="wide")
    render_main_page()
