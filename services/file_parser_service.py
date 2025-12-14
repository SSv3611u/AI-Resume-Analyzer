import pdfplumber
import docx

def extract_text(file):
    if file.filename.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"
        return text
    elif file.filename.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join(p.text for p in doc.paragraphs)
    return ""