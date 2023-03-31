from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from database import engine
import models

#
# 지금까지는 GET방식이기에 URL 및 Request Header로 값이 넘어왔다.
#  하지만 POST방식에서는 Request Body로 넘어오기에 이전가지의 방식으로는 데이터를 받을 수 없다.
# Request Body는 Pydantic Model을 이용하여 값을 받을 수 있다.
# 1. from pydantic import BaseModel를 통해 class구성 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Model(BaseModel):
    name: str
    phoneNumber :int

@app.get("/")
async def root():
    return {"message": "루트페이지"}

@app.get("/login")
async def root():
    return {"signup": "회원가입페이지"}


@app.get("/cat")
async def cat():
    return{'고양이':'야옹'}


#post사용 방법 
@app.post("/send") # app.+메서드 
def data받음(data:Model):
    print(data)
    return '전송완료'




@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}




# 함수가 받은(반환도 하는) 값은 문자열 "3"이 아니라 파이썬 int 형인 3입니다.

# 즉, 타입 선언을 하면 FastAPI는 자동으로 요청을 "파싱"합니다.

