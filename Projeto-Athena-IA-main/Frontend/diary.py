import streamlit as st
from frontend.api import _request
from frontend.session import get_token

def render_diary():
    st.title('Diário')
    with st.form('new_entry'):
        content = st.text_area('Como foi seu dia?')
        if st.form_submit_button('Salvar') and content:
            _request('POST', '/diary/', get_token(), json={'content': content})
            st.rerun()
    for entry in _request('GET', '/diary/', get_token()):
        with st.container(border=True):
            st.write(entry['content'])
