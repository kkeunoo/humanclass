from fastapi import FastAPI
from router.es_router import router as es_router
from router.langchain_router import router as langchain_router
from router.langgraph_router import router as langgraph_router

app = FastAPI()
app.include_router(es_router)
app.include_router(langchain_router)
app.include_router(langgraph_router)

@app.get('/')
def home():
    return "hello world"

if __name__ == "__main__" :
    import uvicorn
    uvicorn.run('api:app', port=8000, reload=True, host='0.0.0.0')