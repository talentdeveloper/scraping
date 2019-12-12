import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# class PythonOrgSearch(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()

#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("https://www.google.com/")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No result found." not in driver.page_source

#     def tearDown(self):
#         self.driver.close()






driver = webdriver.Chrome()
driver.get("http://www.google.com")
# assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()


if __name__ == "__main__":
    unittest.main()
        