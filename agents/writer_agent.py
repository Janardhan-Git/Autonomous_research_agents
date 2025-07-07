import os
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def generate_blog(research_summary: str) -> str:
    # Create the LLM instance
    llm = ChatGroq(
        model_name="llama3-70b-8192",
        temperature=0.7,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    # Create the prompt
    prompt = PromptTemplate(
        input_variables=["summary"],
        template="""
You are a professional blog writer and editor.
Using the following research summary, write a well-formatted article in Markdown with:
- A compelling Title
- A TL;DR section
- Headings and subheadings
- Bullet points if needed
- A strong Conclusion

Research Summary:
---
{summary}
---
Make it clear, informative, and SEO-optimized.
"""
    )

    # Create the LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)

    # Run the chain with input
    return chain.run({"summary": research_summary})
