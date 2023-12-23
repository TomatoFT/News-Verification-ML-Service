import pandas as pd
from config import directory_path, output_file
from features_eng import (get_entities_of_news, get_news_categories,
                          get_sentiment_of_the_news,
                          get_summarization_of_the_news)
from get_article import GetArticle
from get_links import (CombineCSV, DKNNewsLink, LinkCrawler, LuatKhoaLink,
                       NgoisaoLink, ThanhNienNewsLinks, VnExpressNewsLink,
                       VTVNewsLinks)

link_crawler = LinkCrawler(sources=[
                                    VTVNewsLinks, 
                                    ThanhNienNewsLinks, 
                                    VnExpressNewsLink, 
                                    NgoisaoLink, 
                                    DKNNewsLink,
                                    LuatKhoaLink
                                    ])()

# Call the function to combine CSV files
CombineCSV(directory_path=directory_path, output_file=output_file)()

# Function to apply GetArticle to each row in the DataFrame
def apply_get_article(row):
    url = row['link']
    get_article_instance = GetArticle(url)
    get_article_instance()
    row['title'] = get_article_instance.get_title()
    row['content'] = get_article_instance.get_content()
    return row


def apply_features_engineering_by_DL(data):
    data['summarization'] = data['content'].apply(get_summarization_of_the_news)
    data['category'] = data['content'].apply(get_news_categories)
    data['entities'] = data['content'].apply(get_entities_of_news)
    data['sentiment'] = data['content'].apply(get_sentiment_of_the_news)
    

# Example usage:
csv_data = pd.read_csv(output_file)

# Apply the GetArticle class to each row
csv_data = csv_data.apply(apply_get_article, axis=1)

csv_data