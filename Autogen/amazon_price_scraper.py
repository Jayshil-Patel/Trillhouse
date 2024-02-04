# filename: amazon_price.py
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.ca/LG-24MP40A-C-FreeSync-OnScreen-Charcoal/dp/B0B273TFXW/ref=sr_1_5?crid=XY26YA6IVWGL&keywords=monitor&qid=1707062618&sprefix=monitor%2Caps%2C103&sr=8-5&th=1"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

price = soup.select_one(".a-price-whole").get_text()

print("The price is:", price)