import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
import time
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def call_gemini(prompt):
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(URL, json=payload)
    data = response.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        return f"Error: {data}"

def analyze_feedback(feedback_text):
    prompt = f"""
    Analyze this piece of customer feedback and respond in this exact format:

    Category: [Bug / Feature Request / Praise / Complaint / Pricing / UX]
    Sentiment: [Positive / Negative / Neutral]
    Urgency: [Low / Medium / High]
    Summary: [one sentence summary]

    Feedback: "{feedback_text}"
    """
    return call_gemini(prompt)

st.set_page_config(page_title="AI Feedback Analyzer", layout="centered")
st.title("🧠 AI Feedback Analyzer")
st.write("Paste customer feedback below (one per line) and let the AI agent analyze it.")

default_text = """The app crashes every time I try to upload a photo. Very frustrating.
Love the new dashboard design! Much cleaner than before.
Why is there no dark mode yet? Every other app has this.
Customer support took 3 days to respond to my ticket. Not okay.
Pricing is too high compared to competitors for the same features.
The onboarding flow was smooth and easy to follow."""

user_input = st.text_area("Feedback (one per line):", value=default_text, height=200)

if st.button("Analyze Feedback"):
    feedback_list = [line.strip() for line in user_input.split("\n") if line.strip()]
    
    all_results = []
    with st.spinner("Analyzing individual feedback..."):
        for i, feedback in enumerate(feedback_list, 1):
            result = analyze_feedback(feedback)
            with st.expander(f"Feedback #{i}: {feedback[:50]}..."):
                st.write(f"**Original:** {feedback}")
                st.write(result)
            all_results.append(f"Feedback: {feedback}\nAnalysis: {result}")
            time.sleep(13)

    st.divider()
    st.subheader("📊 Aggregate Summary Report")
    
    combined_results = "\n\n".join(all_results)
    summary_prompt = f"""
    You are a product manager reviewing analyzed customer feedback below.
    Based on ALL the feedback and its analysis, produce a concise executive report with:

    1. Top 3 recurring themes (with rough frequency)
    2. Most urgent issue that needs immediate attention
    3. Overall sentiment breakdown (% positive/negative/neutral, estimate is fine)
    4. Top 2 product priority recommendations for next sprint, with brief reasoning

    Here is the analyzed feedback data:

    {combined_results}
    """
    with st.spinner("Generating executive summary..."):
        summary = call_gemini(summary_prompt)
    st.markdown(summary)