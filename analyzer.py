import requests
from dotenv import load_dotenv
import os

load_dotenv()
import time

API_KEY = os.environ.get("GEMINI_API_KEY")
API_KEY = os.environ.get("GEMINI_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

feedback_list = [
    "The app crashes every time I try to upload a photo. Very frustrating.",
    "Love the new dashboard design! Much cleaner than before.",
    "Why is there no dark mode yet? Every other app has this.",
    "Customer support took 3 days to respond to my ticket. Not okay.",
    "Pricing is too high compared to competitors for the same features.",
    "The onboarding flow was smooth and easy to follow.",
]

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

# STEP 1: Analyze each piece of feedback individually
print("=" * 50)
print("INDIVIDUAL FEEDBACK ANALYSIS")
print("=" * 50)

all_results = []
for i, feedback in enumerate(feedback_list, 1):
    print(f"\n--- Feedback #{i} ---")
    print(f"Original: {feedback}")
    result = analyze_feedback(feedback)
    print(result)
    all_results.append(f"Feedback: {feedback}\nAnalysis: {result}")
    time.sleep(13) 

# STEP 2: Agentic step - reason across ALL results to produce an aggregate report
print("\n" + "=" * 50)
print("AGGREGATE SUMMARY REPORT")
print("=" * 50)

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

summary = call_gemini(summary_prompt)
print(summary)