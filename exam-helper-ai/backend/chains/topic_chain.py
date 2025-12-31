def generate_topics(llm, retriever):
    docs = retriever.get_relevant_documents("basic explanation of topics")
    context = "\n\n".join(d.page_content for d in docs)

    prompt = f"""
From the context below, list the main topics and give a short explanation
for each (3–4 lines).

Context:
{context}
"""

    return llm(prompt)
