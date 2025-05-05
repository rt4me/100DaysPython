import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(filename)s:%(lineno)s - %(funcName)s() ] %(levelname)s %(message)s')

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'
FILENAME = '100_top_movies.txt'

def get_list_of_movies(url):
    
    logging.info(f"Fetch text from url: {url}.")

    try:
        logging.info("Entering try block.")
        response = requests.get(f"{url}")
        page = response.text
        soup = BeautifulSoup(page, "html.parser")
        
    
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL {url}: {e}")
    except Exception as e:
        logging.error(f"Error processing URL {url}: {e}")
    
    # Find all <strong> tags that start with a number
    pattern = re.compile(r'^\d') # Matches strings starting with digit
    elements_with_numbers = [tag.text for tag in soup.find_all('strong') if tag.text and pattern.match(tag.text)]
    
    logging.info(f"Elements with numbers list: {elements_with_numbers}")

    text_content = ""

    # build String in reverse order
    for movie in elements_with_numbers:
          text_content = f"{movie}\n{text_content}"
          

    with open(f"Day45_WebScraping_BeautifulSoup\\{FILENAME}", "w", encoding="utf-8") as f:
                 f.write(text_content)
    
    
    
if __name__ == "__main__":
    logging.info("Starting __main__ run.")
    get_list_of_movies(URL)