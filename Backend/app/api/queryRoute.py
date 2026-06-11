from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.query import QueryRequest
router = APIRouter()

@router.post('/query')
def ask_query(req:QueryRequest):
    return JSONResponse(
        status_code=200,
        content={
            "query":req.question,
            "repo_id":req.repo_id,
        }
    )
    
