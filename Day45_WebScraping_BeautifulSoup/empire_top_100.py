import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(filename)s:%(lineno)s - %(funcName)s() ] %(levelname)s %(message)s')

base_url = 'https://www.empireonline.com/movies/features/best-movies-2/'
filename = '100_top_movies.txt'

def get_list_of_movies(url):
    
    logging.info(f"Fetch text from url: {url}.")

    try:
        response = requests.get(f"{url}")
        page = response.text
        soup_main = BeautifulSoup(page, "html.parser")
        
    
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL {url}: {e}")
    except Exception as e:
        logging.error(f"Error processing URL {url}: {e}")
    
    movie_list = soup_main.find_all('strong')
    
    print(movie_list)

    # with open(f"Day45_WebScraping_BeautifulSoup\\{filename}", "w", encoding="utf-8") as f:
    #             f.write(text_content)
    
    
    
    if __name__ == "__main__":
        get_list_of_movies(base_url)