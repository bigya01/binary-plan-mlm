import streamlit as st
import networkx as nx
import streamlit.components.v1 as components
from pyvis.network import Network
from utils.mlmtree import BinaryMLMTree, Node
from options import options as graph_options


def generate_graph(tree):
    nt = Network("800px", "1000px", notebook=True,
                 heading='', cdn_resources='remote')
    wr = tree.generate_DOT()
    with open('tmp.DOT', 'w') as dotFile:
        dotFile.write(wr)
    nt.from_DOT("tmp.DOT")
    nt.toggle_physics(True)
    nt.show('tmp.html')
    with open('tmp.html', 'r', encoding='utf-8') as htmlFile:
        source_code = htmlFile.read()
        components.html(source_code, width=1000, height=800)


def main():
    def insert_root(user):
        st.session_state.tree.insert_root(user)

    def insert(parent, side, user):
        st.session_state.tree.insert(user, parent, side)

    if "tree" not in st.session_state:  # make it run once
        st.session_state.tree = BinaryMLMTree()

    #program begins here 
    st.title("Binary MLM Simulator")
    placeholder = st.empty()
    if st.session_state.tree.root is None:
        with placeholder.container():
            col1, col2 = st.columns([2, 1])
            user = col1.text_input('User',
                                   placeholder="Insert User..")
            col2.button('Insert', on_click=lambda: insert_root(user))
    else:
        with placeholder.container():
            col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
            parent = col1.selectbox('Where would you like the node to be added?',
                                    st.session_state.tree.get_nodes(), index=None, placeholder="Select parent node..")
            user = col2.text_input('User',
                                   placeholder="Insert User..")
            side = col3.selectbox('Side',
                                  ('Left', 'Right', 'Spill'), index=None, placeholder="Insert Value..")
            col4.button('Insert', on_click=lambda: insert(user, parent, side))
    generate_graph(st.session_state.tree)


if __name__ == '__main__':
    main()
