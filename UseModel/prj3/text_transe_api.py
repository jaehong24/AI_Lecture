# STEP 1. 모듈 임포트
from fastapi import FastAPI, Form
from transformers import MarianMTModel, MarianTokenizer


# STEP 2. 모델 다운
model_name = 'Helsinki-NLP/opus-mt-ko-en'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)



app = FastAPI()

@app.post("/text/")
async def text(text: str = Form()):
    # STEP 3. prepare input data
    # text = "This was a masterpiece. Not completely faithful to the books, but enthralling from beginning to end. Might be my favorite of the three."
    encoded_text = tokenizer.prepare_seq2seq_batch([text], return_tensors='pt')
    translated = model.generate(**encoded_text)
    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)


    return translated_text[0]

