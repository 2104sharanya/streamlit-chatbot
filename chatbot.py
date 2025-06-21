import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="ChatBot", layout="centered")
st.title("💬 Stylish ChatBot")

# Inject CSS for custom chat bubbles
st.markdown("""
    <style>
    .chat-bubble {
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 0;
        max-width: 75%;
        display: inline-block;
        font-size: 16px;
    }
    .user {
        background-color: #DCF8C6;
        color: black;
        margin-left: auto;
        text-align: right;
    }
    .bot {
        background-color: #E4E6EB;
        color: black;
        margin-right: auto;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

# Store chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Reply generator
def get_reply(user_msg):
    polarity = TextBlob(user_msg).sentiment.polarity
    if polarity > 0.2:
        return "😊 You seem happy! How can I help you?"
    elif polarity < -0.2:
        return "😢 I'm here for you. Want to talk about it?"
    else:
        return "🤖 I'm listening! Tell me more."

# User input
user_input = st.text_input("Type your message:", "")

# Process input
if user_input:
    bot_response = get_reply(user_input)
    st.session_state.chat.append(("user", user_input))
    st.session_state.chat.append(("bot", bot_response))

# Display chat
for role, message in st.session_state.chat:
    bubble_class = "user" if role == "user" else "bot"
    st.markdown(f"<div class='chat-bubble {bubble_class}'><b>{'🧑 You' if role=='user' else '🤖 Bot'}:</b> {message}</div>", unsafe_allow_html=True)
