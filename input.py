from myreader import extract_text

print("Welcome to Health Report Analyzer")

file_path = input("Enter your PDF file name: ")

text = extract_text(file_path)

query = input("Ask your question about the report: ")

if query.lower() in text.lower():
    print("Answer found in report:")
    print("->", query, "is mentioned in the report.")
else:
    print("No relevant information found.")
