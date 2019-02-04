import json
from bs4 import BeautifulSoup
import requests


def site_map(url_base: str) -> dict:
    """Function which is generated site map"""

    # importing data from json file
    with open('urls.json') as f:
        data = json.load(f)

    # Creating a set of url adresses
    urls = {i['url'] for i in data}

    # main dictionary -> contains all map
    d_main = {}

    for link in sorted(urls):

        # function will be execute only if site contains to main site
        if url_base in link:
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'lxml')
            tags = soup.find_all('a')
            title = str(soup.find('title'))[7:-8]

            # Dict contains title and all links of page
            help_dict = {'title': title, 'links': {str(tag.get('href')) if 'http' in str(tag)
                                                   else url_base + str(tag.get('href'))
                                                   for tag in tags}}
            d_main[link] = help_dict
    return d_main

print(site_map('http://0.0.0.0:8000'))