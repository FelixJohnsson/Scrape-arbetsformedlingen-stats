from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import json
import re

options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(options=options)

base_url = 'https://arbetsformedlingen.se'

# Read json file
with open('jobs.json', 'r', encoding='utf-8') as f:
    jobs = json.load(f)

for job in jobs:
    # Navigate to the website
    url = base_url + job['url']
    driver.get(url)

    # Wait for the page to load
    time.sleep(6)

    # Get the rendered HTML content
    page_source = driver.page_source

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the span containing the text 'Omfattning'
    omfattning_span = soup.find('span', string=re.compile(r'Omfattning'))
    varaktighet_span = soup.find('span', string=re.compile(r'Varaktighet'))
    anställningsform_span = soup.find('span', string=re.compile(r'Anställningsform'))

    description = soup.find('div', class_='section job-description')

    if description:
        description = description.text.strip()
    else:
        # Then the JS has not loaded yet, so we need to wait a bit
        time.sleep(5)
        description = soup.find('div', class_='section job-description').text.strip()

    link_to_apply = soup.find('a', string=re.compile(r'Ansök här'))

    if link_to_apply:
        link_to_apply = link_to_apply['href']
    else:
        link_to_apply = 'Cannot find link to apply'

    if omfattning_span:
        next_span = omfattning_span.find_next('span')
        if next_span:
            omfattning_value = next_span.text
            job['omfattning'] = omfattning_value
            print(f"Omfattning {omfattning_value} for job: {job['title']}")
    else:
        print(f"Omfattning span not found for job: {job['title']}")

    if varaktighet_span:
        next_span = varaktighet_span.find_next('span')
        if next_span:
            varaktighet_value = next_span.text
            job['varaktighet'] = varaktighet_value
            print(f"Varaktighet {varaktighet_value} for job: {job['title']}")

    if anställningsform_span:
        next_span = anställningsform_span.find_next('span')
        if next_span:
            anställningsform_value = next_span.text
            job['anställningsform'] = anställningsform_value
            print(f"Anställningsform {anställningsform_value} for job: {job['title']}")

    if link_to_apply:
        job['link_to_apply'] = link_to_apply
        print(f"Link to apply {link_to_apply} for job: {job['title']}")

    if description:
        job['description'] = description

    # Add a delay between requests to be respectful to the server
    time.sleep(random.randint(3, 5))

# Write to file outside the loop
with open('jobs.json', 'w', encoding='utf-8') as f:
    json.dump(jobs, f, ensure_ascii=False, indent=4)