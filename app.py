
import streamlit as st
from customer_agent import customer_support

# Page configuration
st.set_page_config(
    page_title="AI Customer Support",
    page_icon="🤖",
    layout="centered"
)

# Page title
st.title("🤖 AI Customer Support Agent")
st.write("Welcome! Ask me about your order or request an order cancellation.")

st.divider()

# Customer question input
question = st.text_area(
    "Enter your question:",
    placeholder="Example: What is the status of my order? My order ID is 101.",
    height=120
)

# Submit button
if st.button("Submit", type="primary", use_container_width=True):

    if not question.strip():
        st.warning("Please enter your question first.")

    else:
        try:
            # Show loading spinner
            with st.spinner("AI Agent is processing your request..."):

                response = customer_support(question)

            # Display AI response
            st.success("Response generated successfully!")

            st.subheader("Customer Support Response")
            st.write(response)

        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.divider()

st.caption("Powered by LangChain, OpenAI and Streamlit")
