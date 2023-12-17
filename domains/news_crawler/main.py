import pandas as pd
import yaml
from get_article import GetArticle
from get_links import (CombineCSV, DKNNewsLink, LinkCrawler, LuatKhoaLink,
                       NgoisaoLink, ThanhNienNewsLinks, VnExpressNewsLink,
                       VTVNewsLinks)

from config import directory_path, output_file

link_crawler = LinkCrawler(sources=[
                                    VTVNewsLinks, 
                                    ThanhNienNewsLinks, 
                                    VnExpressNewsLink, 
                                    NgoisaoLink, 
                                    DKNNewsLink,
                                    LuatKhoaLink
                                    ])()


# Specify the directory containing CSV files and the output file name


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

# Example usage:
csv_data = pd.read_csv(output_file)

# Apply the GetArticle class to each row
csv_data = csv_data.apply(apply_get_article, axis=1)

csv_data