import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def list_models():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key: return
    client = genai.Client(api_key=api_key)
    with open("full_model_list.txt", "w") as f:
        for m in client.models.list():
            f.write(m.name + "\n")

if __name__ == "__main__":
    list_models()
