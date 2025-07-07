from notion_client import Client
import os

notion = Client(auth=os.getenv("NOTION_API_KEY"))

def save_to_notion(title: str, content: str, database_id: str):
    notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "Name": {"title": [{"text": {"content": title}}]}
        },
        children=[
            {"object": "block", "type": "paragraph", "paragraph": {"text": [{"type": "text", "text": {"content": content}}]}}
        ]
    )
