# 인사이트페이스는 추론기는 onnxruntime 추론기를 사용한다.
# 인사이트페이스 모델은 

# STEP 1 임포트하기
import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

# STEP 2 추론기 만들기
#providers=['CUDAExecutionProvider', 'CPUExecutionProvider'] 오닉스 런타임에 제공하는 것 
#cpu니 CUDA 지우기
app = FaceAnalysis(providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

# STEP 3 데이터 가져오기
# img = ins_get_image('t1') #셈플이미지
# 이미지 읽어오기 , 두번쨰 매게변수는 컬러 흑백 구분 
img = cv2.imread('ca.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('k4.jpg',cv2.IMREAD_COLOR)

# STEP 4 추론
faces = app.get(img)
faces2 = app.get(img2)

print(faces)
print( '얼굴수 = ' , len(faces))
print( '임베딩 = ' , faces[0].embedding)

# STEP 5 보여주기
# rimg = app.draw_on(img, faces)
# cv2.imwrite("./k1_output.jpg", rimg)

# then print all-to-all face similarity
feats = []
feats.append(faces[0].normed_embedding) #norm 임베디딩 : 외우기 그냥 이거 쓰면됨 
feats.append(faces2[0].normed_embedding) #norm 임베디딩 : 외우기 그냥 이거 쓰면됨 

feats = np.array(feats, dtype=np.float32)   #넘파이에 닷 연산이 있다. 512길이의 배열 을 세워준다
sims = np.dot(feats[0], feats[1].T)
print('일치도 = ' , sims)
# 0.6이 확률을 말하는 것이 아니라 유사도를 나타냄 
# -1 ~ 1 사이의 값을 가지니 0.6 정도면 높은 수치다 
# 0.6을 넘으면 같다고 본다고 설정

# <밑 오류 해결>
# The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
#     https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations. Did you mean: 'inf'?

# conda create -n proj22 python=3.10

# conda activate proj22

# pip install insightface

# pip install onnxruntime

# pip uninstall numpy

# pip install numpy==1.23.0
