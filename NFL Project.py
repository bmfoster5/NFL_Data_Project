#NFL Project

#Import necessary libraries
import requests
from bs4 import BeautifulSoup
#URL of hte webpage to scrape data from
url = 'https://www.pro-football-reference.com/'
#Send the GET request to the webpage
response = requests.get(url)
#Check to see if request was successful
if response.status_code == 200:
    #Parse HTML content using BeautifulSoup Library
    soup = BeautifulSoup(response.text, 'html.parser')
    #Example: Extract all links
    links = soup.find_all('a')
    for link in links: 
        print(link.get('href'))
    else:
        print(f"Failed to retrieve webpage. Status code: {response.status_code}")
#Example: Extract all headings
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
for heading in headings:
    print(heading.text.strip)
