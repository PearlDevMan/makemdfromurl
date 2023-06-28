from getContent import getRawContent
from makeMD import makeMD
from rewrite import getrewrite
from translate import translate
def main():    
    site_data, title, related = getRawContent("http://127.0.0.1:3000/Can Dogs Eat Shrimp_.html")
    beauty_text = makeMD(site_data, related) 
    newtext = getrewrite(beauty_text, title)
    translate(newtext, title, "IT")
    
if __name__ == "__main__":
    main()