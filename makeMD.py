from bs4 import BeautifulSoup as bs

def makeMD(soup, name, related):
    filename = name + ".txt"
    with open(filename, 'w') as f:
        for tag in soup.find_all(True):
            if(len(tag.get_text())):
                if(tag.name == 'h1'):
                    str = '#' + tag.get_text().strip() + '\n'
                    f.write(str)
                
                if(tag.name == 'h2'):
                    str = '##' + tag.get_text().strip() + '\n'
                    f.write(str)
                
                if(tag.name == 'h3'):
                    str = '##' + tag.get_text().strip() + '\n'
                    f.write(str)
                
                if(tag.name == 'p' and not "AKC is a participant" in tag.get_text()):
                    str = tag.get_text().strip() + '\n\n'
                    f.write(str)

        if(related != ""):
            f.write(related)
        f.close