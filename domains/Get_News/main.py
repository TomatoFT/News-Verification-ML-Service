# from load_to_hdfs import append_data_to_hdfs_file, read_hdfs_data_file, create_the_hdfs_file
import json

from fastapi import FastAPI
from kafka_server import get_data_from_consumer, push_data_to_producer
from load_to_mysql_db import load_the_data_to_db, observe_the_data_from_table
from newspaper import Article
import aiohttp
import asyncio

import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            data = response.json()
            return data['ip']
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    
    return None

hostname = get_public_ip()
SUMMARIZATION_PORT = 3001
CATEGORIES_PORT = 3002
RELEVANCY_PORT = 3003


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                return None

app = FastAPI()


async def make_Summarization_request(raw_texts):
    url = f"http://{hostname}:{SUMMARIZATION_PORT}/api/get_news_summarization_content"
    payload = {"news_content": raw_texts}
    print(payload)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, params=payload) as response:
            response_text = await response.json()
            return response_text

async def make_get_categories_request(raw_texts):
    url = f"http://{hostname}:{CATEGORIES_PORT}/api/get_news_categories"
    payload = {"news_content": raw_texts}
    print(payload)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, params=payload) as response:
            response_text = await response.json()
            return response_text

async def make_get_relevancy_score_request(text_1, text_2):
    url = f"http://{hostname}:{CATEGORIES_PORT}/api/get_the_revelancy_score"
    payload = {"first_news_content": text_1, 'seconnd_news_content':text_2}
    print(payload)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, params=payload) as response:
            response_text = await response.json()
            return response_text['score']


@app.post("/api/get_news_content_from_user")
def get_news_content_from_url(news_url: str, is_verified: bool):
    article = Article(news_url, language="vi")
    article.download()
    article.parse()
    results = {
        "Source": news_url.split("/")[2],
        "Title": article.title,
        "Content": article.text,
        "Is_verified": str(is_verified),
    }
    # Add the summarize_content
    loop = asyncio.new_event_loop()
    
    results['Summarization'] = loop.run_until_complete(make_Summarization_request(results["Content"]))
    results['Categories'] = loop.run_until_complete(make_get_categories_request(results["Content"]))

    serialized_value = json.dumps(results).encode("utf-8")
    push_data_to_producer(serialized_value)
    
    msg = get_data_from_consumer()
    decode_value = ""
    if msg == None:
        print("ERROR")
    else:
        decode_value = msg.value().decode("utf-8")
        decoded_dict = json.loads(decode_value)
        load_the_data_to_db(results)
        print("INSERT TO KAFKA SUCCESSFULLY")
    observe_the_data_from_table()


    return results
