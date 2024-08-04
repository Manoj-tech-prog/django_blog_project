import requests
import json
import os
import schedule
import time


INDEX_FILE = 'index.txt'
NEWS_FILE = 'news_data.json'

def fetch_news():
    try:
        api_key = '374ea7196abc4f4ab7ddd6d55dbe6e29'
        api_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

        response = requests.get(api_URL)
        response.raise_for_status()
        news_data = response.json()

        if 'articles' in news_data:
            with open(NEWS_FILE, 'w') as file:
                json.dump(news_data, file, indent=4)
            print("News data fetched & saved")
        else:
            print("NO 'articles' key found in the response" )
    except requests.RequestException as e:
        print(f"Request error as {e}")
    except json.JSONDecodeError as e:
        print(f"JSON decode error as {e}")
    except Exception as e:
        print(f"error as {e}")


def update_index():
    if not os.path.exists(INDEX_FILE):
        with open(INDEX_FILE,'w') as file:
            file.write('0')
    with open(INDEX_FILE,'r') as file:
        current_index = int(file.read().strip())
    new_index = (current_index+5)%20

    with open(INDEX_FILE,'w') as file:
        file.write(str(new_index))

def get_current_index():
    if not os.path.exists(NEWS_FILE):
        return []
    
    with open(NEWS_FILE, 'r') as file:
        news_data = json.load(file) 
    
    if 'articles' not in news_data:
        return []
    
    if not os.path.exists(INDEX_FILE):
        return []
    
    with open(INDEX_FILE, 'r') as file:
        current_index = int(file.read().strip())
    return news_data['articles'][current_index:current_index+5]


schedule.every(20).seconds.do(fetch_news)
schedule.every(20).seconds.do(update_index)

while True:
    schedule.run_pending()
    time.sleep(1)