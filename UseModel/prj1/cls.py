

# vs 코드는 커멘드와 일치화가 되어 있지 않아 설정을 맞춰줘야한다. 
import cv2
# from google.colab.patches import cv2_imshow
import math

# util에서 받은 파일 이름 가지고 오기
DESIRED_HEIGHT = 480
DESIRED_WIDTH = 480
# def resize_and_show(image):
#   h, w = image.shape[:2]

#   if h < w:
#     img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
#   else:
#     img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))

#   # cv2_imshow(img) 코렙에서만 사용 하니 대체해야한다.
#   # 아무 창을 만들고 그기에 사진을 보여주게함 
#   cv2.imshow("Image", img)  
#   cv2.waitKey(0) 
# # Preview the images.
# images = {name: cv2.imread(name) for name in IMAGE_FILENAMES}
# for name, image in images.items():
#   print(name)
#   resize_and_show(image)



IMAGE_FILENAMES = ['burger.jpg', 'cat.jpg','airplain.jpg']

# STEP 1: Import the necessary modules. -> 필요한 모듈을 임포트
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.components import processors
from mediapipe.tasks.python import vision


# STEP 2: Create an ImageClassifier object. -> 추론기를 만드는 것,  모든 테스크에는 모델이 필요하다. base 옵션에는 model경로 위치를 설정 해야한다.
base_options = python.BaseOptions(model_asset_path='models\efficientnet_lite0.tflite')

options = vision.ImageClassifierOptions(
    base_options=base_options, max_results=1)  # max_result = 모델이 벹어내는 아웃풋을 몇 개를 설정
classifier = vision.ImageClassifier.create_from_options(options)  # 최종적으로 classifiter 가 만들어진다



# images = []
# predictions = []
# for image_name in IMAGE_FILENAMES: -> 지금은 처음이니 배열로 하지말고 특정 값으로만 진행
# STEP 3: Load the input image. -> 데이터를 가져오기 
image = mp.Image.create_from_file(IMAGE_FILENAMES[2]) 



# STEP 4: Classify the input image.   ->  추론시키기, 분류시키기 
classification_result = classifier.classify(image)



# STEP 5: Process the classification result. In this case, visualize it.  -> 결과보여주기, step3, step5 만 바뀐다 api를 만들떄 
# images.append(image)
top_category = classification_result.classifications[0].categories[0]
resulut = (f"{top_category.category_name} ({top_category.score:.2f})")


print(resulut)
# display_batch_of_images(images, predictions)