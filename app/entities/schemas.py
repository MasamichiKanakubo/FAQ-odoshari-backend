from pydantic import BaseModel
from typing import List, Optional

class Synonyms(BaseModel):
    synonyms_list: Optional[List[str]] = None
    
    