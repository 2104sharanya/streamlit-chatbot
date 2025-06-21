import streamlit as st
from textblob import TextBlob

st.title("🤖 Simple ChatBot")

if "messages" not in st.session_state:
    st.session_state.messages = []

def get_response(msg):
    polarity = TextBlob(msg).sentiment.polarity
    if polarity > 0.2:
        return "😊 You seem happy! How can I help?"
    elif polarity < -0.2:
        return "😟 I’m sorry you're feeling that way. I'm here for you."
    else:
        return "🤖 I'm listening! How can I assist?"

user_input = st.text_input("You:", "")

if user_input:
    st.session_state.messages.append(("You", user_input))
    reply = get_response(user_input)
    st.session_state.messages.append(("Bot", reply))

for sender, msg in st.session_state.messages:
    st.markdown(f"**{sender}:** {msg}")

