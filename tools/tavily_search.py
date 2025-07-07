# tools/tavily_search.py
from langchain_community.tools.tavily_search import TavilySearchResults

import os

# Export this so researcher_agent.py can import it
web_search_tool = TavilySearchResults (k=5)

def get_search_tool():
    return TavilySearchResults(k=5)  # top 5 results





