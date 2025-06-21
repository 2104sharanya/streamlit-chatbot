import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="ChatGPT-Style Bot", layout="centered")
st.title("🤖 ChatGPT-Style ChatBot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display the chat
for msg in st.session_state.chat_history[1:]:  # Skip system prompt
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# Get user input
prompt = st.chat_input("Type your message...")

if prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Call OpenAI to get a response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.chat_history
        )
        full_response = response.choices[0].message.content
        message_placeholder.markdown(full_response)

    # Save assistant reply
    st.session_state.chat_history.append({"role": "assistant", "content": full_response})
