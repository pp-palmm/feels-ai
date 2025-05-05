# pages/1_English_to_Japanese.py

import streamlit as st
from functions import handle_chat_tab

def english_to_japanese_tab():
    instruction = "Translate the following English text to Japanese in daily life style."
    handle_chat_tab("english_to_japanese", "Convert English to Japanese", instruction, "gpt-4o")

st.set_page_config(page_title="English to Japanese")
english_to_japanese_tab()