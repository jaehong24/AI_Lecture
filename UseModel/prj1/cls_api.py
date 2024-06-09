import PIL.Image
from fastapi import FastAPI, File, UploadFile

# STEP 1: Import the necessary modules. -> 필요한 모듈을 임포트
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.components import processors
from mediapipe.tasks.python import vision

import io
import PIL
import numpy as np

# fastApi 가 만들어지기 전에 사용 해야 한다.
# 이벤트를 받도록 루프가 계속 서버가 떠있기 때문에 
# 먼저 인스턴스 객체를 한번 만들어 놓으면, 만들어진 객체를 사용 할 수 있다.
# 이로서 모델을 한번만 다운 받게됨, 만약 app=fastAPI() 뒤에 넣으면 모델을 계속 다운함
# STEP 2: Create an ImageClassifier object. -> 추론기를 만드는 것,  모든 테스크에는 모델이 필요하다. base 옵션에는 model경로 위치를 설정 해야한다.
base_options = python.BaseOptions(model_asset_path='models\\efficientnet_lite0.tflite')

options = vision.ImageClassifierOptions(
base_options=base_options, max_results=3)  # max_result = 모델이 벹어내는 아웃풋을 몇 개를 설정
classifier = vision.ImageClassifier.create_from_options(options)  # 최종적으로 classifiter 가 만들어진다




app = FastAPI()

# <파일 전송>
# 1. files로 들어 온 것은 os에 미리 파일이 왔다가 서버로 전송됨 

# 2. uploadfile 는 메타정보만 os에 보낸다. http header에 있는 정보를 보낸다
# 그래서 read()가 필요하다.
# curl -X 'POST' \
#   'http://127.0.0.1:8000/uploadfile/' 
#   -H 'accept: application/json' \
#   -H 'Content-Type: multipart/form-data' 
#   -F 'file=@123.jpg;type=image/jpeg'
# 업로드 파일로 받게 되면 메타 정보가 있기 때문에 read를 통해 await를 통해 
# 업로드 파일을 받을 수 있다.

# 2 번을 쓰는게 좋다 .




# @app.post("/files/")
# async def create_file(file: bytes = File()):
#     return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):  

    # uploadfile를 사용하면 file.content_type   통해 확장자가 다를 때 거를 수 있다 . 
 
    byte_file  =  await file.read() # 파일을 한번 읽어줘야 한다 
    
    # STEP 3: Load the input image. -> 데이터를 가져오기 
    # 추론 할 수 있는 이미지로 만들어준다. 로컬 파일에 있는 것을 불러와서 사용한다. 

    # 바이너리가 http로 오면 문자열로 온다. 
    # 그래서 바이너리로 바꿔주는 모듈이 있다.
    imgage_bin =  io.BytesIO(byte_file)  # char array- > binary array
    
    pil_img = PIL.Image.open(imgage_bin) # binary array -> PIL(파이썬에서 다룰 수 있는 이미지로변환) 비트맵으로 디코딩 한다
   
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.asarray(pil_img))
   

    
    # STEP 4: Classify the input image.   ->  추론시키기, 분류시키기 
    classification_result = classifier.classify(image)
    print(classification_result)

    # STEP 5: Process the classification result. In this case, visualize it.  -> 결과보여주기, step3, step5 만 바뀐다 api를 만들떄 
    # images.append(image)
    
    count =3
    resulut = [] 

    for i in range(count) :
        # 왜 0 번을 쓰나요 ? 사진이 한장이니 !!!
        top_category = classification_result.classifications[0].categories[i]
        resulut.append(f"{top_category.category_name} ({top_category.score:.2f})")
    
    print(resulut)
    return {"result" : resulut}



    




# uvicorn main:app --reload 
# main은 파이썬 이름, 5번쨰 줄에있는 인스턴스
# fast api는 swager가 있따.