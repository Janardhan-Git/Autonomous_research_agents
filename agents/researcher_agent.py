from langchain_groq import ChatGroq
import os
import json
from tools.tavily_search import web_search_tool

def run_researcher_agent(query):
    llm = ChatGroq(
        temperature=0.7,
        model_name="llama3-70b-8192",
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    # 🔍 Step 1: Get search results using Tavily
    raw_results = web_search_tool.run(query)

    # 🔄 Step 2: Parse JSON string into Python list (if needed)
    if isinstance(raw_results, str):
        try:
            results = json.loads(raw_results)
        except json.JSONDecodeError:
            return "Failed to parse Tavily results."

    else:
        results = raw_results  # Already parsed

    # 📚 Step 3: Combine all content into one big string
    combined_content = "\n\n".join([item["content"] for item in results if "content" in item])

    # 🧠 Step 4: Ask the LLM to summarize the combined info
    prompt = f"Summarize the following search results on the topic '{query}':\n\n{combined_content}"
    summary = llm.invoke(prompt)

    return summary
