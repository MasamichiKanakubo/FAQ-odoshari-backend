from app.entities.schemas import Synonyms

class GPTRepository:
    def __init__(self, openai_api_key: str):
        self.openai_api_key = openai_api_key
        
    