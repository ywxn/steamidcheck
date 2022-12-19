import requests
from bs4 import BeautifulSoup

    
def parseWords():
    with open('words_alpha.txt') as list_words:
        words = set(list_words.read().split())
        return words

def check(id):
    if BeautifulSoup(requests.get("https://steamcommunity.com/id/" + id).content, 'html.parser').select_one("#message > h3:nth-child(3)") is not None:
        return True
    else:
        return False

def main():
    f = open("freeids.txt", "a")
    words = parseWords()
    for i in words:
        print("Checking " + i + "...")
        if check(i) == True:
            print(i + " is free!")
            f.write(i+"\n")
            f.flush()


if __name__ == "__main__":
    main()