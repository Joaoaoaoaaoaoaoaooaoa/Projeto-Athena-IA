import streamlit as st
from frontend.api import _request
from frontend.session import get_token

def render_routines():
    st.title('Rotinas')
    with st.form('new_routine'):
        name = st.text_input('Nome da rotina')
        description = st.text_area('Descrição')
        if st.form_submit_button('Adicionar') and name:
            _request('POST', '/routines/', get_token(), json={'name': name, 'description': description})
            st.rerun()
    for routine in _request('GET', '/routines/', get_token()):
        st.subheader(routine['name'])
        if routine.get('description'):
            st.write(routine['description'])
