from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


def preload_summarization_model():
    tokenizer = AutoTokenizer.from_pretrained(
        "VietAI/vit5-large-vietnews-summarization"
    )
    model = AutoModelForSeq2SeqLM.from_pretrained(
        "VietAI/vit5-large-vietnews-summarization"
    )
    return tokenizer, model


tokenizer, model = preload_summarization_model()


def get_summarization_of_the_news(sentence):
    results = []
    text = "vietnews: " + sentence + " </s>"
    encoding = tokenizer(text, return_tensors="pt")
    input_ids, attention_masks = encoding["input_ids"], encoding["attention_mask"]

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
