import PIL.Image
from fastapi import FastAPI, File, UploadFile

# STEP 1: Import the necessary modules. -> 필요한 모듈을 임포트
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.components import processors
from mediapipe.tasks.python import vision

# fastApi 가 만들어지기 전에 사용 해야 한다.
# 이벤트를 받도록 루프가 계속 서버가 떠있기 때문에 
# 먼저 인스턴스 객체를 한번 만들어 놓으면, 만들어진 객체를 사용 할 수 있다.
# 이로서 모델을 한번만 다운 받게됨, 만약 app=fastAPI() 뒤에 넣으면 모델을 계속 다운함
# STEP 2: Create an ImageClassifier object. -> 추론기를 만드는 것,  모든 테스크에는 모델이 필요하다. base 옵션에는 model경로 위치를 설정 해야한다.
base_options = python.BaseOptions(model_asset_path='models\efficientnet_lite0.tflite')

options = vision.ImageClassifierOptions(
    base_options=base_options, max_results=1)  # max_result = 모델이 벹어내는 아웃풋을 몇 개를 설정
classifier = vision.ImageClassifier.create_from_options(options)  # 최종적으로 classifiter 가 만들어진다




app = FastAPI()

import io
import PIL
import numpy as np

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    byte_file = await file.read()

    # STEP 3: Load the input image.
    #image = mp.Image.create_from_file(IMAGE_FILENAMES[1])

    # convert char array to binary array
    image_bin = io.BytesIO(byte_file)
    
    # create PIL Image from binary array
    pil_img = PIL.Image.open(image_bin)

    # Convert MP Image from PIL IMAGE
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.asarray(pil_img))

    # STEP 4: Classify the input image.
    classification_result = classifier.classify(image)


    # STEP 5: Process the classification result. In this case, visualize it.
    top_category = classification_result.classifications[0].categories[0]
    result = f"{top_category.category_name} - ({top_category.score:.2f})"

    print(result)

    return {"file_size": len(byte_file)}


# uvicorn main:app --reload 
# main은 파이썬 이름, 5번쨰 줄에있는 인스턴스
# fast api는 swager가 있따.