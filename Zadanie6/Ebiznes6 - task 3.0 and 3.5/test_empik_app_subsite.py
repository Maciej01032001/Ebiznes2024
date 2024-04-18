from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from empik_setup_teardown import EmpikSetupTeardown


class TestEmpikCasesSubsite(EmpikSetupTeardown):
    def test_gifts(self):
        expected_header = "Miliony trafionych prezentów"

        gifts_link = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Prezenty")))
        gifts_link.click()

        tag_element = self.driver.find_element(By.CLASS_NAME, "tina-tag")
        self.assertTrue(tag_element.is_displayed())

        title_tag_element = tag_element.find_element(By.CLASS_NAME, "tina-tag__title")
        self.assertEqual(title_tag_element.text, "Prezenty")

        header_element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "univ-header__text")))
        self.assertTrue(header_element.is_displayed())

        self.assertEqual(header_element.text, expected_header)

    def test_top_100(self):
        expected_header = "TOP 100 - najlepiej sprzedające się produkty w empik.com"
        expected_option = "Bestsellery tygodnia"

        top_100_link = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Top 100")))
        top_100_link.click()
        header_element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH,
                                            "//div[@class='boxesHeader searchHeader displayInlineBlock "
                                            "js-searchHeader']/h2[@class='whiteBox__title ta-title']")))

        self.assertTrue(header_element.is_displayed())
        self.assertEqual(header_element.text.strip(), expected_header)

        select_element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, "search-sort-select")))
        self.assertTrue(select_element.is_displayed())

        selected_option = select_element.find_element(By.CSS_SELECTOR, "option[selected='selected']")
        self.assertEqual(selected_option.text.strip(), expected_option)

    def test_promotions(self):
        expected_promo_title = "Promocje Empik"
        expected_promo_online = "Promocje online"

        promo_link = self.driver.find_element(By.LINK_TEXT, "Promocje")
        promo_link.click()

        promo_title_element = self.driver.find_element(By.CLASS_NAME, "tina-tag__title")
        self.assertTrue(promo_title_element.is_displayed())
        self.assertEqual(promo_title_element.text, expected_promo_title)

        promo_online_element = self.driver.find_element(By.XPATH,
                                                        "//h2[contains(@class, 'univ-header') and contains(text(), "
                                                        "'Promocje online')]")
        self.assertTrue(promo_online_element.is_displayed())
        self.assertEqual(promo_online_element.text, expected_promo_online)

    def test_empik_premium(self):
        expected_title = "Empik Premium | Kup na rok za 39,90 zł"
        expected_element_title = "Oszczędzaj z Premium, nie tylko na dostawie"
        expected_alt_text = "Tydzień promocji z Empik Premium"

        premium_link = self.driver.find_element(By.XPATH, "//a[contains(@href, '/premium')]")
        premium_link.click()

        title_element = self.driver.find_element(By.CSS_SELECTOR, "h1.title.desktop")
        self.assertIsNotNone(title_element)

        self.assertEqual(title_element.text, expected_element_title)
        self.assertEqual(self.driver.title, expected_title, "Wrong title")

        banner_element = self.driver.find_element(By.CSS_SELECTOR, "img.display-desktop.banner-w-100")
        self.assertIsNotNone(banner_element)
        self.assertEqual(banner_element.get_attribute("alt"), expected_alt_text)

    def test_empik_new(self):
        expected_text = "Nowości w empik.com"

        new_link = self.driver.find_element(By.XPATH, "//a[@href='/nowosci']")
        new_link.click()

        self.assertEqual(self.driver.title, "Nowości - 0 zł za dostawę - empik.com", "Wrong title")
        self.assertEqual(self.driver.current_url, "https://www.empik.com/nowosci")

        element = self.driver.find_element(By.XPATH,
                                           "//div[@class='boxesHeader searchHeader displayInlineBlock "
                                           "js-searchHeader']/h2[@class='whiteBox__title ta-title']")
        self.assertTrue(element)
        self.assertEqual(element.text, expected_text)

    def test_empik_culture_tome(self):
        expected_title = "Tom Kultury - gazetka promocyjna Empik"
        expected_url = "https://www.empik.com/tom-kultury"

        tome_link = self.driver.find_element(By.XPATH, "//a[@href='/tom-kultury']")
        tome_link.click()

        self.assertEqual(self.driver.title, expected_title, "Wrong title")
        self.assertEqual(self.driver.current_url, expected_url, "Wrong URL")

        flipbook_element = self.driver.find_element(By.CSS_SELECTOR, "div.flipbook")
        self.assertTrue(flipbook_element)
        iframe_element = flipbook_element.find_element(By.TAG_NAME, "iframe")
        self.assertTrue(iframe_element)

    def test_empik_go(self):
        expected_title = "Empik Go – aplikacja z audiobookami i ebookami - EMPIK"
        expected_url = "https://www.empik.com/go"
        expected_text = "Z nami po prostu masz czas na książkę"

        go_link = self.driver.find_element(By.XPATH, "//a[@href='/go']")
        go_link.click()

        self.assertEqual(self.driver.title, expected_title, "Wrong title")
        self.assertEqual(self.driver.current_url, expected_url, "Wrong URL")

        hero_heading = self.driver.find_element(By.CLASS_NAME, "hero__heading")
        self.assertTrue(hero_heading)
        self.assertEqual(hero_heading.text, expected_text)

    def test_empik_contact(self):
        expected_heading = "Formularz kontaktowy"
        expected_element = "Element not found"

        contact_link = self.driver.find_element(By.CSS_SELECTOR, "a.el-4[title='Kontakt']")
        contact_link.click()

        contact_heading = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "h1.css-1cevg0i-heading")))
        self.assertTrue(contact_heading.is_displayed())
        self.assertEqual(contact_heading.text, expected_heading)

        element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "css-16g4cmo-root")))
        self.assertIsNotNone(element, expected_element)

    def test_empik_mobile_app(self):
        expected_text = "Najlepiej oceniana aplikacja zakupowa w Polsce: 4,9 / 5"

        mobile_link = self.driver.find_element(By.CSS_SELECTOR, "a.el-7[title='Aplikacja mobilna']")
        mobile_link.click()

        header_main = self.driver.find_element(By.CLASS_NAME, "app-header__text__main")
        self.assertTrue(header_main.is_displayed(), "Element is not present")

        header_text = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "app-header__text__about-text")))
        self.assertIsNotNone(header_text, "Element is not present")
        self.assertEqual(header_text.text, expected_text, f"Expected: '{expected_text}', Actual: '{header_text.text}'")

    def test_empik_salons(self):
        expected_header = "Najlepsze promocje w salonach"
        expected_title = "Salony Empik w Twojej okolicy - EMPIK.COM"

        salons_link = self.driver.find_element(By.XPATH, "//a[@href='/salony-empik']")
        salons_link.click()

        header_element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//header[@class='whiteBox__header whiteBox__header--border mw-box-header']"))
        )
        menu_element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-box-type='menu']")))
        self.assertIsNotNone(menu_element, "Element is not present")

        self.assertEqual(header_element.text, expected_header, "Bad header text")
        self.assertEqual(self.driver.title, expected_title, "Bad title")

    def test_empik_business(self):
        expected_title = "Strefa dla Biznesu"
        expected_header = "Pomagamy rozwijać Twój biznes"

        business_link = self.driver.find_element(By.XPATH, "//a[@href='/biznes']")
        business_link.click()

        header_text = self.driver.find_element(By.CLASS_NAME, "b2b-header-text__title").text
        button = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "b2b-header-text__link")))
        self.assertIsNotNone(button, "Element is not present")
        self.assertEqual(header_text, expected_header)
        self.assertEqual(self.driver.title, expected_title)

    def test_empik_become_a_seller(self):
        become_seller_link = self.driver.find_element(By.XPATH, "//a[@href='https://www.empik.com/empikplace']")
        become_seller_link.click()
