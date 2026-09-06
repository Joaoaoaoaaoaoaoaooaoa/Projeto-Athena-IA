import streamlit as st
from frontend.api import _request
from frontend.session import get_token

def render_tasks():
    st.title('Tarefas')
    with st.form('new_task'):
        title = st.text_input('Nova tarefa')
        priority = st.selectbox('Prioridade', ['low', 'medium', 'high'])
        if st.form_submit_button('Adicionar') and title:
            _request('POST', '/tasks/', get_token(), json={'title': title, 'priority': priority})
            st.rerun()
    tasks = _request('GET', '/tasks/', get_token())
    for task in tasks:
        c1, c2, c3 = st.columns([5, 1, 1])
        c1.write(('✅ ' if task.get('completed') else '⬜ ') + task['title'])
        if c2.button('Concluir', key=f'done{task["id"]}') and not task.get('completed'):
            _request('PATCH', f'/tasks/{task["id"]}', get_token(), json={'completed': True})
            st.rerun()
        if c3.button('Excluir', key=f'del{task["id"]}'):
            _request('DELETE', f'/tasks/{task["id"]}', get_token())
            st.rerun()
