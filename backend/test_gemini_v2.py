import os
from dotenv import load_dotenv
from google import genai
import time

# Load env
env_path = os.path.join(os.getcwd(), '.env')
load_dotenv(env_path)
api_key = os.getenv("GEMINI_API_KEY")

print(f"Testing with key: {api_key[:10]}...")
print(f"Model: gemini-2.5-flash")

client = genai.Client(api_key=api_key)
try:
    start_time = time.time()
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='Hello, response with one word.'
    )
    duration = time.time() - start_time
    print(f"Response: {response.text}")
    print(f"Success! Took {duration:.2f}s")
except Exception as e:
    print(f"Error: {e}")
