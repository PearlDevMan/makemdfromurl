import requests
import re
from bs4 import BeautifulSoup as bs

def getRawContent(url):
    # Get Content
    response = requests.get(url=url)
    soup = bs(response.text, 'html.parser')
    related = ""
    for tag in soup.find_all('a'):
        if(tag.string != None):
            if("Related article:" in tag.string):
                related = tag.string
    tempsoup = str(soup)
    if "Related article:" in tempsoup:
        del_index = tempsoup.index("Related article:")
        tempsoup = tempsoup[:del_index-1]

    new_soup = bs('', 'html.parser')

    soup = bs(tempsoup, 'html.parser')
    for tag in soup.find_all(['h1', 'h2', 'h3', 'p']):
        for min_tag in tag.find_all('a'):
            min_tag.replace_with(min_tag.string)
        
        new_soup.append(tag)
    for tag in new_soup.find_all('h3')[:22]:
        tag.extract()
    filename = new_soup.find('h1').string.replace('\n', '').strip()
    filename = re.sub('[^A-Za-z0-9 ]+', '', filename)
    
    #print(new_soup)
    return new_soup, filename, related
#getRawContent("http://127.0.0.1:3000/Can Dogs Eat Shrimp_.html")