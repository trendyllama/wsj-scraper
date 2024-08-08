'''
'''
import random
import requests
import bs4

URL = 'https://www.wsj.com/'


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
]


HEADERS = {
    'User-Agent': random.choice(USER_AGENTS)
}

CLASS_OF_HEADLINES = ''
TAG_OF_HEALINES = ''



def main() -> None:
    

    r = requests.get(url=URL, headers=HEADERS, timeout=2)

    soup = bs4.BeautifulSoup(markup=r.content)

    articles = soup.find_all(name=TAG_OF_HEALINES, attrs={'class': CLASS_OF_HEADLINES})

    for article in articles:
        print(article)







if __name__ == "__main__":
    main()