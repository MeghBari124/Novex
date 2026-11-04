import os
from google import genai
from dotenv import load_dotenv
import traceback

load_dotenv()

def test_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key: return

    try:
        client = genai.Client(api_key=api_key)
        print("TRYING GENERATE CONTENT (gemini-flash-lite-latest)...")
        response = client.models.generate_content(
            model='gemini-flash-lite-latest',
            contents="Say 'API is working' if you see this."
        )
        print("SUCCESS! Resp: " + response.text.strip())
    except Exception as e:
        print("ERROR:")
        traceback.print_exc()

if __name__ == "__main__":
    test_gemini()
