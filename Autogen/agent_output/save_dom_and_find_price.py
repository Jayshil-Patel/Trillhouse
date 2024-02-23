# filename: save_dom_and_find_price.py
import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://www.amazon.ca/LG-24MP40A-C-FreeSync-OnScreen-Charcoal/dp/B0B273TFXW/ref=sr_1_5?crid=XY26YA6IVWGL&keywords=monitor&qid=1707062618&sprefix=monitor%2Caps%2C103&sr=8-5&th=1"
response = requests.get(url)

# Save the DOM of the webpage to a file
with open("dom.html", "w", encoding="utf-8") as file:
    file.write(response.text)

# Parse the DOM using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find the price element
price_element = soup.find("span", class_="a-offscreen")

# Extract the price value
price = price_element.text.strip()

# Print the price
print("Price:", price)