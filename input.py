from pdf_reader import extract_text
from search import search_answer

print("=== Health Report Analyzer ===")

pdf_path = input("Enter PDF file path: ")
query = input("Ask your question: ")

text = extract_text(pdf_path)

answer = search_answer(text, query)

print("\nAnswer:")
print(answer)
