import requests
from config import TRANSCRIPT_URL

def load_transcript():
    response = requests.get(TRANSCRIPT_URL)
    srt_data = response.text

    lines = srt_data.split("\n")
    clean_text = []

    for line in lines:
        if "-->" not in line and not line.strip().isdigit():
            clean_text.append(line)

    return " ".join(clean_text)

TRANSCRIPT = load_transcript()