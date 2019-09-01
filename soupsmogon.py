from bs4 import BeautifulSoup
import requests

#get function accesses the webpage
result = requests.get("https://www.smogon.com/dex/sm/pokemon/arceus-electric/")

# need to get 200 which means this site is accessible
# print(result.status_code)

#get header
# print(result.headers)

#store the content, can print this to see what we get need BS4 to parse it
src = result.content

#pass to bs4 class to get a soup object
soup = BeautifulSoup(src, 'lxml')  #need to put lxml there to dodge warnings
# we want links so we target the "a" tag 
links = soup.find_all("p")
print(links)

