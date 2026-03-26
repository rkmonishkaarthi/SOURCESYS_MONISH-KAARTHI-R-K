import streamlit as st
from gemini_api import load_gemini, get_response
from transformer_utils import analyze_input

st.title(" AI Chatbot With Gemini API Key")

model = load_gemini()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    sentiment = analyze_input(user_input)

    bot_response = get_response(model, user_input)

    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    with st.chat_message("assistant"):
        st.write(bot_response)
        st.caption(f"Sentiment: {sentiment['label']}")
