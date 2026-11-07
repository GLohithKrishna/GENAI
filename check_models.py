import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env", override=True)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

for model in client.models.list():
    if "generateContent" in (getattr(model, "supported_actions", []) or []):
        print(model.name)
