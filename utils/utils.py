import pandas as pd
import streamlit.components.v1 as components
from pyvis.network import Network
import pandas as pd

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