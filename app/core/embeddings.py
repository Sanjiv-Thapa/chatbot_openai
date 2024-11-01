from langchain_openai.embeddings import OpenAIEmbeddings
from config.settings import settings


def get_embeddings():
    return OpenAIEmbeddings(openai_api_key=settings.openai_api_key)