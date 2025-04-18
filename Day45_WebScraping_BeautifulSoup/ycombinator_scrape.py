import requests
from bs4 import BeautifulSoup

site = 'https://news.ycombinator.com/news'

response = requests.get(site)
yc_web_page = response.text # Save HTML of webpage.

soup = BeautifulSoup(yc_web_page, "html.parser")

# Find the first occurance of Title, URL and Count
# Pull chunk of HTML that contains the first Title line
titleline_element = soup.find('span', {'class': 'titleline'})

# Narrow down the chunk of HTML to just the section with the anchor
title_element = titleline_element.find('a', href=True)
if titleline_element:
    article_title = title_element.text
    article_href = title_element['href']

# Pull group of HTML for the count line of the first Title
count_element = soup.find('span', {'class': 'score' })
upvote_count = count_element.text

# Print the extracted information
# print(f"Article Title: {article_title}")
# print(f"Article Href: {article_href}")
# print(f"Upvote Count: {upvote_count}")


#Find the Title, URL and Count of the listing on the page with the highest Count.
title_list = []
href_list = []
count_list = []
title_elements = titleline_element.find_all('a', href=True)
if titleline_element:
    for element in title_elements:
        print(element)
        title_list.append(title_element.getText())
        href_list.append(title_element['href'])


# Get list of Upvote counts, splitting from text and changing it to a number so Max() can be performed on it.
count_list = [int((element.text).split()[0]) for element in soup.find_all('span', {'class': 'score' })]
#count_elements = soup.find_all('span', {'class': 'score' })
# for element in count_elements:
#     text = element.text
#     count_list.append(int(text.split()[0]))

max_position = count_list.index(max(count_list))

most_popular_title = title_list[max_position]
most_popular_href = href_list[max_position]
most_populat_count = count_list[max_position]

print(f"The most popular article's Title: {most_popular_title}, URL: {most_popular_href} and Upvote Count: {most_populat_count}")

