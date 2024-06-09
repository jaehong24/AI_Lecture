from fastapi import FastAPI, Form
# STEP 1. import modules
from transformers import pipeline

# STEP 2. create inference instatnce
            # 허깅페이스는 pipeline 하나로 다 된다.
            # pipeline("태스크", 모델)
            # 모델에서 앞에 사용자명을 안적으면 내 허브에서 찾기 때문에 huggingface에 로그인하라고 오류가 뜬다
classifier = pipeline("sentiment-analysis", model="snunlp/KR-FinBert-SC")


app = FastAPI()


@app.post("/text/")
async def text(text: str = Form()):
    # STEP 3. prepare input data
    # text = "This was a masterpiece. Not completely faithful to the books, but enthralling from beginning to end. Might be my favorite of the three."




    # STEP 4. infrence
    result = classifier(text)

    # STEP 5. visualize
    # print(result)

    return {"text": result}