'''
'''
import random
import requests
import bs4

URL = 'https://www.wsj.com/news/latest-headlines?mod=nav_top_section'


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
    'User-Agent': random.choice(USER_AGENTS),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}



# Example Headline HTML Element

# <span class="WSJTheme--headlineText--He1ANr9C ">Harris Makes Risky Bet That Walz Can Prop Up Blue Wall</span>

CLASS_OF_HEADLINES = 'article'
TAG_OF_HEALINES = 'WSJTheme--headlineText--He1ANr9C '


class RequestError(Exception):
    pass


def main() -> None:
    

    r = requests.get(url=URL, headers=HEADERS, timeout=5)


    match r.status_code:

        case 200:
            
            soup = bs4.BeautifulSoup(r.text, 'html.parser')
        
        case _ :
        
            raise RequestError(f'request failed with code {r.status_code} \n {r.headers} \n {r.text}')


    articles = soup.find_all(name=TAG_OF_HEALINES, attrs={'class': CLASS_OF_HEADLINES}, recursive=True)


    for article in articles:
        print(article)





if __name__ == "__main__":
    main()