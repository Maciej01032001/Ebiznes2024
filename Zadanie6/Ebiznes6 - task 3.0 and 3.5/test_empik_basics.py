from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import unittest
import empik_functions as ef


class TestEmpikCasesBasics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        ef.open_empik(self.driver)

    def test_1_open_empik(self):
        self.assertIn("Empik.com | 5 000 000 produktów i pomysłów na prezent | Dostawa za 0 zł z Empik Premium",
                      self.driver.title, "Failed to open Empik website")
        self.assertEqual(self.driver.current_url, "https://www.empik.com/")

    def test_2_accept_cookies(self):
        try:
            accept_button = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@data-ta='cookie-btn-accept-all']"))
            )
        except TimeoutException:
            accept_button = None

        self.assertIsNotNone(accept_button, "Accept cookies button is not present")
        ef.accept_cookies(self.driver)
