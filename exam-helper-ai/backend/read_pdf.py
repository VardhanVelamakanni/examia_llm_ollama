from pypdf import PdfReader

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


# TEST (temporary)
if __name__ == "__main__":
    content = read_pdf("40819_Author Instructions_2023.pdf")
    print(content)
