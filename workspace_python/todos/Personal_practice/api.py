from fastapi import FastAPI, APIRouter
from crud import crud_router

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(crud_router)

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run("api:app", port=8000, reload=True, host="0.0.0.0")
