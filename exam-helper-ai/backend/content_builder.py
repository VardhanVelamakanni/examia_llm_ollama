from read_pdf import read_pdf
from read_ppt import read_ppt

def build_content(pdf_path=None, ppt_path=None):
    content = ""

    if pdf_path:
        content += "\n--- PDF CONTENT ---\n"
        content += read_pdf(pdf_path)

    if ppt_path:
        content += "\n--- PPT CONTENT ---\n"
        content += read_ppt(ppt_path)

    return content
