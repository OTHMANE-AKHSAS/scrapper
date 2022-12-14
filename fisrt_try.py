import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

search_query = 'winter jacket'.replace(' ', '+')
base_url = 'https://www.amazon.com/s?k={0}'.format(search_query)

items = []
for i in range(1, 5):
    print('Processing {0}...'.format(base_url + '&page={0}'.format(i)))
    response = requests.get(base_url + '&page={0}'.format(i), headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    results = soup.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})

    for result in results :
        product_name = result.h2.text
        print(product_name)
        try :
            rating = result.find('i', {'class': 'a-icon'}).text
            print(rating)
            rating_count = result.find('span', {'class': 'a-size-base'}).text
            print(rating_count)
        except AttributeError :
            print("errr")
            continue
        break