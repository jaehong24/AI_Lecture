# 의미론적 신텍스가 나온다
# 짧은 단어 
# Hybird Search도 있다. 
# 글자의 유사도가 아닌 의미론적인 유사도를본다.
# 모델 중에 multilingual가 붙어야 다국어를 지원한다. 


# STEP 1
from sentence_transformers import SentenceTransformer

# STEP 2 추론기만들기
# 허깅페이스에서와 모델 가지고오는 거 같은데, 자신들의 것이니 배포자 이름 안적어도 됨
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')




# STEP 3 데이터
sentences1 = "I LIKE you "
sentences2 = "I love you"


# STEP 4  인코딩시키기
embedding1 = model.encode(sentences1)
embedding2 = model.encode(sentences2)

print(embedding1.shape)
print(embedding2.shape)

# STEP 5 출력
similarities = model.similarity(embedding1, embedding2)

print(similarities)
