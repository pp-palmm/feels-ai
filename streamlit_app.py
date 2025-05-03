from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Feels the Isekai AI")

# Create two tabs using Streamlit's native tab interface
tab1, tab2, tab3 = st.tabs(["English to Japanese", "Guild Master Response", "Rune Translator"])

def english_to_japanese_tab():
    st.subheader("Convert English to Japanese")
    instruction = "Translate the following English text to Japanese."
    
    if "english_to_japanese" not in st.session_state:
        st.session_state["english_to_japanese"] = []

    for message in st.session_state["english_to_japanese"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter text in English", key="english_japanese"):
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
    instruction = "As a guild master in a grand MMORPG setting, respond..."

    if "guild_master_response" not in st.session_state:
        st.session_state["guild_master_response"] = []

    for message in st.session_state["guild_master_response"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter comment here", key="guild_master"):
        st.session_state["guild_master_response"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state["guild_master_response"]]
            messages.insert(0, {"role": "system", "content": instruction})

            stream = client.chat.completions.create(model="gpt-4o", messages=messages, stream=True)
            response = st.write_stream(stream)

        st.session_state["guild_master_response"].append({"role": "assistant", "content": response})

def english_to_rune():
    st.subheader("English to Rune Translator")
    instruction = '''
    Convert the following English text into Elder Futhark-style runes using this mapped guide for letters a-z:
{
  'a': 'ᚨ',
  'b': 'ᛒ',
  'c': 'ᚲ',
  'd': 'ᛞ',
  'e': 'ᛖ',
  'f': 'ᚠ',
  'g': 'ᚷ',
  'h': 'ᚺ',
  'i': 'ᛁ',
  'j': 'ᛃ',
  'k': 'ᚲ',
  'l': 'ᛚ',
  'm': 'ᛗ',
  'n': 'ᚾ',
  'o': 'ᛟ',
  'p': 'ᛈ',
  'q': 'ᛩ',
  'r': 'ᚱ',
  's': 'ᛋ',
  't': 'ᛏ',
  'u': 'ᚢ',
  'v': 'ᚡ',
  'w': 'ᚹ',
  'x': 'ᛉ',
  'y': 'ᛃ',
  'z': 'ᛉ'
}

other than this, write as original character or symbol
    '''

    if "english_to_rune" not in st.session_state:
        st.session_state["english_to_rune"] = []

    for message in st.session_state["english_to_rune"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter comment here", key="english_rune"):
        st.session_state["english_to_rune"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state["english_to_rune"]]
            messages.insert(0, {"role": "system", "content": instruction})

            stream = client.chat.completions.create(model="o1", messages=messages, stream=True)
            response = st.write_stream(stream)

        st.session_state["english_to_rune"].append({"role": "assistant", "content": response})

with tab1:
    english_to_japanese_tab()

with tab2:
    guild_master_response_tab()

with tab3:
    english_to_rune()