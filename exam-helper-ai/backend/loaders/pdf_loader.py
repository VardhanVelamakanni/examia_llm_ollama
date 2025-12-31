from pypdf import PdfReader

def load_pdf(path: str) -> str:
    reader = PdfReader(path)
    text = ""

    for i, page in enumerate(reader.pages):
        print(f"Extracting page {i + 1}/{len(reader.pages)}")

        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text
