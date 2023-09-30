from underthesea import classify, ner, sentiment


def get_news_categories(news_content):
    return classify(news_content)


def get_entities_of_news(news_content):
    results = ner(news_content, deep=True)
    return results


def get_sentiment_of_the_news(news_content):
    return sentiment(news_content)
