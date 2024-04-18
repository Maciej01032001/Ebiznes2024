from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging


def open_empik(driver):
    driver.get("https://www.empik.com/")


def accept_cookies(driver):
    try:
        accept_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@data-ta='cookie-btn-accept-all']"))
        )
        accept_button.click()
    except Exception as e:
        logging.exception(e)


def search_item(driver, product_name):
    try:
        search_box = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, ".main-search__container input[type='search']")))
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)
    except Exception as e:
        logging.exception(e)


def click_first_result_item(driver):
    first_result = driver.find_element(By.CSS_SELECTOR,
                                       ".search-list-item.js-reco-product.js-energyclass-product.ta-product-tile a.img")
    first_result.click()
