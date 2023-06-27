from getContent import getRawContent
from makeMD import makeMD
from rewrite import getrewrite

def main():    
    site_data, title, related = getRawContent("http://127.0.0.1:3000/Can Dogs Eat Shrimp_.html")
    makeMD(site_data, title, related) 
    newtext = getrewrite(title)
    
if __name__ == "__main__":
    main()