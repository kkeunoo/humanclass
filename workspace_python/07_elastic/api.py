from fastapi import FastAPI
from router.es_router import router as es_router

app = FastAPI()
app.include_router(es_router)

@app.get('/')
def home():
    return 'welcome!'

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run('api:app', port=8000, reload=True, host="0.0.0.0")