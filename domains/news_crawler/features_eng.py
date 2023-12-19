import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from underthesea import classify, ner, sentiment

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def get_news_categories(news_content):
    return classify(news_content)

def get_entities_of_news(news_content):
    results = ner(news_content, deep=True)
    return results

def get_sentiment_of_the_news(news_content):
    return sentiment(news_content)

def preload_summarization_model():
    tokenizer = AutoTokenizer.from_pretrained("VietAI/vit5-large-vietnews-summarization")
    model = AutoModelForSeq2SeqLM.from_pretrained("VietAI/vit5-large-vietnews-summarization")
    model = model.to(device)
    return tokenizer, model

tokenizer, model = preload_summarization_model()

def get_summarization_of_the_news(sentence):
    sentence = str(sentence)
    results = []
    text = "vietnews: " + sentence + " </s>"
    encoding = tokenizer(text, return_tensors="pt")
    input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)

    outputs = model.generate(
        input_ids=input_ids,
        attention_mask=attention_masks,
        max_length=1024,
        early_stopping=True,
    )

    for output in outputs:
        line = tokenizer.decode(
            output, skip_special_tokens=True, clean_up_tokenization_spaces=True
        )
        results.append(line)
    return " ".join(results)
