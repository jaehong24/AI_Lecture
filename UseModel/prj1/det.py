# 디텍션 모델 
# 그림을 그려 주도록 만드는 것 

import cv2
import numpy as np

MARGIN = 10  # pixels
ROW_SIZE = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
TEXT_COLOR = (255, 0, 0)  # red


def visualize(
    image,
    detection_result
) -> np.ndarray:
  """Draws bounding boxes on the input image and return it.
  Args:
    image: The input RGB image.
    detection_result: The list of all "Detection" entities to be visualize.
  Returns:
    Image with bounding boxes.
  """
  for detection in detection_result.detections:
    # Draw bounding_box
    bbox = detection.bounding_box
    start_point = bbox.origin_x, bbox.origin_y
    end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
    cv2.rectangle(image, start_point, end_point, TEXT_COLOR, 3)

    # Draw label and score
    category = detection.categories[0]
    category_name = category.category_name
    probability = round(category.score, 2)
    result_text = category_name + ' (' + str(probability) + ')'
    text_location = (MARGIN + bbox.origin_x,
                     MARGIN + ROW_SIZE + bbox.origin_y)
    cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                FONT_SIZE, TEXT_COLOR, FONT_THICKNESS)

  return image



IMAGE_FILE = 'burger.jpg'

# import cv2

# img = cv2.imread(IMAGE_FILE)
# # cv2_imshow(img)
# cv2.imshow("test",img)
# cv2.waitKey(0) # 내가 누를 떄 까지 잡아준다.



# STEP 1: Import the necessary modules.
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# STEP 2: Create an ObjectDetector object.  -> 모델을 다룰.. 추론기 만들기 
base_options = python.BaseOptions(model_asset_path='models\\efficientdet_lite0.tflite')
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.5)   # score_threshold 디테치 확률이 0.5 이상일 경우만 이미지 표시
detector = vision.ObjectDetector.create_from_options(options)

# STEP 3: Load the input image. -> 추론할 이미지 가지고오기
image = mp.Image.create_from_file(IMAGE_FILE)

# STEP 4: Detect objects in the input image.
detection_result = detector.detect(image)  # 디테치 시키기
print(detection_result) # 디텍션 결과보기 객체 보기 

# STEP 5: Process the detection result. In this case, visualize it. -> step4 까지는 건드릴게 잘 없다 . 
image_copy = np.copy(image.numpy_view())  # 원본이미지를 카피한다
annotated_image = visualize(image_copy, detection_result) # 카피한 이미지에 그림을 그려준 이미지가 리턴된다
rgb_annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB) #bgb -> rgb 로 바꾸는 작업
# cv2_imshow(rgb_annotated_image)
cv2.imshow('test',rgb_annotated_image)
cv2.waitKey(0)