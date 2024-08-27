# web scrapping

import requests
from bs4 import BeautifulSoup

url = "https://www.cricbuzz.com/cricket-match/live-scores"

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")
print(soup.prettify())

# get full html code of the web page