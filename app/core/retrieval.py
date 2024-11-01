from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_pinecone import PineconeVectorStore
from app.core.embeddings import get_embeddings
from config.settings import settings

def setup_pinecone_vector_store(documents):
    embeddings = get_embeddings()
    pinecone_store = PineconeVectorStore.from_documents(
        documents,embeddings,index_name=settings.pinecone_index_name

    )
    return pinecone_store.as_retriever()
