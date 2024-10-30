#Input your information
import streamlit as st
import base64
from st_pages import add_page_title, get_nav_from_toml
import webbrowser
import re
import smtplib

st.title("Leave your feedback for us!")

with st.form("my_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    Submit = st.form_submit_button("Submit")

email_regex = r"^[a-zA-Z0-9_.+-]+@(gmail).(com|edu|net|org)$"
if Submit:
    if not re.match(email_regex, email):
        st.error("Invalid email address")
    else:
        st.success("Form submitted successfully")







