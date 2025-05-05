# pages/4_YT_Content_Writer.py

import streamlit as st
from functions.yt_content_writer import yt_content_writer

def main():
    st.title("YouTube Content Writing")
    yt_content_writer()

if __name__ == "__main__":
    main()