from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from empik_setup_teardown import EmpikSetupTeardown
import empik_functions as ef


class TestEmpikCasesBasicUserInteraction(EmpikSetupTeardown):
    def test_1_search_item(self):
        phrase_to_search = "Harry Potter"
        expected_title = "Fraza: harry potter - Empik"
        expected_url = "https://www.empik.com/szukaj/produkt?q=harry%20potter&qtype=basicForm"

        ef.search_item(self.driver, phrase_to_search)
        self.assertEqual(self.driver.title, expected_title, "Bad title")
        self.assertEqual(self.driver.current_url, expected_url, "Bad URL address")

    def test_2_get_first_search_title(self):
        phrase_to_search = "Harry Potter"
        expected_title = "Plecak szkolny Dwukomorowy Harry Potter Hogward - Inna marka | Sklep EMPIK.COM"
        expected_url = "https://www.empik.com/plecak-szkolny-dwukomorowy-harry-potter-hogward-karacter-mania," \
                       "p1469061111,szkolne-i-papiernicze-p?mpShopId=9963 "

        ef.search_item(self.driver, phrase_to_search)
        first_search_item = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR,
                                            ".search-list-item.js-reco-product.js-energyclass-product.ta"
                                            "-product-tile")))

        search_title = first_search_item.find_element(By.CSS_SELECTOR, "strong.ta-product-title").text
        search_price = first_search_item.find_element(By.CSS_SELECTOR, "div.price.ta-price-tile").text.strip()
        search_brand = first_search_item.find_element(By.CSS_SELECTOR, "a.smartAuthor").text

        ef.click_first_result_item(self.driver)

        page_title = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "h1[data-ta='title'].css-9rngxa-title"))).text
        page_price = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR,
                                            "span[data-ta='price'].css-1f0k13e-DesktopPriceStyles"))).text.strip()
        page_brand = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "a.css-wdj6e1-author-smartAuthorLink"))).text

        self.assertEqual(search_title, page_title,
                         f"Search Title: '{search_title}', Product Title: '{page_title}'")
        self.assertEqual(search_price, page_price,
                         f"Search Price: '{search_price}', Product Price: '{page_price}'")
        self.assertEqual(search_brand, page_brand,
                         f"Search Brand: '{search_brand}', Product Brand: '{page_brand}'")
        self.assertEqual(self.driver.title, expected_title, "Bad title")
        self.assertEqual(self.driver.current_url, expected_url, "Bad URL address")

    def test_3_empty_cart(self):
        expected_title = "Koszyk"
        expected_url = "https://www.empik.com/cart/"
        expected_purchase_price = "0,00 zł"

        cart_link = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, "simple-dropdown4")))
        cart_link.click()

        empty_cart_element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "p.css-z8hido-emptyCartTitle")))
        purchase_price_element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "span[data-ta='purchase-price'].css-18ewk7h")))

        self.assertTrue(empty_cart_element.is_displayed(), "Empty cart message is not displayed")
        self.assertTrue(purchase_price_element.is_displayed(), "Purchase price is not displayed")
        self.assertEqual(purchase_price_element.text, expected_purchase_price,
                         f"Expected purchase price: {expected_purchase_price}, Actual purchase price: \
                         {purchase_price_element.text}")
        self.assertEqual(self.driver.current_url, expected_url, "Bad URL address")
        self.assertEqual(self.driver.title, expected_title, "Bad title")

    def test_4_add_to_cart(self):
        phrase_to_search = "Harry Potter"
        expected_title = "Koszyk"
        expected_url = "https://www.empik.com/cart/"

        ef.search_item(self.driver, phrase_to_search)
        ef.click_first_result_item(self.driver)

        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "button[data-ta='add-to-cart-btn']")))
        add_to_cart_button.click()

        page_price = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "span[data-ta='price']"))).text
        page_name = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "h1[data-ta='title']"))).text

        go_to_cart_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "button[data-ta='go-to-cart']")))
        go_to_cart_button.click()

        cart_price = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "span[data-ta='products-price']"))).text
        cart_name = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "a[data-ta='product-title']"))).text

        self.assertEqual(page_price, cart_price)
        self.assertEqual(cart_name, page_name)
        self.assertEqual(self.driver.current_url, expected_url, "Bad URL address")
        self.assertEqual(self.driver.title, expected_title, "Bad title")

    def test_5_log_in(self):
        email = "example@mail.com"
        expected_title = "Logowanie - EMPIK"
        expected_url = "https://www.empik.com/logowanie?continue=%2F"

        login_link = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, "simple-dropdown2")))
        login_link.click()

        login_form = self.driver.find_elements(By.ID, "user-login-form")
        self.assertTrue(login_form, "Login form does not exist")

        email_input = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, "user-email")))
        email_input.send_keys(email)

        self.assertEqual(self.driver.title, expected_title, "Bad title")
        self.assertEqual(self.driver.current_url, expected_url, "Bad URL address")

        submit_button = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, ".buttons-group.show button")))
        submit_button.click()

        try:
            __element1 = self.driver.find_elements(By.XPATH, "//h2[contains(text(), 'Witaj ponownie, zaloguj się')]")
            element1_present = True
        except NoSuchElementException:
            element1_present = False

        try:
            __element2 = self.driver.find_elements(By.XPATH, "//h2[contains(text(), 'Rejestracja')]")
            element2_present = True
        except NoSuchElementException:
            element2_present = False

        self.assertTrue(element1_present or element2_present)

    def test_6_registration(self):
        registration_address = "https://www.empik.com/rejestracja?continue=%2Fpomoc%2Frejestracja"
        expected_title = "Rejestracja - EMPIK"
        expected_url = "https://www.empik.com/rejestracja?continue=%2Fpomoc%2Frejestracja"

        self.driver.get(registration_address)

        email_input = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        self.assertTrue(email_input.is_displayed(), "Email input is not present")

        password_input = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        self.assertTrue(password_input.is_displayed(), "Password input is not present")

        phone_number_input = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@name='phoneNumber']")))
        self.assertTrue(phone_number_input.is_displayed(), "Phone number input is not present")

        self.assertEqual(self.driver.title, expected_title, "Bad title")
        self.assertEqual(self.driver.current_url, expected_url, "Bad URL address")
