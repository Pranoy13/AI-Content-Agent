import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env variables (only local use)
load_dotenv()

# Configure Gemini API key (works on Streamlit Secrets too)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# UI Setup
st.set_page_config(page_title="AI Content Agent", page_icon="✨")
st.title("✨ AI Content Generation Agent")
st.write("Generate high-quality social media content instantly.")

# User Inputs
prompt = st.text_area("Enter your topic or content request:")
tone = st.selectbox("Choose tone:", ["professional", "friendly", "engaging"])
length = st.selectbox("Choose length:", ["short", "medium", "long"])

# Generate Button
if st.button("Generate Content"):
    try:
        model = genai.GenerativeModel("gemini-pro")   # FIXED MODEL NAME

        full_prompt = f"""
        You are a Content Generation AI Agent.
        Generate content using the following details:

        Topic: {prompt}
        Tone: {tone}
        Length: {length}

        Provide:
        1. A high-quality version
        2. A short version
        3. A highly engaging version
        """

        response = model.generate_content(full_prompt)

        # Display Output
        st.subheader("✨ Output")
        st.write(response.text)

    except Exception as e:
        st.error("❌ Error occurred: " + str(e))
