# filename: amazon_price_scraper.py
import asyncio
from pyppeteer import launch
from pyppeteer_install import install

async def scrape_amazon_price():
    # Install Chromium
    await install()

    # Launch the browser
    browser = await launch(args=['--no-sandbox'])
    page = await browser.newPage()

    # Navigate to the Amazon product page
    await page.goto("https://www.amazon.ca/LG-24MP40A-C-FreeSync-OnScreen-Charcoal/dp/B0B273TFXW/ref=sr_1_5?crid=XY26YA6IVWGL&keywords=monitor&qid=1707062618&sprefix=monitor%2Caps%2C103&sr=8-5&th=1")

    # Wait for the price element to be visible
    await page.waitForSelector("#priceblock_ourprice")

    # Get the price element and extract the price text
    price_element = await page.querySelector("#priceblock_ourprice")
    price_text = await page.evaluate('(element) => element.textContent', price_element)

    # Print the price
    print("The price of the monitor is:", price_text)

    # Close the browser
    await browser.close()

# Run the scraping function
asyncio.run(scrape_amazon_price())