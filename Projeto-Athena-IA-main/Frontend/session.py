import streamlit as st

def get_token():
    return st.session_state.get('token')

def set_token(token: str):
    st.session_state.token = token

def clear_token():
    st.session_state.token = None
