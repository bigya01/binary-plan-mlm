import streamlit as st
from utils.utils import generate_graph
from utils.avltree import AVLTree


def insert(value):
    print(value)
    st.session_state.avltree.insert(int(value))


def delete(value):
    st.session_state.avltree.delete(int(value.val))


st.title("AVL Tree Visualization")

if "avltree" not in st.session_state:
    st.session_state.avltree = AVLTree()

placeholder = st.empty()
col1, col2 = st.columns(2)

with col1.container(border=True):
    col11, col12 = st.columns(2)
    insert_value = col11.number_input(
        "Insert Node", placeholder="Insert Value", step=1)
    print(insert_value)
    col12.markdown('### ')
    col12.button('Insert', on_click=lambda: insert(insert_value))

with col2.container(border=True):
    col21, col22 = st.columns(2)
    delete_value = col21.selectbox(
        "Delete Node", placeholder="Insert Value", options=st.session_state.avltree.get_nodes())
    col22.markdown('### ')
    col22.button('Delete', type="primary", on_click=lambda : delete(delete_value))

generate_graph(st.session_state.avltree)
