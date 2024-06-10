import streamlit as st
from llsp_base import create_pycode_to_llsp3


st.set_page_config(
    page_title="Convert Python code to LLSP3 file",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "## ファイルコンバーター\n\nPythonコードをLLSP3ファイルに変換するアプリです。"
    }
)


def main():
    st.title('Python code to LLSP3 file converter')
    py_code = st.text_area(label='Enter python code here', height=300)

    st.download_button(label='Convert & Dwonload LLSP3 file', 
                       type='primary',
                       data=create_pycode_to_llsp3(py_code),
                       file_name='srps.llsp3',
                       mime='application/zip')


if __name__ == '__main__':
    main()