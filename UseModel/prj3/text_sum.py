# STEP1. 필요 모듈 가지고오기
from transformers import pipeline

# STEP2. 추론기 만들기 (테스크 이름, 모델 이름)
# 자연어도 내부적으로는 전처리 후처리가 있다. 
summarizer = pipeline("summarization", model="stevhliu/my_awesome_billsum_model")

# STEP 3. 데이터 만들기
text = "summarize: The Inflation Reduction Act lowers prescription drug costs, health care costs, and energy costs. It's the most aggressive action on tackling the climate crisis in American history, which will lift up American workers and create good-paying, union jobs across the country. It'll lower the deficit and ask the ultra-wealthy and corporations to pay their fair share. And no one making under $400,000 per year will pay a penny more in taxes."

# STEP 4. 추론화
result = summarizer(text)

# STEP 5. 출력
print(result)