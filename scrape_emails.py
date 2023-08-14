from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import json

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
num_of_pages = 34

base_url = 'https://arbetsformedlingen.se'

# Read json file
with open('jobs.json', 'r', encoding='utf-8') as f:
    jobs = json.load(f)

for job in jobs:
    # Navigate to the website
    url = base_url + job['url']
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    # Get the rendered HTML content
    page_source = driver.page_source

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')




    #Add a delay between requests to be respectful to the server
    time.sleep(random.randint(5,15))