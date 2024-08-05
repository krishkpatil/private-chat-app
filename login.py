import streamlit as st
import pandas as pd

def login():
    st.title("Login Page")

    st.write("""
    ### Data Privacy Disclaimer
    By joining the chat, you agree to the collection and storage of the following information:
    - Your username
    - Messages you send during the chat session
    - Decisions you make regarding whether to send or refrain from sending messages
    - Feedback you provide through the Google Form

    This information is collected to evaluate the effectiveness of the chat nudges and to improve our system. Your data will be stored securely and will not be shared with third parties.
    """)

    # Read user credentials from CSV
    username = st.text_input("Username")

    if st.button("Join the Chat"):
        st.session_state['logged_in'] = True
        st.session_state['username'] = username
        st.rerun()
