from transformers import BertTokenizer, BertForSequenceClassification
import torch
from scipy.special import softmax
import numpy as np

# KoBERT 모델과 토크나이저 로드
model_name = "monologg/kobert"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=3) # 3개의 감정 클래스 (긍정, 부정, 중립)로 설정

# 텍스트 전처리
def preprocess(text):
    return text

# 분석할 한국어 텍스트
text_kor = "이 음식이 너무 맛있다/"
text = preprocess(text_kor)

# 감정 분석을 위해 텍스트 인코딩
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)

# 감정 점수 계산
scores = output.logits[0].detach().numpy()
scores = softmax(scores)

# 레이블과 점수 출력
labels = ['Negative', 'Neutral', 'Positive'] # 클래스 레이블
ranking = np.argsort(scores)[::-1]
for i in range(scores.shape[0]):
    l = labels[ranking[i]]
    s = scores[ranking[i]]
    print(f"{i+1}) {l} {np.round(float(s), 4)}")
