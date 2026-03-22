import requests
from config import ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID

def text_to_speech(text):

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1"
    }

    response = requests.post(url, json=data, headers=headers)

    return response.content