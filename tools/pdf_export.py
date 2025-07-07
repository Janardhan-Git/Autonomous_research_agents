import markdown2
import pdfkit

def export_to_pdf(markdown_text: str, output_path: str):
    html = markdown2.markdown(markdown_text)
    pdfkit.from_string(html, output_path)
