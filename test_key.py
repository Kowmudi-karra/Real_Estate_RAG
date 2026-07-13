from dotenv import load_dotenv
import os

load_dotenv()

google_key = os.getenv("GOOGLE_API_KEY")
model = os.getenv("MODEL_NAME")

print("API Key:", google_key)
print("Model:", model)