from getContent import getRawContent
from makeMD import makeMD

def main():    
    site_data, title, related = getRawContent("http://127.0.0.1:3000/Can Dogs Eat Shrimp_.html")
    makeMD(site_data, title, related) 
if __name__ == "__main__":
    main()