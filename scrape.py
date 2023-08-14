import requests
from bs4 import BeautifulSoup

# Define the URL you want to scrape from
url = 'https://arbetsformedlingen.se/platsbanken/annonser?p=5:DJh5_yyF_hEM&q=developer'

response = requests.get(url)
response.raise_for_status()  # Raise an exception for HTTP errors

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.title.string
print(f"Title of the webpage: {title}")