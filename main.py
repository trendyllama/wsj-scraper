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


# Example Headline HTML Element

# <span class="WSJTheme--headlineText--He1ANr9C ">Harris Makes Risky Bet That Walz Can Prop Up Blue Wall</span>

CLASS_OF_HEADLINES = 'span'
TAG_OF_HEALINES = 'WSJTheme--headlineText--He1ANr9C'



def main() -> None:
    

    r = requests.get(url=URL, headers=HEADERS, timeout=2)

    if r.status_code != '200':

        print(f'request failed with code {r.status_code} \n\n {r.text}')
        
        raise SystemExit

    soup = bs4.BeautifulSoup(r.content, 'html.parser')



    articles = soup.find_all(name=TAG_OF_HEALINES, attrs={'class': CLASS_OF_HEADLINES}, recursive=True)

    print(articles)
    for article in articles:
        print(article)







if __name__ == "__main__":
    main()