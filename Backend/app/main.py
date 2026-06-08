import os ,subprocess,pathlib,json
from uuid import uuid4
from langchain_ollama import ChatOllama
from langchain_chroma import Chroma 
from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
from pydantic import BaseModel




##-----models-----##
class IngestRequest(BaseModel):
    repo_url:str

class QueryRequest(BaseModel):
    question:str
    repo_id:str






