from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "오늘 저녁은 뭐먹지?"}



@app.get("/login")
async def root():
    return {"signup": "회원가입페이지"}