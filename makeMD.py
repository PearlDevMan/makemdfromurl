from bs4 import BeautifulSoup as bs

def makeMD(soup, related):
    pretty_text=''
    for tag in soup.find_all(True):
        if(len(tag.get_text())):
            str = ""
            if(tag.name == 'h1'):
                str = '#' + tag.get_text().strip() + '\n'
            
            if(tag.name == 'h2'):
                str = '##' + tag.get_text().strip() + '\n'
            
            if(tag.name == 'h3'):
                str = '##' + tag.get_text().strip() + '\n'
            
            if(tag.name == 'p' and not "AKC is a participant" in tag.get_text()):
                str = tag.get_text().strip() + '\n\n'

            pretty_text += str

    if(related != ""):
        pretty_text += related
    return pretty_text
