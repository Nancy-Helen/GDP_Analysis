import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

table = soup.find("table", {"class": "wikitable"})

df = pd.read_html(str(table))[0]
df.to_csv("GDP_wikipedia.csv",index=False)
