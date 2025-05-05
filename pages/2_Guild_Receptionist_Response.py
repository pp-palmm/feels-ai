# pages/2_Guild_Receptionist_Response.py

import streamlit as st
from functions import handle_chat_tab

def guild_receptionist_response_tab():
    instruction = (
        "As a guild receptionist female in a isekai anime setting, respond to the adventurer's "
        "comment in a concise manner. Embrace the essence of an isekai anime guild receptionist "
        "guidance and be easy to understand."
    )
    handle_chat_tab("guild_receptionist_response", "Guild Receptionist Reply to Comments", instruction, "gpt-4o")

st.set_page_config(page_title="Guild Receptionist Response")
guild_receptionist_response_tab()