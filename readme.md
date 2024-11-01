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

## Introduction

```
This chatbot API leverages OpenAI's language models to process natural language queries, using Pinecone for enhanced retrieval and search functionality. The context for responses is provided through a pre-generated transcription file (`transcription.txt`), allowing the chatbot to provide answers based on specific content relevant to your application.

The API also includes a basic user interface (`index.html`) that allows users to interact with the chatbot directly from a browser. This setup is suitable for applications requiring contextual question-answering capabilities, including educational tools, customer support, and knowledge-based services.

## Prerequisites

- **Python** 3.8 or higher
- **OpenAI API Key** to access OpenAI's language models
- **Pinecone API Key** if using Pinecone for vector search
- **Node.js** (optional, if you need a local server for the HTML file)

## Setup

1. **Clone the Repository**:
   ```bash
   git clone <repo-url>
   cd chatbot-fastapi
2. ** install dependencis**:
```
pip install -r requirements.txt

3. ** configure environment variable**:
```
create .env file and do the following 

OPENAI_API_KEY=your_openai_api_key

PINECONE_API_KEY=your_pinecone_api_key

PINECONE_INDEX_NAME=your_index_name

4. ** Add the Transcription File **: 
```
Place your transcription.txt file in the project root. This file serves as the contextual source for the chatbot's responses.

5.** start the fastapi app**:
```

uvicorn main:app --reload
