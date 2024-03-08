import streamlit as st
import networkx as nx
import streamlit.components.v1 as components
from pyvis.network import Network
import pandas as pd

from utils.mlmtree import BinaryMLMTree, Node
from options import options as graph_options
import utils.settings as s

def generate_table(tree):
    dictionary = tree.get_nodes_dict()
    data = pd.DataFrame.from_dict(dictionary)
    data['From Members'] = data['Members Added']*s.SIGNUP_COMMISION
    data['From Sales'] = data['Sales']*s.PRODUCT_SOLD_COMMISSION
    data['From Branched Members'] = data['Total Commission'] - data['From Members'] - data['From Sales']
    # print(dictionary)
    st.table(data)

def generate_graph(tree):
    nt = Network("800px", "1000px", notebook=True,
                 heading='', cdn_resources='remote')
    wr = tree.generate_DOT()
    with open('tmp.DOT', 'w') as dotFile:
        dotFile.write(wr)
    nt.from_DOT("tmp.DOT")
    # nt.toggle_physics(True)
    nt.set_options(graph_options)
    nt.show('tmp.html')
    with open('tmp.html', 'r', encoding='utf-8') as htmlFile:
        source_code = htmlFile.read()
        components.html(source_code, width=1000, height=800)


def main():
    # use callback for state management (streamlit hacks)
    def insert_root(user):
        st.session_state.tree.insert_root(user)

    def insert(user, parent):
        # print(user,parent,side)
        st.session_state.tree.insert(user, parent)

    def update_sales(node, key):
        st.session_state.tree.update_sales(node, key)

    if "tree" not in st.session_state:  # make it run once
        st.session_state.tree = BinaryMLMTree()

    # program begins here
    st.title("Binary MLM Simulation")
    placeholder = st.empty()
    if st.session_state.tree.root is None:
        with placeholder.container():
            col1, col2 = st.columns([2, 1])
            user = col1.text_input('User',
                                   placeholder="Insert User..")
            col2.button('Insert', on_click=lambda: insert_root(user))
    else:
        with placeholder.container():
            col1, col2, col3 = st.columns([2, 2, 1])
            parent = col1.selectbox('Where would you like the node to be added?',
                                    st.session_state.tree.get_nodes(), index=None, placeholder="Select parent node..", key=1)
            user = col2.text_input('User',
                                   placeholder="Insert User..")
            col3.button('Add User', on_click=lambda: insert(user, str(parent)))
            generate_table(st.session_state.tree)
            col1, col2, col3 = st.columns([2, 2, 1])
            parent = col1.selectbox('Where would you like the node to be added?',
                                    st.session_state.tree.get_nodes(), index=None, placeholder="Select parent node..", key=2)
            sale = col2.number_input('Sales',
                                     placeholder="Insert Sales..")
            col3.button('Update', on_click=lambda: update_sales(
                str(parent), int(sale)))

    generate_graph(st.session_state.tree)


if __name__ == '__main__':
    main()
