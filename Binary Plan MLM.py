import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network
import pandas as pd

from utils.mlmtree import BinaryMLMTree


def generate_table(tree):
    dictionary = tree.get_nodes_dict()
    data = pd.DataFrame.from_dict(dictionary)
    data.reset_index(drop=True, inplace=True)
    return data


def generate_graph(tree):
    nt = Network("800px", "1000px", notebook=True,
                 heading='', cdn_resources='remote')
    wr = tree.generate_DOT()
    with open('tmp.DOT', 'w') as dotFile:
        dotFile.write(wr)
    nt.from_DOT("tmp.DOT")
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

    def change_config(config):
        st.session_state.tree.set_config(config)
        st.sidebar.success('Applied Settings Sucessfully!')

    def update_sales(node, key):
        st.session_state.tree.update_sales(node, key)

    if "tree" not in st.session_state:  # make it run once
        st.session_state.tree = BinaryMLMTree()

    # program begins here
    st.title("Binary MLM Simulation")
    with st.sidebar:
        st.markdown("## Settings")
        v1 = st.slider("Signup Commission", 0, 100, 20)
        v2 = st.slider("Balance Commission", 0, 500, 50)
        v3 = st.slider("Product Sold Commission", 0.0, 1.0, 0.1)
        v4 = st.slider("Branch Commission", 0.0, 1.0, 0.5)
        st.button("Apply Settings",
                  on_click=lambda: change_config([v1, v2, v3, v4]))

    placeholder = st.empty()
    if st.session_state.tree.root is None:
        with placeholder.container(border=True):
            col1, col2 = st.columns([2, 1])
            user = col1.text_input('User',
                                   placeholder="Insert User..")
            col2.markdown('### ')
            col2.button('Insert', on_click=lambda: insert_root(user))
    else:
        with placeholder.container(border=True):
            col1, col2, col3 = st.columns([2, 2, 1])
            parent1 = col1.selectbox('Where would you like the node to be added?',
                                     st.session_state.tree.get_nodes(), index=0, placeholder="Select parent node..")
            user = col2.text_input('User',
                                   placeholder="Insert User..")
            col3.markdown('### ')
            col3.button('Add User', on_click=lambda: insert(
                user, str(parent1)))

            col1, col2, col3 = st.columns([2, 2, 1])
            parent2 = col1.selectbox('Update Sales Value for a node',
                                     st.session_state.tree.get_nodes(), index=0, placeholder="Select node..")
            sale = col2.number_input('Sales',
                                     placeholder="Insert Sales..")
            col3.markdown('### ')
            col3.button('Update', on_click=lambda: update_sales(
                str(parent2), int(sale)))
        st.table(generate_table(st.session_state.tree))

    generate_graph(st.session_state.tree)


if __name__ == '__main__':
    main()
