from transformers import MarianMTModel, MarianTokenizer
import sentencepiece as spm



model_name = 'Helsinki-NLP/opus-mt-ko-en'

tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

text = "안녕하세요"
encoded_text = tokenizer.prepare_seq2seq_batch([text], return_tensors='pt')

# encoded_text 딕셔너리 내용 예시:
# {'input_ids': tensor([[...]]), 'attention_mask': tensor([[...]])}

# **encoded_text를 사용하여 키워드 인수로 전달
translated = model.generate(**encoded_text)

# translated는 모델이 생성한 번역된 텍스트의 토큰 ID를 포함한 텐서입니다.
translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
print(translated_text)

print(translated_text[0])  # 번역된 텍스트 출력
