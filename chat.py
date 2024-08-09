import streamlit as st
import pandas as pd
import time
from nlp_model import check_for_confidential_info

def display_chat_history(messages):
    for message_ in messages:
        role = 'assistant' if message_["user_id"] == st.session_state['username'] else 'user'
        with st.chat_message(role):
            st.write(f"{message_['user_id']}: {message_['message_content']}")
    st.markdown("""
        <style>
            .stChatMessage:has(.chat-assistant) {
                flex-direction: row-reverse;
                text-align: right;
            }
        </style>
        """, unsafe_allow_html=True)

def assign_roles(messages):
    for each_message in messages:
        each_message['role'] = 'assistant' if each_message['user_id'] == st.session_state['username'] else 'user'
    return messages

def on_yes_confirmation(user_message):
    messages_df = pd.read_csv("data/messages.csv")
    new_message = pd.DataFrame({
        'user_id': [st.session_state['username']], 
        'message_content': [user_message],
        'model_response': ['public'],
        'decision': ['send']
    })
    message_all = pd.concat([messages_df, new_message], ignore_index=True)
    message_all.to_csv("data/messages.csv", index=False)
    del st.session_state.confirm_confidential

def on_no_confirmation(user_message, response):
    confidential_message = pd.DataFrame({
        'user_id': [st.session_state['username']], 
        'message_content': [user_message], 
        'model_response': [response],
        'decision': ['refrain']
    })
    confidential_message_all = pd.read_csv("data/flagged_messages.csv")
    confidential_message_all = pd.concat([confidential_message_all, confidential_message], ignore_index=True)
    confidential_message_all.to_csv("data/flagged_messages.csv", index=False)
    del st.session_state.confirm_confidential

def auto_refresh():
    time.sleep(5)
    st.rerun()

def chat():
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        st.error("Please login first.")
        return        

    st.title("Welcome to Private Chat!")

    st.sidebar.title("User Name")
    st.sidebar.code(st.session_state['username'], language='')

    st.write("### Instructions")
    st.write("""
    In this task, you will be interacting with a chat application that simulates real-world scenarios.
    The messages you send can be classified into one of three types:
    1. **Public**: Information that is safe to share openly.
    2. **Sensitive**: Information that should be handled with care and only shared with authorized individuals.
    3. **Confidential**: Information that is highly sensitive and should not be shared without proper authorization.
    
    **Data Privacy Reminder**: All your messages, decisions, and feedback will be stored securely and used only for evaluating the effectiveness of the chat nudges. Your data will not be shared with third parties.
    """)

    messages_df = pd.read_csv("data/messages.csv")
    messages_list = messages_df.to_dict('records')
    messages_list = assign_roles(messages_list)
    display_chat_history(messages_list)

    user_message = st.chat_input("Enter your message:")

    if user_message:
        if 'confirm_confidential' not in st.session_state:
            st.session_state['confirm_confidential'] = False

        model_response = check_for_confidential_info(user_message)
        if model_response != 'public':
            if not st.session_state['confirm_confidential']:
                with st.chat_message('assistant'):
                    st.write(f"{st.session_state['username']}: {user_message}")
                error, yes_button, no_button = st.columns([6, 0.5, 0.5])
                with error:
                    if model_response == 'confidential':
                        st.error('Your message may contain confidential information. Do you still want to send it?')
                    elif model_response == 'sensitive':
                        st.warning('Your message may contain sensitive information. Do you still want to send it?')
                with yes_button:
                    if st.button("Yes", use_container_width=True, on_click=on_yes_confirmation, args=(user_message,)):
                        st.session_state.confirm_confidential = True
                with no_button:
                    if st.button("No", use_container_width=True, on_click=on_no_confirmation, args=(user_message, model_response)):
                        st.session_state.confirm_confidential = True
            time.sleep(2)
        else:
            new_message = pd.DataFrame({
                'user_id': [st.session_state['username']], 
                'message_content': [user_message],
                'model_response': ['public'],
                'decision': ['send']
            })
            message_all = pd.concat([messages_df, new_message], ignore_index=True)
            message_all.to_csv("data/messages.csv", index=False)
            st.rerun()
    
    # Add a section to provide feedback link after tasks
    st.write("Please provide your feedback using the link below.")
    st.markdown("[Google Form Feedback](https://forms.gle/5DocUusJSYvKCkuq8)")
    
    auto_refresh()

if __name__ == "__main__":
    chat()
