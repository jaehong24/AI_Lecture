from fastapi import FastAPI

# pip install fastapi  - 파이썬을 통해 웹 개발 할 수 있는 라이브러리
# pip install uvicorn  - 서버 띄우는 것 

# 해당 폴더에 cd로 들어가서 실행해야함 
# uvicorn main:app --reload



# python 으로 작성된 API를 만들기 위한 웹 프레임워크

# 장점
# 1. 고성능 = 아주 빠른 성능을 제공하며, 기존의 flask 같은 웹 
# 프레임워크보다 2배 가량 빠르다.
# 2. 쉬운 사용 = 작성하기 쉬운 코드 방식을 가지고 있다.
# 3. 자동 문서화 = swagger 문서 지원
# 4. 비동기 지원 = 비동기 기능을 지원하여 비동기 작업을 쉽게 처리할 수 있다.

# app 객체를 통해 FastAPI 설정을 할 수 있다.
app = FastAPI()



# get 요청
@app.get("/")
def read_root():
    return {"hello" : "world"}

# __name__ 파이썬 파일이 실행 될 떄 마다 생성 
# __main__일 때만 서버가 실행 되겠다, 다른 파일에서 실행하면 실행되지 않게 하겠다.
# __name__ 변수 python 에서는 각 파일이 실행 될마다  특별한 변수인 __name__을 갖는다.
# 스크립트가 실행될때, __name__변수는 "__main__" 으로 설정된다.
# 스크립트가 다른 모듈에 임포트 될 떄 __name__ 변수는 해당 모듈의 이름으로 바뀐다.
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True) # 



# < uvicorn main:app --reload >
# main = main.py 파일을 의미
# app = main.py 에서 FastAPI() 객체를 식별하는 app 객체를 의미
# --reload = 파일에 변화가 생기면 재시작 하겠다는 옵션 

