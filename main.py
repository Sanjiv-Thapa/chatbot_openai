from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import chatbot
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Allow CORS for all origins (for testing purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include the chatbot API routes
app.include_router(chatbot.router)

# Serve index.html at the root URL
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")  # Make sure "index.html" exists in the "static" directory

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
