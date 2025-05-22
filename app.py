import streamlit as st
import openai
import os

# Set your OpenAI API key securely
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Marketing Stack Matcher", page_icon="🧩")
st.title("🧩 Marketing Stack Matcher")
st.write("Get a personalized marketing tool stack based on your business type, time, and tech level — no overwhelm.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a friendly tech advisor helping small business owners choose marketing tools. Ask one question at a time."},
        {"role": "assistant", "content": "Hey there! Let’s find your ideal marketing tools. First up: What type of business do you run?"}
    ]

for msg in st.session_state.messages[1:]:
    if msg["role"] == "assistant":
        st.markdown(f"**GPT:** {msg['content']}")
    else:
        st.markdown(f"**You:** {msg['content']}")

user_input = st.text_input("Your answer", key="user_input")

if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()
