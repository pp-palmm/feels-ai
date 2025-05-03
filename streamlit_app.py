from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("ChatGPT-like Clone with Tabs")

# Create two tabs using Streamlit's native tab interface
tab1, tab2 = st.tabs(["English to Japanese", "Guild Master Response"])

def english_to_japanese_tab():
    st.subheader("Convert English to Japanese")
    # Instruction for this tab
    instruction = "Translate the following English text to Japanese."
    
    if "english_to_japanese" not in st.session_state:
        st.session_state["english_to_japanese"] = []

    # Display previous messages
    for message in st.session_state["english_to_japanese"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Enter text in English"):
        st.session_state["english_to_japanese"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state["english_to_japanese"]]
            messages.insert(0, {"role": "system", "content": instruction})
            
            stream = client.chat.completions.create(model="gpt-4o", messages=messages, stream=True)
            response = st.write_stream(stream)

        st.session_state["english_to_japanese"].append({"role": "assistant", "content": response})

def guild_master_response_tab():
    st.subheader("Guild Master Reply to Comments")
    # Instruction for this tab
    instruction = "As a guild master in a grand MMORPG setting, respond to the adventurer's comment in a concise manner. Embrace the essence of an NPC, using a formal, majestic tone of speech infused with wisdom and guidance while maintaining positivity, but keep it very concise and easy to understand"

    if "guild_master_response" not in st.session_state:
        st.session_state["guild_master_response"] = []

    # Display previous messages
    for message in st.session_state["guild_master_response"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Enter comment here"):
        st.session_state["guild_master_response"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state["guild_master_response"]]
            messages.insert(0, {"role": "system", "content": instruction})

            stream = client.chat.completions.create(model="gpt-4o", messages=messages, stream=True)
            response = st.write_stream(stream)

        st.session_state["guild_master_response"].append({"role": "assistant", "content": response})

with tab1:
    english_to_japanese_tab()

with tab2:
    guild_master_response_tab()