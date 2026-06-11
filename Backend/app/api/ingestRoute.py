from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.ingest import IngestRequest

router = APIRouter()

@router.post('/ingest')
def data_ingestion(req:IngestRequest):
    

    return JSONResponse(
        status_code=200,
        content={
            "repo_url":str(req.repo_url)
        }
    )