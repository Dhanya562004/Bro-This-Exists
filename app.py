import streamlit as st
import json
import os
import re
import random
import time
import urllib.parse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="💀 Bro This Exists | Startup Idea Roaster",
    page_icon="💀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern glassmorphism aesthetic
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Main Container Padding */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 780px;
    }

    /* Gradient Title */
    .title-text {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FF4B4B 0%, #FF8F00 50%, #FF007A 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.2rem;
    }

    .subtitle-text {
        font-size: 1.15rem;
        color: #9CA3AF;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 400;
    }

    /* Card Styling */
    .result-card {
        background: rgba(22, 27, 34, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 16px;
        padding: 24px;
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        backdrop-filter: blur(10px);
    }

    /* Verdict Badges */
    .verdict-badge-build {
        display: inline-block;
        background: linear-gradient(135deg, #059669 0%, #10B981 100%);
        color: #ffffff;
        font-weight: 800;
        font-size: 1.3rem;
        padding: 8px 20px;
        border-radius: 30px;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);
        text-align: center;
    }

    .verdict-badge-maybe {
        display: inline-block;
        background: linear-gradient(135deg, #D97706 0%, #F59E0B 100%);
        color: #ffffff;
        font-weight: 800;
        font-size: 1.3rem;
        padding: 8px 20px;
        border-radius: 30px;
        box-shadow: 0 0 15px rgba(245, 158, 11, 0.4);
        text-align: center;
    }

    .verdict-badge-donot {
        display: inline-block;
        background: linear-gradient(135deg, #DC2626 0%, #EF4444 100%);
        color: #ffffff;
        font-weight: 800;
        font-size: 1.3rem;
        padding: 8px 20px;
        border-radius: 30px;
        box-shadow: 0 0 15px rgba(239, 68, 68, 0.4);
        text-align: center;
    }

    /* Callout Boxes */
    .explanation-box {
        background: rgba(139, 92, 246, 0.12);
        border-left: 4px solid #8B5CF6;
        border-radius: 8px;
        padding: 14px 18px;
        margin: 16px 0;
        color: #E2E8F0;
        font-size: 1.05rem;
    }

    .pivot-box {
        background: rgba(16, 185, 129, 0.12);
        border-left: 4px solid #10B981;
        border-radius: 8px;
        padding: 14px 18px;
        margin: 16px 0;
        color: #E2E8F0;
        font-size: 1.05rem;
    }

    .funny-line-box {
        background: rgba(245, 158, 11, 0.12);
        border: 1px dashed rgba(245, 158, 11, 0.4);
        border-radius: 8px;
        padding: 12px 16px;
        margin-top: 14px;
        color: #FCD34D;
        font-style: italic;
        font-size: 0.95rem;
    }

    /* Similar Products Chips */
    .chip {
        display: inline-block;
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        color: #F3F4F6;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.9rem;
        margin: 4px 4px 4px 0;
    }

    /* Custom Submit Button */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #FF4B4B 0%, #FF8F00 100%);
        color: white;
        font-size: 1.1rem;
        font-weight: 700;
        border: none;
        border-radius: 12px;
        padding: 12px 28px;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
    }

    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.5);
    }

    /* Hide Streamlit Menu / Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# List of funny random quotes
FUNNY_QUOTES = [
    "Even your senior tried this in 3rd year and gave up after 2 commits.",
    "Y Combinator rejected 40 versions of this during lunch yesterday.",
    "Sam Altman just sighed somewhere in San Francisco.",
    "A 16-year-old on Twitter built this exact project during history class.",
    "SoftBank lost $100M on this exact business model in 2021.",
    "There are already 14 open-source GitHub repos doing this with 0 stars.",
    "Your pitch deck for this would make VCs check their watches in 12 seconds.",
    "This idea has been born and died 5 times on ProductHunt this month."
]

def get_fallback_analysis(idea: str, mode: str) -> dict:
    """Intelligent offline fallback analysis if API key is missing or fails."""
    idea_lower = idea.lower()
    
    # Simple heuristic scoring based on common cliché keywords
    cliches = ["uber for", "tinder for", "ai wrapper", "crypto", "nft", "social network for", "dating app for", "dog walking", "cold email"]
    is_cliche = any(c in idea_lower for c in cliches)
    
    if is_cliche or len(idea) < 15:
        score = random.randint(1, 3)
        saturation = "High 🔴"
        verdict = "DO NOT BUILD"
    elif len(idea) > 80:
        score = random.randint(6, 9)
        saturation = "Low 🟢" if "niche" in idea_lower or "b2b" in idea_lower else "Medium 🟡"
        verdict = "BUILD" if score >= 7 else "MAYBE"
    else:
        score = random.randint(3, 6)
        saturation = "Medium 🟡"
        verdict = "MAYBE"

    if mode == "Savage 😈":
        explanation = f"💀 Bro... this is literally just another generic pitch. VCs will fall asleep before slide 2." if is_cliche else f"💀 Sounds cool in your shower thoughts, but good luck fighting 50 VC-backed startups with $20M war chests."
    else:
        explanation = f"😇 It's a crowded market! Many startups have tried similar concepts, so standard execution will be tough." if is_cliche else f"😇 Interesting concept, though user acquisition might be your main bottleneck."

    similar = ["GenericStartup.io", "Appify (YC W22)", "PivotNow", "Copycat.ai"] if is_cliche else ["SimilarApp Inc.", "NicheTool", "MarketLeader AI"]
    pivot = f"Focus strictly on a hyper-niche audience (e.g., enterprise B2B compliance instead of general consumers)."

    return {
        "similar_products": similar,
        "originality_score": score,
        "market_saturation": saturation,
        "explanation": explanation,
        "niche_pivot": pivot,
        "verdict": verdict,
        "funny_line": random.choice(FUNNY_QUOTES)
    }

def analyze_idea_with_llm(idea: str, mode: str, api_key: str = None) -> dict:
    """Analyze idea using Gemini or OpenAI API, fallback if unavailable."""
    # Check for API key in args, env, or secrets
    key = api_key or os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY")
    
    # Try Streamlit secrets if not found
    if not key and hasattr(st, "secrets"):
        key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

    if not key:
        return get_fallback_analysis(idea, mode)

    prompt = f"""
You are "Bro This Exists", a viral, sarcastic, yet insightful startup validator tool.
Analyze this startup idea: "{idea}"

Mode: {mode}

Tone Requirements:
- Keep all responses short (1-2 lines maximum per field).
- Use relevant emojis.
- Witty, sarcastic, punchy.
- If Mode is "Savage 😈", be brutally honest, hilarious, and slightly roasting (never hateful/offensive).
- If Mode is "Normal 😇", be lighthearted, constructive, with mild sarcastic humor.

Output strictly valid JSON with this schema:
{{
  "similar_products": ["Product 1", "Product 2", "Product 3"],
  "originality_score": <number between 1 and 10>,
  "market_saturation": "<Low / Medium / High>",
  "explanation": "<Short 1-2 line punchy explanation/roast>",
  "niche_pivot": "<Short 1-2 line better/niche alternative angle>",
  "verdict": "<BUILD or MAYBE or DO NOT BUILD>",
  "funny_line": "<One random funny line about this idea>"
}}
"""

    # Try Gemini API if available
    try:
        import google.generativeai as genai
        genai.configure(api_key=key)
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        text = response.text.strip()
        
        # Clean JSON block formatting
        cleaned_json = re.sub(r"```(?:json)?", "", text).strip("`\n ")
        data = json.loads(cleaned_json)
        return data
    except Exception as e:
        # Try OpenAI API if Gemini fails or if key is OpenAI key
        try:
            from openai import OpenAI
            client = OpenAI(api_key=key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"}
            )
            data = json.loads(response.choices[0].message.content)
            return data
        except Exception as e2:
            # Safe fallback
            return get_fallback_analysis(idea, mode)

# Header Section
st.markdown("<h1 class='title-text'>💀 Bro This Exists</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-text'>Paste your startup idea. Find out if you’re a genius… or late to the party.</p>", unsafe_allow_html=True)

# Sidebar settings & API option
with st.sidebar:
    st.header("⚙️ Settings & API")
    user_api_key = st.text_input("Gemini / OpenAI API Key (Optional)", type="password", help="If left blank, our smart offline roast engine will analyze your idea.")
    
    st.markdown("---")
    st.markdown("### 💡 Preset Examples")
    if st.button("🐶 Uber for Dog Walking"):
        st.session_state["idea_input"] = "An app like Uber but for on-demand luxury dog walking and pet spa services."
    if st.button("📧 AI Cold Email Sender"):
        st.session_state["idea_input"] = "An AI agent that writes and sends personalized cold emails to CEOs on LinkedIn."
    if st.button("🏠 Tinder for Roommates"):
        st.session_state["idea_input"] = "Swipe left or right to find your ideal college roommate based on sleep schedule and cleanliness."

# Initialize Session State
if "idea_input" not in st.session_state:
    st.session_state["idea_input"] = ""

# Input Form
idea_input = st.text_area(
    "Enter your startup idea",
    value=st.session_state["idea_input"],
    placeholder="e.g., An AI-powered app that automatically cancels unused subscriptions...",
    height=110
)

# Mode Toggle
col_mode1, col_mode2 = st.columns([1, 1])
with col_mode1:
    mode = st.radio(
        "Select Roast Mode:",
        ["Normal 😇", "Savage 😈"],
        horizontal=True,
        index=1
    )

# Action Button
check_button = st.button("🚀 Check Idea")

if check_button:
    if not idea_input.strip():
        st.warning("⚠️ Please enter a startup idea first, bro!")
    else:
        # Animated loading spinner with humorous step updates
        with st.spinner("Checking if your idea is already stolen..."):
            time.sleep(0.6)
            analysis = analyze_idea_with_llm(idea_input, mode, api_key=user_api_key)

        st.session_state["last_analysis"] = analysis
        st.session_state["last_idea"] = idea_input

# Display Results Card if available
if "last_analysis" in st.session_state:
    analysis = st.session_state["last_analysis"]
    
    verdict = analysis.get("verdict", "MAYBE").upper()
    score = int(analysis.get("originality_score", 5))
    saturation = analysis.get("market_saturation", "Medium")
    similar_list = analysis.get("similar_products", ["Similar Product A", "Similar Product B"])
    explanation = analysis.get("explanation", "")
    pivot = analysis.get("niche_pivot", "")
    funny_line = analysis.get("funny_line", random.choice(FUNNY_QUOTES))

    # Determine Verdict Badge HTML
    if "BUILD" in verdict and "NOT" not in verdict:
        verdict_html = "<div class='verdict-badge-build'>🚀 VERDICT: BUILD IT NOW</div>"
    elif "MAYBE" in verdict:
        verdict_html = "<div class='verdict-badge-maybe'>🤔 VERDICT: MAYBE / PIVOT</div>"
    else:
        verdict_html = "<div class='verdict-badge-donot'>💀 VERDICT: DO NOT BUILD</div>"

    # Main Card Container
    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    
    # Top Verdict
    st.markdown(f"<div style='text-align: center; margin-bottom: 20px;'>{verdict_html}</div>", unsafe_allow_html=True)
    
    # Originality Score & Progress Bar
    st.markdown(f"**🔥 Originality Score:** {score}/10")
    st.progress(score / 10.0)

    # Columns for Similar Products & Market Saturation
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**💀 Similar Products:**")
        chips_html = "".join([f"<span class='chip'>{prod}</span>" for prod in similar_list])
        st.markdown(chips_html, unsafe_allow_html=True)

    with col2:
        st.markdown("**⚠️ Market Saturation:**")
        st.markdown(f"### {saturation}")

    # Short Explanation
    st.markdown(f"""
    <div class='explanation-box'>
        <strong>😈 The Roast:</strong><br/>
        {explanation}
    </div>
    """, unsafe_allow_html=True)

    # Better / Niche Version
    st.markdown(f"""
    <div class='pivot-box'>
        <strong>💡 Better / Niche Angle:</strong><br/>
        {pivot}
    </div>
    """, unsafe_allow_html=True)

    # Funny Random Quote
    st.markdown(f"""
    <div class='funny-line-box'>
        💬 <strong>VC Real Talk:</strong> "{funny_line}"
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Copy and Share Section
    st.markdown("### 📢 Share & Export")
    
    # Formatted output text for copying
    full_text = f"""💀 BRO THIS EXISTS - STARTUP ROAST 💀
Idea: {st.session_state.get('last_idea', '')}
Verdict: {verdict}
Originality Score: {score}/10
Market Saturation: {saturation}
Similar Products: {', '.join(similar_list)}
Roast: {explanation}
Better Niche Angle: {pivot}
VC Real Talk: {funny_line}
"""
    
    col_copy, col_share = st.columns([1, 1])
    
    with col_copy:
        st.markdown("**📋 Copy Full Result:**")
        st.code(full_text, language=None)

    with col_share:
        st.markdown("**🐦 Share on X / Twitter:**")
        tweet_text = f"I ran my startup idea through 'Bro This Exists' 💀\nVerdict: {verdict}\nOriginality: {score}/10 🔥\n\nRoast: {explanation[:100]}...\nCheck yours at Bro This Exists!"
        tweet_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(tweet_text)}"
        st.markdown(f"""
        <a href="{tweet_url}" target="_blank" style="text-decoration: none;">
            <button style="
                background-color: #1DA1F2;
                color: white;
                border: none;
                padding: 10px 18px;
                border-radius: 8px;
                font-weight: 700;
                cursor: pointer;
                width: 100%;
                margin-top: 5px;
            ">
                🐤 Share Roast on Twitter
            </button>
        </a>
        """, unsafe_allow_html=True)
