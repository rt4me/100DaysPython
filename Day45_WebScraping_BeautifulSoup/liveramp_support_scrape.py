import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Or FirefoxOptions
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(filename)s:%(lineno)s - %(funcName)s() ] %(levelname)s %(message)s')

base_url = "https://docs.liveramp.com/connect/en/"
first_page = f"{base_url}getting-started.html"

def get_main_body_text(url):

    logging.info(f"Fetching text from URL: {url}")
    try:
        page_name = url.split('.')[0]
        response = requests.get(f"{base_url}{url}")
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        page = response.text
        soup_main = BeautifulSoup(page, "html.parser")
        body = soup_main.find_all("p")
        logging.debug(f"The body of the scraped page: \n {body}")
        logging.info(f"Successfully fetched and parsed text from: {url}")

        # Extract and format text
        text_content = "\n".join(p.get_text(separator="\n", strip=True) for p in body)

        # Save to file
        filename = f"LiveRamp Support Site - {page_name}.txt"
        with open(f"Day45_WebScraping_BeautifulSoup\\LiveRamp_Output\\{filename}", "w", encoding="utf-8") as f:
            f.write(text_content)

        logging.info(f"Successfully fetched and saved text from: {url} to {filename}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL {url}: {e}")
    except Exception as e:
        logging.error(f"Error processing URL {url}: {e}")

try:
    # Configure Chrome options (headless mode is recommended)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in the background
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (sometimes needed in headless mode)
    logging.info("Chrome options configured.")

    # Initialize the Chrome driver (make sure you have ChromeDriver installed and in your PATH)
    driver = webdriver.Chrome(options=chrome_options)
    logging.info("Chrome driver initialized.")

    driver.get(first_page)
    logging.info(f"Navigated to base URL: {first_page}")

    # Give the page time to load and JavaScript to execute (adjust the sleep time as needed)
    time.sleep(5)  # Wait 5 seconds
    logging.info("Waited for 5 seconds for page to load.")

    # Get the rendered HTML source
    html = driver.page_source
    logging.info("Page source retrieved.")

    # Close the browser
    driver.quit()
    logging.info("Chrome driver quit.")

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)

    # Find the aside element (same as before)
    section_list = soup.find_all("a", {"class": "topic-link section"})
    logging.debug(f"List of Sections found: /n{section_list}")
    list_of_href = []
    
    for section in section_list:
        href = section['href']
        logging.debug(f"Adding {href} to list")
        list_of_href.append(href)

    logging.info(f"Found {len(list_of_href)} hrefs in the section list.")

    for href in list_of_href:
        logging.info(f"Sending {href} to get_main_body_text.")
        get_main_body_text(href)
        time.sleep(30) # Add wait time to not overwhelm server.

except Exception as e:
    logging.error(f"An error occurred in the main process: {e}")
except Exception as e:
    print(f"An error occurred: {e}")