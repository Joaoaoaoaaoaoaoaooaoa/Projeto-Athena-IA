import streamlit as st
from frontend.api import _request
from frontend.session import get_token

def render_dashboard():
    st.title('Dashboard')
    try:
        tasks = _request('GET', '/tasks/', get_token())
        routines = _request('GET', '/routines/', get_token())
        diary = _request('GET', '/diary/', get_token())
        c1, c2, c3 = st.columns(3)
        c1.metric('Tarefas', len(tasks))
        c2.metric('Rotinas', len(routines))
        c3.metric('Registros', len(diary))
    except Exception as exc:
        st.warning(f'Não foi possível carregar o resumo: {exc}')
