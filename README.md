# Real-Time AI Voice Tutor
Overview

This project is a real-time, voice-based AI tutor that answers student questions strictly based on a provided lecture transcript.
It simulates an interactive tutoring session using speech input, LLM reasoning, and audio output.

🚀 Features
🎤 Voice Input using browser Speech Recognition
🧠 AI Tutor (Azure OpenAI) with strict grounding on transcript
🔊 Text-to-Speech (ElevenLabs) for natural voice responses
⚡ Real-time Interaction with minimal latency
🎬 Visual Feedback States
Listening
Thinking
Speaking
🤖 Interactive UI with animated tutor avatar
🏗️ Architecture

User Speech → STT (Browser) → FastAPI Backend → Azure OpenAI → Response
→ ElevenLabs TTS → Audio Output → UI Playback

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: FastAPI (Python)
LLM: Azure OpenAI
TTS: ElevenLabs
STT: Web Speech API
🔒 Grounding Constraint

The tutor:

Answers ONLY from the provided transcript
Rejects out-of-scope questions
Avoids hallucinations
