from fastapi import FastAPI

app = FastAPI(
    title="Mi Primera API",
    description="API de ejemplo para",
    version="1.0.0"
)

@app.get("/")
async def root() :
    """"Emd"""
