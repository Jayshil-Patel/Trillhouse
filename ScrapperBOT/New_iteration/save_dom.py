# filename: save_dom.py
import requests
from bs4 import BeautifulSoup

# URL of the Amazon product page
url = "https://www.amazon.ca/LG-24MP40A-C-FreeSync-OnScreen-Charcoal/dp/B0B273TFXW/ref=sr_1_5?crid=XY26YA6IVWGL&keywords=monitor&qid=1707062618&sprefix=monitor%2Caps%2C103&sr=8-5&th=1"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Save the DOM to a file with UTF-8 encoding
with open('dom.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))