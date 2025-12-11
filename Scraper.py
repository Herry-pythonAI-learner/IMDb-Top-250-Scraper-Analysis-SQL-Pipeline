import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


Cache_file = 'MoviesCache.html'
URL = 'https://www.imdb.com/chart/top/?ref_=hm_nv_menu&sort=user_rating%2Cdesc'

def get_imdb_movies():

    print("Lunching real browser...")
    chrome_options =Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(URL)
        print("Waiting for page to load or redirect...")
        time.sleep(10)

        html_content = driver.page_source

        if "The Shawshank Redemption" in html_content:
            print("Page loaded successfully!!")
            with open(Cache_file, 'w',encoding="utf-8") as file:
                file.write(html_content)
                print(f'Data saved to {Cache_file} succefully!!')

        else:
            print("Failed to load the page correctly")

    except Exception as e:
        print(f'An error occured: {e}')

    finally:
        print("Closing the browser...")
        driver.quit()

if __name__ == "__main__":
    get_imdb_movies()

    
      