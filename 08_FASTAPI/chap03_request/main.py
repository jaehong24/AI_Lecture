# 요청 응답

# POST, PUT, PATCH 등의 메소드를 사용하는 경우 
# HTTP 본문(body) 사용

#단순 텍스트나 json 이용한다.

# pydantic 으로 요청 본문 받기
# 데이터 유효성 검사 및 설정 관리를 위한 라이브러리 


from typing import Optional 
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# BaseModel 상속받아야 POST 요청으로 받아온 데이터를 사용가능하다.
class UserInfo(BaseModel) : 
    name : str
    password :str
    url : Optional[HttpUrl] = None # Optional : 선택사항을 설정 할 수 있다. required, Htturl -> url 형식이어야 하고, 기본값은 None


 # UserInfo 클래스 (BaseModel 을 상속 받음 )
 # BaseModel 을 상속 받아야 request body 부분을 받을 클래스로 이용할 수 있다.
@app.post('/users')  
def createUser(user: UserInfo) :  
    return user

# /users post 요청에 담겨온 body 부분을 userInfo 자료형에 담아 user라는 객체를 생성한다
