import streamlit as st
from utils.utils import generate_graph
from utils.redblacktree import RedBlackTree


def insert(value):
    print(value)
    st.session_state.rb_tree.insert(int(value))


def delete(value):
    st.session_state.rb_tree.delete(int(value.key))


st.title("Red Black Tree Visualization")

if "rb_tree" not in st.session_state:
    st.session_state.rb_tree = RedBlackTree()

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
        "Delete Node", placeholder="Insert Value", options=st.session_state.rb_tree.get_nodes())
    col22.markdown('### ')
    col22.button('Delete', type="primary",
                 on_click=lambda: delete(delete_value))

generate_graph(st.session_state.rb_tree)
