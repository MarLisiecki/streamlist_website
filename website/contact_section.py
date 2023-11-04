import streamlit as st
from streamlit_lottie import st_lottie

from website.const import MAIL_URL
from website.utils import load_lottie_animation, load_custom_css


def render_contact_section():
    with st.container():
        empty_left, animation, txt, empty_right = st.columns(4)

        with animation:
            mail_animation = load_lottie_animation(MAIL_URL)
            st_lottie(mail_animation, height=650, key="mail")

        with txt:
            st.title('Contact information')
            st.markdown('## :envelope: Mail: marcin.lisiecki@tutanota.com')
            st.markdown('## :globe_with_meridians: [Linkedin](https://www.linkedin.com/in/marcin-lisiecki1997/)')
            st.markdown('## :robot_face: [Facebook](https://www.facebook.com/marcin.lisiecki.39/)')

    with st.container():
        st.markdown(
            "<h1 style='text-align: center; color: white;'> Contact me 📮</h1>",
            unsafe_allow_html=True
        )
        contact_form = f"""
        <form action="https://formsubmit.co/marcin.lisiecki@tutanota.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        right_col, center_col, left_col = st.columns((1,2,1))
        load_custom_css("style/style.css")

        with left_col:
            st.empty()

        with center_col:
            st.markdown(contact_form, unsafe_allow_html=True)

        with right_col:
            st.empty()