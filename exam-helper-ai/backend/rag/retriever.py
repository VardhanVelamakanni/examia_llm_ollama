def get_retriever(vectorstore, k=2):
    return vectorstore.as_retriever(search_kwargs={"k": k})
