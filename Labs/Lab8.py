# import of non-built=in modules to make http requests
import requests
from bs4 import BeautifulSoup
# get html from site
url ='https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life'
response = requests.get(url)
headers = response.headers
body = response.text[:2000]
# drill down into html to grab desired info -- quotes and "authors" of said quotes
html = BeautifulSoup(response.text, 'html.parser')
quotes = html.findAll('strong')
#print (quotes)
# clean up data -- remove unwanted html and make it more readable
for quote in quotes:
        text_only_quote = quote.text
        print(text_only_quote)
