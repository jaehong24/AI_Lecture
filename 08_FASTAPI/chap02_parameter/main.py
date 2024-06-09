from fastapi import FastAPI

# 매게변수 알아보기 
app = FastAPI()


# 경로 매게변수
# URL 경로에 들어가는 매게변수
# @app.get("/users/{user_id}")
# def get_user(user_id) : 
#     return {"user_id " : user_id}


# 타입을 정의하려면 ?  
@app.get("/users/{user_id}")
def get_user(user_id : int) : 
    return {"user_id " : user_id}

# 순서가 중요하다 
@app.get("/users/aaa")
def get_current_user():
    return {"user_id" : 123}

# 쿼리 매개변수

# 호스트 주소/path? 뒤에 오는 변수들을 쿼리 매개변수 라고 한다
# 각 매개변수는 & 기호로 구분되괴 key=value 쌍으로 정의된다.
# http://127.0.0.1:8000/users?limit=2&name=asdf
@app.get("/users")
def get_users(limit : int, name : str):
    return {"limit" : limit, "name" : name}


#http://127.0.0.1:8000/docs -> 스웨거

@app.get('/users')
def get_users(limit:int = 100 ): # 기본값 지정
    return {"limit":limit}


# uvicorn main:app --port 8080 --reload  -> 포트 번호 지정 





