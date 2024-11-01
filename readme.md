# Chatbot API with FastAPI and OpenAI

This project is a chatbot API developed using FastAPI, integrated with OpenAI's language model and Pinecone for vector search. The chatbot can respond to user questions with context provided by a transcription file.

## Project Structure

```plaintext
chatbot-fastapi/
├── .env                     # Environment variables
├── main.py                  # Main FastAPI application file
├── requirements.txt         # Python dependencies
├── transcription.txt        # Pre-generated transcription file for chatbot context
├── config/
│   └── settings.py          # Settings configuration for environment variables
├── app/
│   ├── models.py            # Data models for requests and responses
│   ├── core/
│   │   ├── embeddings.py    # OpenAI embedding setup
│   │   ├── retrieval.py     # Pinecone retrieval setup
│   │   └── chain.py         # Chain setup for LangChain pipeline
│   └── routes/
│       └── chatbot.py       # Chatbot route for handling user questions
└── static/
    └── index.html           # Simple UI for user interaction
