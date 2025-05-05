# functions/chat_handler.py

from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def handle_chat_tab(key, subheader, instruction, model):
    st.subheader(subheader)

    # Initialize the session state for message history
    if key + "_history" not in st.session_state:
        st.session_state[key + "_history"] = []

    # Render the chat history
    for message in st.session_state[key + "_history"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Read user input
    if prompt := st.chat_input("Enter your text here:", key=key + "_prompt"):
        st.session_state[key + "_history"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Fetch AI response
        with st.chat_message("assistant"):
            messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state[key + "_history"]]
            messages.insert(0, {"role": "system", "content": instruction})

            stream = client.chat.completions.create(model=model, messages=messages, stream=True)
            response = st.write_stream(stream)

        st.session_state[key + "_history"].append({"role": "assistant", "content": response})