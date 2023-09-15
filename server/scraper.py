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
    #options.headless = True
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537"
    options.add_argument(f"user-agent={user_agent}")

    driver = webdriver.Firefox(options=options)

    driver.get('https://pcpartpicker.com/products/cpu/')
    print("URL Loaded")

    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'category_content')))
    except Exception as e:
        print(f"Exception: {e}")
        
        # Debugging - Save the page source
        with open("debug_page_source.html", "w") as f:
            f.write(driver.page_source)
            
        print("Taking screenshot for debugging...")
        driver.save_screenshot("debug_screenshot.png")
        driver.quit()
        return

    print("Wait successful, continue scraping...")
    sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    outer_container = soup.find('tbody', {'id': 'category_content'})

    if outer_container is not None:
        for product in outer_container.find_all('tr', {'class': 'tr__product'}):
            try:
                # Extracting product data
                name = product.select_one('.td__nameWrapper p').text.strip()
                core_count = int(product.select_one('.td__spec--1').text.split('\n')[-1].strip())
                performance_core_clock = float(product.select_one('.td__spec--2').text.split('\n')[-1].strip().replace(' GHz', ''))
                price = float(product.select_one('.td__price').text.strip().replace('$', '').replace(',', ''))

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

# Call the scraper
# if __name__ == "__main__":
#     run_scraper()
