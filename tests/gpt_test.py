from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "学生向けの税金事情に詳しい弁護士で、学生からのFAQに答えます。",
        },
        {
            "role": "user", 
            "content": "住民税に関する学生の支払い義務のFAQを1つ、具体的な金額を引用して教えてください. JSON形式でtitleとbodyを返してください。"
        },
    ],
)

print(completion.choices[0].message.content)
