def generate_answers(llm, questions, retriever):
    docs = retriever.invoke("detailed answers for exam questions")

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an exam assistant.
Using the study material below, answer the questions clearly and concisely.

Study material:
{context}

Questions:
{questions}
"""

    return llm.invoke(prompt)
