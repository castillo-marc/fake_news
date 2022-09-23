# from bs4 import BeautifulSoup
# import requests
import re


# def scraper(url):
#     try:
#         content = requests.get(url, timeout=30)
#         soup = BeautifulSoup(content.text, 'html.parser')

#         text = soup.findAll('p')
#         text = [word.text for word in text]
#         text = ' '.join(text)
#         text = re.sub('\W+', ' ', re.sub('xa0', ' ', text))
#     except: 
#          print("Couldn't parse website")

#     return text

# commenting out everything aside from clean_text
def clean_text(text):
    text = re.sub("[^a-zA-Z]", " ", text.lower())
    return text

# if __name__ == "__main__":
#     scraped = scraper("https://www.frontiersin.org/articles/10.3389/fpsyg.2020.566790/full")
#     print(clean_text(scraped))