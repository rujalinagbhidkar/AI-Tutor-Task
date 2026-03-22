from langchain_openai import AzureChatOpenAI
from langchain.messages import HumanMessage, SystemMessage
from config import *
from transcript import TRANSCRIPT

llm = AzureChatOpenAI(
    azure_deployment=AZURE_OPENAI_DEPLOYMENT_NAME,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2025-01-01-preview",
    temperature=0.3,
    max_tokens=300
)

def ask_tutor(query):

    system_prompt = f"""
You are an AI tutor.

STRICT RULES:
- Answer ONLY using the transcript
- If not present, say:
"I’m sorry, this topic is not covered in the current lesson."

STYLE:
- Keep answers concise (3–5 lines)
- Explain clearly like a teacher

TRANSCRIPT:
{TRANSCRIPT[:5000]}
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=query)
    ]

    response = llm.invoke(messages)

    return response.content