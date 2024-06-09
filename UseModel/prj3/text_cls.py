# STEP 1. import modules
from transformers import pipeline

# STEP 2. create inference instatnce
            # 허깅페이스는 pipeline 하나로 다 된다.
            # pipeline("태스크", 모델)
            # 모델에서 앞에 사용자명을 안적으면 내 허브에서 찾기 때문에 huggingface에 로그인하라고 오류가 뜬다
classifier = pipeline("sentiment-analysis", model="stevhliu/my_awesome_model")

# STEP 3. prepare input data
text = "This was a masterpiece. Not completely faithful to the books, but enthralling from beginning to end. Might be my favorite of the three."




# STEP 4. infrence
result = classifier(text)

# STEP 5. visualize
print(result)



############ 위에서 파이프라인으로 쉽게 썼지만 내부적으로는 아래처럼 전처리-추론-후처리로 나누어져 있어서 아래와 같이 쓰는 것이 원래 내부적인 것이다. 하지만 파이프라인만 쓸 것이기 때문에 이해 못해도 된다.





# # STEP 1. import modules
# from transformers import pipeline
# from transformers import AutoTokenizer, AutoModelForSequenceClassification  # sequence 데이터는 문장이나 음성 등의 데이터를말한다.(순서가 있기 때문)

# # STEP 2. 
# tokenizer = AutoTokenizer.from_pretrained("stevhliu/my_awesome_model")
# model = AutoModelForSequenceClassification.from_pretrained("stevhliu/my_awesome_model")


# classifier = pipeline("sentiment-analysis", model="stevhliu/my_awesome_model")

# # STEP 3. prepare input data
# text = "This was a masterpiece. Not completely faithful to the books, but enthralling from beginning to end. Might be my favorite of the three."

# # STEP 4. infrence
# inputs = tokenizer(text, return_tensors="pt")
# with torch.no_grad():
#     logits = model(**inputs).logits
# # result = classifier(text)

# # 추론은 내부적으로 아래와 같은 흐름으로 진행된다.
# # 딥러닝은 무조건 이런다. 전처리 -> 추론 -> 후처리
# # 4-1 preprocessing(data(사람이 읽을 수 있음) -> tensor(blob))
# # 4-2 inference(tensor(blob) -> logit)
# # 4-3 postprocessing(logit -> data(사람이 읽을 수 있음))

# # STEP 5. visualize
# print(result)