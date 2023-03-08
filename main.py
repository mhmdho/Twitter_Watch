from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def main():
    return {"hello": "world"}

@app.get("/items/{item}")
async def subpage(item: str):
    return {"item": item}

uvicorn.run(app, port = 8080, host = "0.0.0.0")
