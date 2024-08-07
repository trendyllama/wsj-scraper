'''
'''
import random
import requests
import bs4

URL = 'https://www.wsj.com/'

USER_AGENTS = []

HEADERS = {

}

CLASS_OF_HEADLINES = ''
TAG_OF_HEALINES = ''



def main() -> None:
    

    r = requests.get(url=URL, headers=HEADERS, timeout=2)

    soup = bs4.BeautifulSoup(markup=r.content)

    articles = soup.find_all(name=TAG_OF_HEALINES, attrs={'class': CLASS_OF_HEADLINES})







if __name__ == "__main__":
    main()