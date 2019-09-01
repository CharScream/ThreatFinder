import json
import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.smogon.com/dex/sm/pokemon/arceus-electric/")
src = request.content
print(src)