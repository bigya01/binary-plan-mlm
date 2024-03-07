import streamlit as st
import networkx as nx
import streamlit.components.v1 as components
from pyvis.network import Network


def genarate_graph():
    nx_graph = nx.cycle_graph(10)
    nx_graph.nodes[1]['title'] = 'Number 1'
    nx_graph.nodes[1]['group'] = 1
    nx_graph.nodes[3]['title'] = 'I belong to a different group!'
    nx_graph.nodes[3]['group'] = 10
    nx_graph.add_node(20, size=20, title='couple', group=2)
    nx_graph.add_node(21, size=15, title='couple', group=2)
    nx_graph.add_edge(20, 21, weight=5)
    nx_graph.add_node(25, size=25, label='lonely',
                      title='lonely node', group=3)

    nt = Network("500px", "500px", notebook=True, heading='')
    nt.from_nx(nx_graph)
    nt.show_buttons(filter_=['physics'])
    nt.show('test.html')


st.title("Binary MLM Simulator")
genarate_graph()
with open('test.html', 'r', encoding='utf-8') as htmlFile:
    source_code = htmlFile.read()
    components.html(source_code, width=1000, height=30000)
