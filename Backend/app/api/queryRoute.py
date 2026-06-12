from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
from app.models.query import QueryRequest
from app.services.rag_service import get_rag_service,invalidate_cache
router = APIRouter()

@router.post('/query')
def ask_query(req:QueryRequest):
    
    pipeline = get_rag_service(req.repo_id) 
    response = pipeline.run(req.question)

    if response:
        return JSONResponse(
            status_code=200,
            content={
            "query":req.question,
            "response":response,
            }
         )
    else:
        raise HTTPException(status_code=400,detail="Can't genrate response")
