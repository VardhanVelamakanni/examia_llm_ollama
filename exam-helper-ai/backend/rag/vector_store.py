from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from sklearn.feature_extraction.text import TfidfVectorizer


class TfidfEmbeddings:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self._is_fitted = False

    def embed_documents(self, texts):
        if not self._is_fitted:
            vectors = self.vectorizer.fit_transform(texts)
            self._is_fitted = True
        else:
            vectors = self.vectorizer.transform(texts)
        return vectors.toarray().tolist()

    def embed_query(self, text):
        return self.vectorizer.transform([text]).toarray()[0].tolist()


def build_vector_store(text: str, persist_dir="./rag_db_tfidf"
):
    print("Vector store: starting")

    MAX_CHARS = 12000
    text = text[:MAX_CHARS]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    documents = splitter.create_documents([text])
    print(f"Vector store: {len(documents)} chunks created")

    texts = [doc.page_content for doc in documents]

    embeddings = TfidfEmbeddings()

    vectorstore = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        persist_directory=persist_dir
    )

    print("Vector store: finished")

    return vectorstore
