# Real-Time AI Voice Tutor

## Overview

This project is a real-time, voice-based AI tutor that answers student questions strictly based on a provided lecture transcript. It simulates an interactive tutoring session using speech input, language model reasoning, and audio output.

---

## Features

* Voice input using browser Speech Recognition
* AI tutor powered by Azure OpenAI with strict grounding on transcript
* Text-to-speech using ElevenLabs for natural audio responses
* Real-time interaction with minimal latency
* Visual feedback states:

  * Listening
  * Thinking
  * Speaking
* Interactive UI with animated tutor avatar

---

## Architecture

User Speech → Speech-to-Text (Browser) → FastAPI Backend → Azure OpenAI → Response
→ ElevenLabs Text-to-Speech → Audio Output → UI Playback

---

## Tech Stack

* Frontend: HTML, CSS, JavaScript
* Backend: FastAPI (Python)
* LLM: Azure OpenAI
* Text-to-Speech: ElevenLabs
* Speech-to-Text: Web Speech API

---

## Grounding Constraint

The tutor is designed to:

* Answer only from the provided transcript
* Reject out-of-scope questions
* Avoid hallucinations
