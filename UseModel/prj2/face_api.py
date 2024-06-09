from fastapi import FastAPI, File, UploadFile
import numpy as np
import insightface
from insightface.app import FaceAnalysis
import io
import PIL.Image

# 모델을 한 번만 로드하기 위해 FastAPI 인스턴스 생성 전에 모델 로드
faceModel = FaceAnalysis(providers=['CPUExecutionProvider'])
faceModel.prepare(ctx_id=0, det_size=(640, 640))

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile, file2: UploadFile):
    # 업로드된 파일을 읽어 바이트 데이터로 변환
    byte_file = await file.read()
    byte_file2 = await file2.read()

    # 바이트 데이터를 바이너리 스트림으로 변환
    imgage_bin = io.BytesIO(byte_file)
    imgage_bin2 = io.BytesIO(byte_file2)

    # 바이너리 스트림을 PIL 이미지로 변환
    pil_img = PIL.Image.open(imgage_bin)
    pil_img2 = PIL.Image.open(imgage_bin2)

    # PIL 이미지를 numpy 배열로 변환
    np_image = np.asarray(pil_img)
    np_image2 = np.asarray(pil_img2)

    # Insightface를 사용하여 얼굴을 감지
    faces = faceModel.get(np_image)
    faces2 = faceModel.get(np_image2)

    # 얼굴이 감지되지 않았을 경우 에러 메시지 반환
    if not faces or not faces2:
        return {"result": "얼굴을 감지하지 못했습니다."}

    # 감지된 얼굴에서 임베딩 추출
    feats = []
    feats.append(faces[0].normed_embedding)
    feats.append(faces2[0].normed_embedding)
    feats = np.array(feats, dtype=np.float32)

    # 임베딩 벡터 간의 유사도를 계산
    sims = np.dot(feats[0], feats[1].T)

    # 유사도 결과에 따라 메시지 설정
    result = '비슷하지 않습니다.'
    if sims > 0.5:
        result = '비슷합니다.'

    return {"result": result}

# uvicorn main:app --reload
# uvicorn을 사용하여 애플리케이션을 실행
# 'main'은 이 파일의 이름, 'app'은 FastAPI 인스턴스
