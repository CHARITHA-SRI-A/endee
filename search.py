def search_answer(text, query):
    text = text.lower()
    query = query.lower()

    sentences = text.split(".")

    results = []

    for sentence in sentences:
        if query in sentence:
            results.append(sentence.strip())

    if results:
        return " ".join(results[:3])
    else:
        return "No relevant information found in report."
