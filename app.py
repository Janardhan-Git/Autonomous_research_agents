from flask import Flask, request, render_template
from agents.researcher_agent import run_researcher_agent
from agents.writer_agent import generate_blog
from tools.pdf_export import export_to_pdf
from tools.notion_client import save_to_notion
from openai import OpenAIError, RateLimitError
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")
notion_key = os.getenv("NOTION_API_KEY")

app = Flask(__name__)

def save_output(article: str, title: str) -> tuple:
    os.makedirs("output", exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    md_filename = f"output/blog_{timestamp}.md"
    pdf_filename = f"output/blog_{timestamp}.pdf"

    # Save markdown
    with open(md_filename, "w", encoding="utf-8") as f:
        f.write(article)

    # Export to PDF
    export_to_pdf(article, pdf_filename)

    # Save to Notion
    save_to_notion(title, article, os.getenv("NOTION_DB_ID"))

    return md_filename, pdf_filename

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    error = ""
    if request.method == "POST":
        topic = request.form["topic"]
        try:
            research = run_researcher_agent(topic)
            output = generate_blog(research)
            save_output(output, topic)
        except RateLimitError:
            error = "⚠️ OpenAI rate limit exceeded. Try again later or check your quota."
        except OpenAIError as e:
            error = f"OpenAI Error: {str(e)}"
        except Exception as e:
            error = f"Unexpected error: {str(e)}"
    return render_template("index.html", output=output, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
