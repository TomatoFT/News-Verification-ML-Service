import time

import newspaper
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

IS_NEWS_TOKEN = 6


import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

IS_NEWS_TOKEN = 2  # Assuming this is a constant for the token length

class NewsInformation:
    def __init__(self, link, category, source) -> None:
        self.link = link
        self.category = category
        self.source = source

class BaseNewsLinks:
    source = None
    black_list = []
    format_category_urls = []
    unformat_category_urls = []
    articles_link = []
    def __init__(self, path='geckodriver') -> None:
        self.paper = newspaper.build(self.source)
        self.driver = webdriver.Firefox(executable_path=path)

    @staticmethod
    def is_news_article(link):
        try:
            part = link.split('/')
            token = part[4].split('-')
            return len(token) > IS_NEWS_TOKEN
        except:
            return False
        
    def scroll_down(self):
        for _ in range(4):  # Adjust the range as needed
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Add a small delay to allow content to load (adjust as needed)

    
    def get_articles_link(self):
        articles_link = []
        try:
            for category in self.format_category_urls:
                self.driver.get(self.source + category)
                print(category) 
                self.scroll_down()
                # Wait for the page to load (adjust the timeout as needed)
                WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//a")))

                # Find all anchor tags (links) using Selenium
                links = self.driver.find_elements(By.XPATH, "//a[@href]")

                try:
                    # Extract and print the href attribute of each link
                    for link in links:
                        href = str(link.get_attribute('href'))
                        print(href)
                        if self.is_news_article(href):
                            articles_link.append(NewsInformation(link=href, 
                                                                 category=category, 
                                                                 source=self.source))
                        else:
                            continue
                except Exception as e:
                    print(f"Error processing links: {e}")
                    continue

        finally:
            # Close the driver in the finally block to ensure cleanup
            self.driver.quit()
            # Save the unique article link
            self.articles_link = list(set(articles_link))
            return self

    def to_csv(self, file_name='news_links.csv'):  # Added default file_name
        # Assuming you want to write the links to a CSV file
        df = pd.DataFrame({
            'link': [article.link for article in self.articles_link],
            'category': [article.category for article in self.articles_link],
            'source': [article.source for article in self.articles_link]
        })

        df.to_csv(file_name, index=False)  # Save to CSV without index


class VTVNewsLinks(BaseNewsLinks):
    black_list = ['zoom', 'megazine']
    source = 'https://vtv.vn/' 
    format_category_urls = [
                    'chinh-tri.htm',
                    'xa-hoi.htm',
                    'phap-luat.htm',
                    'the-gioi.htm',
                    'kinh-te.htm',
                    'the-thao.htm',
                    'van-hoa-giai-tri.htm',
                    'doi-song.htm',
                    'cong-nghe.htm',
                    'giao-duc.htm']
    unformat_category_urls = ['https://suckhoe.vtv.vn/']

# Example usage
vtv = VTVNewsLinks()
vtv.get_articles_link().to_csv('VTV_link.csv')
