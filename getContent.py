import requests
from bs4 import BeautifulSoup as bs

def getRawContent(url):
    # Get Content
    response = requests.get(url=url)
    soup = bs(response.text, 'html.parser')

    #For test
    #html_content = ""
    #with open("Can Dogs Eat Shrimp_.html", 'r') as f:
    #    html_content = f.read()
    #soup = bs(html_content, 'html.parser')

    # Remove unused tags
    new_soup = bs('', 'html.parser')
    for tag in soup.find_all(['h1', 'h2', 'h3', 'p']):
        new_soup.append(tag)
    return new_soup


getRawContent("http://127.0.0.1:3000/Can Dogs Eat Shrimp_.html")