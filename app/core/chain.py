from app.core.retrieval import setup_pinecone_vector_store
from langchain.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from config.settings import settings

prompt_template = """
Answer the question based on the context below. if you cant answetr, reply i dont know.
Context:{context}
Question:{question}
"""

def setup_chain():
    model = ChatOpenAI(openai_api_key = settings.openai_api_key,model="gpt-3.5-turbo")
    prompt = ChatPromptTemplate.from_template(prompt_template)
    parser = StrOutputParser()
    return prompt|model|parser
