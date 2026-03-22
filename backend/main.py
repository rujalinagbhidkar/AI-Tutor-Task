from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from llm_service import ask_tutor
from audio_service import text_to_speech
from fastapi import Body
import io

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def home():
    return FileResponse("frontend/index.html")


#Chat (LLM)
@app.get("/chat")
def chat(query: str):
    try:
        response = ask_tutor(query)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}


#Text-to-Speech 
@app.post("/speak")
def speak(text: str = Body(...)):
    try:
        audio = text_to_speech(text)
        return StreamingResponse(io.BytesIO(audio), media_type="audio/mpeg")
    except Exception as e:
        return {"error": str(e)}