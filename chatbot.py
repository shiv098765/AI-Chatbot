import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load API Key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="Gemini Chatbot", layout="centered")

st.title("🤖 Gemini AI Chatbot")

prompt = st.text_input("💬 Ask anything:")

if st.button("🚀 Get Answer"):
    if prompt:
        try:
            llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash",
                google_api_key=GOOGLE_API_KEY
            )
            response = llm.invoke([HumanMessage(content=prompt)])
            st.success("✅ Answer:")
            st.write(response.content)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt")
