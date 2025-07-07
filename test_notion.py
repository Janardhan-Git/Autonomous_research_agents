# test_notion.py
from notion_client import Client
import os
from dotenv import load_dotenv

load_dotenv()

notion = Client(auth=os.getenv("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"))

try:
    result = notion.databases.retrieve(database_id=os.getenv("229f723eda7b80748350000c29ca39b4"))
    print("✅ Valid Notion credentials!")
    print("Database name:", result["title"][0]["text"]["content"])
except Exception as e:
    print("❌ Notion credentials error:", e)
