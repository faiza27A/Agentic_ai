
import streamlit as st
from customer_agent import customer_support

# Page configuration
st.set_page_config(
    page_title="E-Commerce Customer Support",
    page_icon="🛒",
    layout="centered"
)

# Page heading
st.title("🛒 E-Commerce Customer Support")
st.write("Welcome! How can I help you today?")

st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Customer input
question = st.chat_input("Ask about your order...")

if question:

    # Display customer question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # AI response
    with st.chat_message("assistant"):

        try:
            with st.spinner("🤖 AI Agent is processing your request..."):

                response = customer_support(question)

            st.markdown(response)

            # Save AI response
            st.session_state.messages.append({
                "role": "assistant",
                "content": response
            })

        except Exception as e:
            st.error(f"Something went wrong: {e}")

# Sidebar
with st.sidebar:
    st.title("Customer Support")
    st.write("Your AI-powered shopping assistant.")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
