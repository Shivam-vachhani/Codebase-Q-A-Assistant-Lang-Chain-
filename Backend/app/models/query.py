from pydantic import BaseModel
from typing import Literal

class QueryRequest(BaseModel):
    question:str
    repo_id:str
    model:Literal["gpt-4o","qwen-2.5"]