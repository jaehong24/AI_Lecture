import torch
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration

# 모델과 토크나이저를 로드합니다.
tokenizer = PreTrainedTokenizerFast.from_pretrained("gogamza/kobart-summarization")
model = BartForConditionalGeneration.from_pretrained("gogamza/kobart-summarization")

# 요약하고자 하는 기사를 입력합니다.
news_text = "2018년 11월 당시 삼성전자-반올림 중재판정 이행합의 협약식에서 반올림 황상기 대표가 입고 있던 옷. 김창길 기자\n\n법원이 삼성전자 화성사업장 현장검증을 실시하기로 했다. 삼성전자 반도체 생산라인에서 일하다···"

# 토크나이저를 사용하여 뉴스기사 원문을 모델이 인식할 수 있는 토큰형태로 바꿔줍니다.
input_ids = tokenizer.encode(news_text, return_tensors="pt")

# 모델에 넣기 전 문장의 시작과 끝을 나타내는 토큰을 추가합니다.
input_ids = torch.cat([torch.tensor([[tokenizer.bos_token_id]]), input_ids, torch.tensor([[tokenizer.eos_token_id]])], dim=1)

# 모델을 사용하여 요약을 생성합니다.
summary_text_ids = model.generate(
    input_ids=input_ids,
    length_penalty=1.0,  # 길이에 대한 penalty값. 1보다 작은 경우 더 짧은 문장을 생성하도록 유도하며, 1보다 클 경우 길이가 더 긴 문장을 유도
    max_length=200,      # 요약문의 최대 길이 설정
    min_length=32,       # 요약문의 최소 길이 설정
    num_beams=4,         # 문장 생성시 다음 단어를 탐색하는 영역의 개수 
)

# 요약문을 출력합니다.
print(tokenizer.decode(summary_text_ids[0], skip_special_tokens=True))
