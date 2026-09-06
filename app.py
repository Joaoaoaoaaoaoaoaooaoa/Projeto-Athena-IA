import streamlit as st
from frontend.session import get_token, set_token, clear_token
from frontend.api import login, register
from frontend.pages.dashboard import render_dashboard
from frontend.pages.tasks import render_tasks
from frontend.pages.routines import render_routines
from frontend.pages.diary import render_diary

st.set_page_config(page_title='ATHENA', page_icon='🧠', layout='wide')

if 'token' not in st.session_state:
    st.session_state.token = None

if not get_token():
    st.title('ATHENA')
    st.caption('Organização, rotina e apoio no dia a dia.')
    login_tab, register_tab = st.tabs(['Entrar', 'Criar conta'])
    with login_tab:
        email = st.text_input('E-mail', key='login_email')
        password = st.text_input('Senha', type='password', key='login_password')
        if st.button('Entrar', type='primary'):
            try:
                data = login(email, password)
                set_token(data['access_token'])
                st.rerun()
            except Exception as exc:
                st.error(f'Não foi possível entrar: {exc}')
    with register_tab:
        email = st.text_input('E-mail', key='register_email')
        password = st.text_input('Senha (mínimo 8 caracteres)', type='password', key='register_password')
        if st.button('Criar conta'):
            try:
                data = register(email, password)
                set_token(data['access_token'])
                st.rerun()
            except Exception as exc:
                st.error(f'Não foi possível criar a conta: {exc}')
    st.stop()

with st.sidebar:
    st.title('ATHENA')
    page = st.radio('Menu', ['Dashboard', 'Tarefas', 'Rotinas', 'Diário'])
    if st.button('Sair'):
        clear_token()
        st.rerun()

if page == 'Dashboard':
    render_dashboard()
elif page == 'Tarefas':
    render_tasks()
elif page == 'Rotinas':
    render_routines()
else:
    render_diary()
