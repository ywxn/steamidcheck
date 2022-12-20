import requests
from bs4 import BeautifulSoup

def check(id):
    if len(id) == 1:
        return False
    elif BeautifulSoup(requests.get("https://steamcommunity.com/id/" + id).content, 'html.parser').select_one("#message > h3:nth-child(3)") is not None:
        return True
    else:
        return False

def main():
    f = open('freeids.txt', 'a')
    words = open('words_alpha.txt').read().splitlines()
    total = len(words)
    current = 0
    for i in words:
        current = current + 1
        print('Checking ' + i + '...' + ' | ' + str(current) + '/' + str(total))
        if check(i) == True:
            print(i + ' is free!')
            f.write(i+'\n')
            f.flush()
    print('FINISHED!')


if __name__ == "__main__":
    main()
