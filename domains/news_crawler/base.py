import time
import pandas as pd
import newspaper
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

IS_NEWS_TOKEN = 6


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

class BaseNewsLinks:
    source = None
    black_list = []
    format_category_urls = []
    unformat_category_urls = []

    def __init__(self) -> None:
        self.paper = newspaper.build(self.source)

    @staticmethod
    def is_news_article(link):
        try:
            part = link.split('/')
            token = part[4].split('-')
            return len(token) > IS_NEWS_TOKEN
        except:
            return False

    @property
    def articles_link(self):
        articles_link = []

        # Initialize the driver outside the try block
        driver = webdriver.Firefox(executable_path='geckodriver')

        try:
            for category in self.format_category_urls:
                driver.get(self.source + category)
                print(category)
                # Scroll down to the end of the page to load all articles
                for _ in range(4):  # Adjust the range as needed
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)  # Add a small delay to allow content to load (adjust as needed)

                # Wait for the page to load (adjust the timeout as needed)
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//a")))

                # Find all anchor tags (links) using Selenium
                links = driver.find_elements(By.XPATH, "//a[@href]")

                try:
                    # Extract and print the href attribute of each link
                    for link in links:
                        href = str(link.get_attribute('href'))
                        print(href)
                        if self.is_news_article(href):
                            articles_link.append(self.source + href)
                        else:
                            # print('Error link: ', href)
                            continue
                except Exception as e:
                    print(f"Error processing links: {e}")
                    continue

        finally:
            # Close the driver in the finally block to ensure cleanup
            driver.quit()

        # Returning a list with unique values
        return list(set(articles_link))


class VTVNewsLinks(BaseNewsLinks):
    black_list = ['zoom', 'megazine']
    source = 'https://vtv.vn/' 
    format_category_urls = ['chinh-tri.htm',
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


vtv = VTVNewsLinks()
print(len(vtv.articles_link))
