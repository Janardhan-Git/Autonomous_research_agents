# 🧠 Autonomous Research Agent

This is an AI-powered Flask application that:
- Uses Groq's LLaMA3 + Tavily Search to research any topic
- Generates a blog article with LangChain
- Exports to PDF and saves to Notion

## 🔧 Setup

1. `git clone ...`
2. `python -m venv venv && source venv/bin/activate`
3. `pip install -r requirements.txt`
4. Create a `.env` file:

GROQ_API_KEY=...
TAVILY_API_KEY=...
NOTION_API_KEY=...
NOTION_DB_ID=...