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


st.title("Binary MLM Simulator")
genarate_graph()
with open('test.html', 'r', encoding='utf-8') as htmlFile:
    source_code = htmlFile.read()
    components.html(source_code, width=1000, height=30000)
