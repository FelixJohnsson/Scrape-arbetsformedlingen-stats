from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
num_of_pages = 34


base_url = 'https://arbetsformedlingen.se/platsbanken/annonser?p=5:DJh5_yyF_hEM&l=2:CifL_Rzy_Mku&page='

for page_num in range(1, num_of_pages+1):
    # Navigate to the website
    url = base_url + str(page_num)
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    # Get the rendered HTML content
    page_source = driver.page_source

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract the job titles
    divs = soup.find_all('div', class_='card-container')

    for div in divs:
        title = div.find('h3').text
        header_div = div.find('div', class_='header-container')
        company_name = header_div.find('strong', class_='pb-company-name').text
        link = header_div.find('a')['href']

        description = div.find('div', class_='pb-job-role ng-star-inserted').text
        
        # Write to file
        with open('jobs.txt', 'a', encoding='utf-8') as f:
            f.write('Page ' + str(page_num) + '\n')
            f.write(title + '\n')
            f.write(company_name + '\n')
            f.write(link + '\n')
            f.write(description + '\n')
            f.write('\n')

    #Add a delay between requests to be respectful to the server
    time.sleep(random.randint(5,15))

# Close the browser
driver.quit()