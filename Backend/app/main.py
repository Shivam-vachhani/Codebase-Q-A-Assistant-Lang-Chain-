from fastapi import FastAPI
from app.api import ingestRoute,queryRoute

server = FastAPI(
    title= "Codebase Q&A Assistant API",
    version="1.0.0"
)

server.include_router(ingestRoute.router,tags=["Ingestion"])
server.include_router(queryRoute.router,tags=["Chatbot"])

@server.get("/")
def root():
    return {"message":"Codebase Q&A Assistant backend running successfully."}










