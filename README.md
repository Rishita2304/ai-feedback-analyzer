# 🧠 AI Feedback Analyzer

An AI-powered agent that automatically analyzes customer feedback, categorizes it, scores sentiment and urgency, and
generates a prioritized executive summary — built to demonstrate agentic AI product design.

## What it does

1. Takes raw customer feedback (bug reports, praise, feature requests, etc.)
2. Analyzes each item individually  categorizing it, scoring sentiment, and flagging urgency
3. **Agentic step:** Reasons across *all* analyzed feedback together to generate an executive report — top themes,
4.  most urgent issue, sentiment breakdown, and prioritized recommendations for the next sprint

## Tech stack

- Python
- Google Gemini API (gemini-2.5-flash)
- Streamlit (for the web app version)

## Files

- `analyzer.py` — command line version, analyzes a hardcoded feedback list and prints results to terminal
- `app.py` — interactive web app version (Streamlit)  paste in your own feedback and get results in-browser

## How to run

1. Clone this repo
2. Install dependencies: `pip install requests python-dotenv streamlit`
3. Create a `.env` file with your Gemini API key: `GEMINI_API_KEY=your_key_here`
4. Run the web app: `streamlit run app.py`

## Why I built this

As a product manager, one of the most time-consuming tasks is manually going through customer feedback to identify patterns and priorities.
This project explores how an AI agent can automate that first pass not replacing product judgment, but surfacing the right signals faster. 
Built this to understand agentic AI system design hands-on: prompt design, reasoning across multiple outputs, and handling real constraints like API rate limits.
