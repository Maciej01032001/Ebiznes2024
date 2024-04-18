from selenium import webdriver
import unittest
import empik_functions as ef


class EmpikSetupTeardown(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        ef.open_empik(self.driver)
        ef.accept_cookies(self.driver)
