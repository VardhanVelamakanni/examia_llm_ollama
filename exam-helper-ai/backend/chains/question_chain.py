def generate_questions(llm, retriever):
    docs = retriever.invoke("important exam questions")

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an exam assistant.
Based on the following study material, generate 5 important exam-oriented questions.

Study material:
{context}
"""

    return llm.invoke(prompt)
