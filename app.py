import streamlit as st
import networkx as nx
import streamlit.components.v1 as components
from pyvis.network import Network
from options import options as graph_options


def genarate_graph():
    nt = Network(notebook=True, heading='', cdn_resources='remote')
    nt.from_DOT("tree.DOT")
    # nt.from_nx(nx.complete_graph(5))
    nt.toggle_physics(True)
    nt.set_options(graph_options)
    # nt.show_buttons()
    nt.show('test.html')


def insert():
    pass


st.title("Binary MLM Simulator")
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
col1.selectbox('Where would you like the node to be added?',
               (1, 2, 3), index=None, placeholder="Select parent node..")
col2.text_input('User',
                placeholder="Insert User..")
col3.selectbox('Side',
               ('Left', 'Right'), index=None, placeholder="Insert Value..")
col4.button('Insert', on_click=insert)

genarate_graph()
with open('test.html', 'r', encoding='utf-8') as htmlFile:
    source_code = htmlFile.read()
    components.html(source_code, width=1000, height=30000)
