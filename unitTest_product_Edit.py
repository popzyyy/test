import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "spqr"
        pwd = "spqr"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)

        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div[1]/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a')
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.get("http://127.0.0.1:8000/product/2/edit/")
        time.sleep(3)

        elem = driver.find_element_by_xpath('// *[ @ id = "id_p_description"]')
        elem.clear()
        elem.send_keys("Selenium test 123")
        time.sleep(3)
        elem = driver.find_element_by_xpath('// *[ @ id = "app-layout"] / div[1] / div / div / form / button')
        elem.send_keys(Keys.RETURN)
        time.sleep(3)





        try:

            elem = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/table/tbody/tr/td[3]')
            assert True


        except NoSuchElementException:
            self.fail("Element search failed. xpath or element may not exist")

            assert False

        time.sleep(3)

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()
