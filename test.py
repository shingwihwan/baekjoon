# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

# Set the URL to crawl
url = 'https://searchn.11st.co.kr/pc/deal?kwd=%25ED%258C%25B8%25ED%258D%25BC%25EC%258A%25A4&tabId=DEAL'

# Make a GET request to the URL
response = requests.get(url)

# Parse the response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the items with the class 'item'
items = soup.find_all(class_='item')

# Loop through the items
for item in items:
    # Find the item with the product name 'Pampers'
    if item.find('span', {'class': 'prodNm'}).text == '펨퍼스':
        # Print the product name and price
        print(item.find('span', {'class': 'prodNm'}).text)
        print(item.find('em', {'class': 'sale'}).text)
