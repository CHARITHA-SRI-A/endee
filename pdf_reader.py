from PyPDF2 import PdfReader
from pdfreader import extract_text

def extract_text(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text
