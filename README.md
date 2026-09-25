# 💀 Bro This Exists

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Gemini_AI-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Gemini AI" />
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License" />
</p>

<h3 align="center">
  <em>“Paste your startup idea. Find out if you're a genius… or late to the party.”</em>
</h3>

<p align="center">
  A viral-style AI web app that evaluates startup ideas and gives a humorous, slightly savage roast along with actionable, niche-focused insights.
  <br /><br />
  🚀 <strong><a href="https://bro-this-exists-mmfhq4vb5nkfbrettsycds.streamlit.app/">Try the Live Demo Here</a></strong> 🚀
</p>

---

## 🌐 Live Demo

👉 **Click here to test your startup idea**: [https://bro-this-exists-mmfhq4vb5nkfbrettsycds.streamlit.app/](https://bro-this-exists-mmfhq4vb5nkfbrettsycds.streamlit.app/)

---

## 📸 Screenshots

> *(Add app screenshots or GIFs here)*

| 💀 Savage Mode Roast | 🚀 Build Verdict & Score |
| :---: | :---: |
| `![App Preview 1](https://via.placeholder.com/400x250?text=Savage+Mode+Roast)` | `![App Preview 2](https://via.placeholder.com/400x250?text=Build+Verdict+%26+Score)` |

---

## 🔥 Features

- 💀 **Similar Products Radar**: Instant detection of 3–5 existing startups or competitors.
- 🔥 **Originality Score Bar**: Visual 1–10 progress score of your idea's uniqueness.
- ⚠️ **Market Saturation Gauge**: Clear breakdown (`Low 🟢` / `Medium 🟡` / `High 🔴`).
- 😈 **Dual Tone Roasts**:
  - **Normal 😇 Mode**: Mild, lighthearted, constructive feedback.
  - **Savage 😈 Mode**: Brutally honest, hilarious, VC-grade roast.
- 💡 **Better / Niche Pivot**: Smart, actionable alternative angle to save a cliché idea.
- 🚀 **Final Verdict Badge**:
  - `BUILD` (Neon Green)
  - `MAYBE / PIVOT` (Vivid Amber)
  - `DO NOT BUILD` (Neon Crimson)
- 💬 **VC Real Talk**: Random humorous lines (*"Even your senior tried this in 3rd year and gave up"*).
- 📋 **1-Click Copy & Share**: Instant result text export and direct Twitter / X sharing button.
- ⚡ **Works Offline**: Includes a smart heuristic offline roast engine so it works 100% of the time, with or without an API key!

---

## 🛠️ Tech Stack

- **Frontend / Framework**: [Streamlit](https://streamlit.io/) (Custom dark glassmorphism layout)
- **Programming Language**: [Python 3.10+](https://www.python.org/)
- **AI Models**: Google Gemini 2.0 Flash (`google-generativeai`) & OpenAI GPT-4o-mini (`openai`)
- **Fallback Engine**: Custom heuristic roast generator for zero-downtime offline execution.

---

## 📂 Project Structure

```text
Bro-This-Exists/
├── app.py                   # Main application entry point & custom CSS styling
├── requirements.txt         # Project dependencies
├── README.md                # Comprehensive documentation
├── .env_example             # Environment variables example template
├── .gitignore               # Excludes secrets, bytecode, and virtual environments
└── .streamlit/
    └── secrets.toml         # Secure local API key configuration (Ignored by Git)
```

---

## ⚙️ Environment Variables & API Key Setup

An API key is **optional** because the app includes a smart offline roast engine. However, to enable live AI responses:

### 1. Local Secrets (`.streamlit/secrets.toml` - Recommended)
Create `.streamlit/secrets.toml` (which is automatically ignored by git):

```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
# OR
OPENAI_API_KEY = "your_openai_api_key_here"
```

### 2. Environment File (`.env`)
Alternatively, create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Dhanya562004/Bro-This-Exists.git
cd Bro-This-Exists
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run app.py
```

The app will launch at `http://localhost:8501`.

---

## 🔮 Future Improvements

- [ ] 📊 **ProductHunt & Crunchbase API Integration**: Live web search validation for real-time market data.
- [ ] 📄 **Auto Pitch Deck Generator**: Generate a 1-page PDF pitch summary for viable ideas.
- [ ] 🎨 **Shareable Image Cards**: Generate downloadable social media screenshots of roasts.
- [ ] 🤖 **Investor Persona Simulator**: Choose roasts from specific VC personas (e.g., YC Partner, Angel Investor, Tech Twitter Bro).

---

## 👩‍💻 Author

Crafted with 💀 and ❤️ by **[Dhanya](https://github.com/Dhanya562004)**

- **GitHub**: [@Dhanya562004](https://github.com/Dhanya562004)
- **Live Demo**: [bro-this-exists.streamlit.app](https://bro-this-exists-mmfhq4vb5nkfbrettsycds.streamlit.app/)

---

<p align="center">
  If you enjoyed this project, give it a ⭐️ on <a href="https://github.com/Dhanya562004/Bro-This-Exists">GitHub</a>!
</p>
