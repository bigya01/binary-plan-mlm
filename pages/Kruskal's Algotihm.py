import streamlit as st
from utils.utils import generate_graph
from utils.kruskal import Graph

def insert(u,v,w):
    print(u,v,w)
    st.session_state.graph.addEdge(u,v,w)


def generate():
    st.session_state.graph = st.session_state.graph.KruskalMST()

def get_weight():
    return st.session_state.graph.get_total_weight()


st.title("Kruskal's Algorithm")

if "graph" not in st.session_state:
    st.session_state.graph = Graph()

placeholder = st.empty()
with placeholder.container(border=True):
    col1, col2 = st.columns([2,1])
    with col1.container():
        col11, col12, col13, col14 = st.columns(4)
        u = col11.text_input(
            "From", placeholder="Insert Value")
        v = col12.text_input(
            "To", placeholder="Insert Value")
        w = col13.number_input(
            "Weight", placeholder="Insert Value", step=1)
        col14.markdown('### ')
        col14.button('Insert', on_click=lambda: insert(u,v,int(w)))
    with col2:
        col21, col22 = st.columns(2)
        col21.markdown(f"#### {get_weight()}")
        col22.markdown('### ')
        col22.button('Generate', type="primary", on_click=lambda :  generate())

generate_graph(st.session_state.graph)
