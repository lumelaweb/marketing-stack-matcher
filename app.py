import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Marketing Stack Matcher", page_icon="🧩")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a friendly tech advisor helping small business owners choose marketing tools. Ask one question at a time."},
        {"role": "assistant", "content": "Hey there! Let’s find your ideal marketing tools. First up: What type of business do you run?"}
    ]

# Display chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get GPT response using the new OpenAI v1 client
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=st.session_state.messages
        )
        re
