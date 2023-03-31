
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SERECT_FILE = os.path.join(BASE_DIR, 'serects.json')
serects = json.loads(open(SERECT_FILE).read())
DB = serects["DB"]

# DB_URL은 "mysql+pymysql://[유저이름]:[비밀번호]@[호스트주소]:[포트번호]/[스키마이름]?charset=utf8"로 구성된다.

# engine: DB엔진을 만든다.
# SessionLocal: 데이터베이스 세션 클래스, 이를 이용해 생성한 인스턴스가 실제 데이터베이스 세션이 된다.
# Base: DB모델이나 클래스를 만들기 위해 선언한 클래스(후에 상속해서 사용함)
# engine, SessionLocal, Base는 main.py에서 서버를 실행시키는데 사용된다.

DB_URL = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}/{DB['database']}?charset=utf8"

engine = create_engine(
 f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}/{DB['database']}?charset=utf8"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# from sqlalchemy import create_engine
# 
# # ORM = 프레임워크에서 DB를 쿼리문을 사용 안하고 파이썬언어로 쿼리문을 작성해서 트랜젝션시켜주는 라이브러리?

# import pymysql 

# # 데이터베이스 주소 -> 연결 url

# # SQLALCHEMY_DATABASE_URL = "sql경로 "

# engine = create_engine('mysql+pymysql://root:aa77447769@127.0.0.1:3306/fastapi,encoding='utf-8')

# engine = create_engine(
# SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # engine = create_engine( encoding='utf-8')


# db = pymysql.connect(host="localhost",user ="root" , password= "aa77447769" ,charset="utf8")



# cursor = db.cursor()

# # create_engine :  인자값으로 DB URL을 추가하면 DB Host에 DB 연결을 생성한다. 이 함수가 DB연결의 출발점이다.
# # sessionmaker : 호출되었을 때, 세션을 생성해준다.
# # autocommit : api가 호출되어 DB의 내용이 변경된 경우, 자동으로 commit하며 변경할지에 대한 여부를 결정한다. False로 지정한 경우에는, insert, update, delete 등으로 내용이 변경됬을 때, 수동적으로 commit을 진행해주어야 한다.
# # autoflush : 호출되면서 commit되지 않은 부분의 내역을 삭제할지의 여부를 정하는 부분이다.
# # bind : 어떤 엔진을 통해 DB연결을 할지 결정하는 부분이다. MySQL, PostgreSQL 등 여러 SQL의 DB URL 중 어느 SQL제품으로 연결을 진행할지 선택하는 부분이다. 위의 부분에서는 engine변수가 하나밖에 선언되어있지 않지만, SQL을 여러 종류 쓰는 경우, 각 SQL에 맞게 해당 부분이 여러종류로 나뉠 수 있다.
# # delarative_base() : 상속된 DB모델 클래스들을 자동적으로 연결시켜주는 역할을 한다. 쉽게 말해, 테이블명이 일치하는 모델을 찾아 쿼리문을 실행시켜준다.
 
 
# # config로 연결시켜주어야함 

 #pymysql로 mysql 연결시키기, 
# import pymysql.cursors
# import pymysql


# # Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='aa77447769',
#                              db='fastapi_db',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# try:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)
# finally:
#     connection.close()
