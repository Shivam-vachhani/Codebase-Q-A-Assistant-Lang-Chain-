import pathlib,shutil
from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
from app.models.ingest import IngestRequest
from app.services.git_service import clone_repo
from app.services.loader_service import get_code_files
from app.services.chunking_service import chunk_files
from app.services.vector_service import ingest_documents_to_chroma
from app.services.rag_service import invalidate_cache

router = APIRouter()

@router.post('/ingest')
async def data_ingestion(req:IngestRequest):

    repo_id,path = clone_repo(str(req.repo_url))

    try:
        if not repo_id:
            raise HTTPException(status_code=400,detail="Clone repo failed please provaid valid url")
        else:
            print("Repo clonned....")
        files = get_code_files(path)
        print("Files loded....")
        chunks = chunk_files(files)
        print("Files chunked....") 
        response = ingest_documents_to_chroma(chunks,repo_id)
        print("Repo files stored....")
        print(response)

    finally:
        if path and pathlib.Path(path).exists():
            shutil.rmtree(path,ignore_errors=True)
            print(f"[Ingest] Cleaned up clone at {path}")

    if(response['status'] == "Success"):
        invalidate_cache(repo_id)
        return JSONResponse(
            status_code=200,
            content=response
            )   
    else:
        raise HTTPException(
            status_code=500,
            detail="Some error occure in storing file in vector store"
            )