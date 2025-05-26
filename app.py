import streamlit as st
import openai

# Set your OpenAI API key securely
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Marketing Stack Matcher", page_icon="🧩")

# Initialize session state for conversation messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a friendly tech advisor helping small business owners choose marketing tools. Ask one question at a time."},
        {"role": "assistant", "content": "Hey there! Let’s find your ideal marketing tools. First up: What type of business do you run?"}
    ]

# Display chat history using st.chat_message
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input using chat_input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Call OpenAI GPT-4 for response
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.messages
        )
        reply = response['choices'][0]['message']['content']
    
    # Append assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
