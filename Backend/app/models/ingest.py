from pydantic import BaseModel,AnyUrl

class IngestRequest(BaseModel):
    repo_url:AnyUrl

