import requests
from bs4 import BeautifulSoup

# URL to be scraped
url = "https://www.geeksforgeeks.org/"

req = requests.get(url)

soup = BeautifulSoup(req.content,"html.parser") 
res = soup.title  

print(res.get_text()) # prints the content of the website