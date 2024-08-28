# web scrapping
# import beautiful soup library
import requests
from bs4 import BeautifulSoup

url = "https://www.cricbuzz.com/cricket-match/live-scores"

r = requests.get(url)

data = r.text

print(data)