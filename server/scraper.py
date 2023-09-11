from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from models import CPU, db

def run_scraper():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    driver.get('https://pcpartpicker.com/products/cpu/')

    # Use WebDriverWait to ensure that the element has loaded
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'category_content')))
    except Exception as e:
        print(f"An error occurred while waiting: {e}")
        driver.quit()
        return

    sleep(1)  # Optional: Additional sleep to allow for any dynamic content

    html = driver.page_source
    print("Fetched HTML.")

    soup = BeautifulSoup(html, 'lxml')

    # Search for the 'category_content' and validate it's not None
    outer_container = soup.find('tbody', {'id': 'category_content'})

    if outer_container is not None:
        for product in outer_container.find_all('tr', {'class': 'tr__product'}):
            try:
                name = product.find('div', {'class': 'td__nameWrapper'}).text.strip()
                core_count = int(product.find('td', {'class': 'td__spec td__spec--1'}).text.strip().split('\n')[-1])
                performance_core_clock = float(product.find('td', {'class': 'td__spec td__spec--2'}).text.strip().split('\n')[-1].replace(" GHz", ""))
                price = float(product.find('td', {'class': 'td__price'}).text.strip().replace("$", ""))
                
                print(f"Adding CPU: {name}, Core Count: {core_count}, Clock: {performance_core_clock}, Price: {price}")

                new_cpu = CPU(
                    name=name,
                    core_count=core_count,
                    performance_core_clock=performance_core_clock,
                    price=price
                )

                db.session.add(new_cpu)
                db.session.commit()
                print("Successfully added and committed.")
            except Exception as e:
                print(f"An error occurred: {e}")
                db.session.rollback()
    else:
        print("Could not find the category_content.")

    driver.quit()
