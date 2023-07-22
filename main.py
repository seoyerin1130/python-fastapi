//Hello API 만들기
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message" : "안녕하세요 파이보"}
