# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
from bs4 import BeautifulSoup

with open("Day45_WebScraping_BeautifulSoup\website.html", 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")
print(f"The complete title (with tags) is {soup.title}")
print(f"Only the actual text of the title: {soup.title.string}")
# print(soup.prettify()) # adds tabs to HTML in print for better readability
print(soup.a) # Prints the first anchor tag found

all_anchor_tags = soup.find_all(name="a") # Return all of the anchor tags



for tag in all_anchor_tags: 
    print(tag.getText()) # Get a list of all text associated with the anchor tags
    list_of_links = tag.get("href") # will give all links

heading = soup.find(name="h1", id="name") # Finds the first instance of an element with this name AND id.
section_heading = soup.find(name="h3", class_="heading") # Looking for h3 element with a certain class. The underscore is needed because class is a reserved word in python.
print(section_heading.getText()) # Returns only the TEXT that is displayed on the page.

company_url = soup.select_one(selector="p a") # Looking for a specific element that is an anchor (a) tag that is inside a paragraph (p) tag. Uses a CSS selector.
print(company_url)

# From quiz using different HTML source code.
soup.select("li a") # find all anchor tags within a li tag.

#HTML:
# <form method="get" action="/search/">
#  <input type="text" name="q" maxlength="255" value=""></input>
# </form> 

form_tag = soup.find("input")
max_length = form_tag.get("maxlength") #Get the value of maxlength



