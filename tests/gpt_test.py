import os
from dotenv import load_dotenv
from openai import api_key, completions

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

response = completions.create(
    model="gpt-3.5-turbo",
    prompt="これはテストです。",
    temperature=0.7,
    max_tokens=100,
)
print(response)
