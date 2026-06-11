from pydantic import BaseModel

class QueryRequest(BaseModel):
    question:str
    repo_id:str