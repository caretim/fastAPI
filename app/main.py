from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from typing import Optional
from database import engine,get_db
from models import Question,Answer
from datetime import datetime
import models
import requests
from sqlalchemy.orm import Session # orm 세션 

from database import get_db
# 경로 동작은 순차적으로 지원됨 동일 경로롤 지나칠때 상위 경로에 지정되어있는주소가 있다면
# 그 주소로 먼저 도착하게됨, 개인페이지 이동시, user/me와 user/{user_id}일때, me를 먼저 선언해줘야 찾아갈 수 있음
#
# 지금까지는 GET방식이기에 URL 및 Request Header로 값이 넘어왔다.
#  하지만 POST방식에서는 Request Body로 넘어오기에 이전가지의 방식으로는 데이터를 받을 수 없다.
# Request Body는 Pydantic Model을 이용하여 값을 받을 수 있다.
# 1. from pydantic import BaseModel를 통해 class구성 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
db=[]


class City(BaseModel):
    name: str
    timezone:str
    is_offer: Union[bool , None] = None
    #None 명시는 초기값으로 필수로 안받아도 된다는뜻, 
    # 만약 설정을 안한다면 필수로 받아야함
    
@app.get("/")
async def root():
    return {"message": "루트페이지"}

@app.get("/login")
async def root():
    return {"signup": "회원가입페이지"}

#city 전체 조회
@app.get("/cities/")
async def get_items():
    results=[]
    for city in db:
        strs=f"http://worldtimeapi.org/timezone/{city['timezone']}"
        header = {"User-Agent": "Mozilla/5.0"}
        r= requests.get(strs,headers=header)
        print(r)
        cur_time=r.json()['datetime']
        results.append({'name':city['name'], 'timezone':city['timezone'] , 'current_time':cur_time})
    return results
#id조회 read
@app.get("/cities/{city_id}")
async def create_city(city_id:int):
    city = db[city_id-1]
    strs="http://worldtimeapi.org/timezone/Asia/Seoul"
    r= requests.get(strs)

    cur_time=r.json()['datetime']
    return {'name':city['name'],{'current_time'}:cur_time}

#생성
@app.post("/cities")
async def create_city(city:City):
    db.append(city.dict())

    return db[-1]

@app.delete("/cities/{city_id}")
async def delete_city(city_id:int):
    db.pop(city_id-1)

    return f"{city_id}번 삭제성공"


    
# 함수가 받은(반환도 하는) 값은 문자열 "3"이 아니라 파이썬 int 형인 3입니다.

# 즉, 타입 선언을 하면 FastAPI는 자동으로 요청을 "파싱"합니다.




