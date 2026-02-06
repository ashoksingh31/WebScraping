import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = []

for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").get_text(strip=True)
    author = quote.find("small", class_="author").get_text(strip=True)

    quotes.append({
        "quote": text,
        "author": author
    })

df = pd.DataFrame(quotes)
df.to_csv("quotes.csv", index=False)

print(f"Scraped {len(df)} quotes")
