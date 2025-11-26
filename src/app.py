import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# UI Layout
st.set_page_config(page_title="AI Content Agent", page_icon="✨")
st.title("✨ AI Content Generation Agent")
st.write("Generate high-quality social media content instantly.")

# Input fields
prompt = st.text_area("Enter your topic or content request:")
tone = st.selectbox("Choose tone:", ["professional", "friendly", "engaging"])
length = st.selectbox("Choose length:", ["short", "medium", "long"])

# Button
if st.button("Generate Content"):
    with st.spinner("Generating…"):
        base_prompt = f"""
        You are a Content Creation AI Agent.
        Generate content based on:

        Topic: {prompt}
        Tone: {tone}
        Length: {length}

        Provide:
        1. A high-quality version
        2. A short version
        3. A highly engaging version
        """

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(base_prompt)

        st.subheader("✨ Output")
        st.write(response.text)
