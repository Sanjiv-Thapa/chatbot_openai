from fastapi import APIRouter, HTTPException
from app.models import ChatRequest, ChatResponse
from app.core.chain import setup_chain
import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter

router = APIRouter()

# Load transcription once when the app starts
try:
    with open("transcription.txt", "r") as file:
        transcription_context = file.read()
except Exception as e:
    logging.error(f"Error loading transcription file: {e}")
    transcription_context = ""

# Define a function to truncate the context if it’s too long
def truncate_context(context, max_tokens=4000):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=max_tokens)
    chunks = text_splitter.split_text(context)
    return chunks[0]  # Use only the first chunk

@router.post("/chat", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest):
    try:
        if not transcription_context:
            raise ValueError("Transcription context is empty.")
        
        # Truncate the context to ensure it fits within model limits
        context = truncate_context(transcription_context)
        
        chain = setup_chain()
        answer = chain.invoke({
            "context": context,  # Use truncated context
            "question": request.question
        })
        return ChatResponse(answer=answer)
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
