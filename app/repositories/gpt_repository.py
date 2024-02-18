from app.entities.schemas import Synonyms
from openai import OpenAI
from typing import Dict
import json


class GPTRepository:
    def __init__(self, client: OpenAI):
        self.client = client

    def generate_gpt4_answer(self, word: str) -> Dict[str, str]:
        messages = [
            {
                "role": "system",
                "content": "学生向けの税金事情に詳しい弁護士で、学生からのFAQに答えます。",
            },
            {
                "role": "user",
                "content": f"{word}に関する学生の支払い義務のFAQを1つ、具体的な金額を引用して教えてください. JSON形式で'page_title'と'descriptions'というフィールドを返してください。page_titleは質問部分、descriptionsは回答部分で配列として一行ごとに要素にして返してください",
            },
        ]
        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=messages,
        )
        answer = json.loads(completion.choices[0].message.content)

        return answer
