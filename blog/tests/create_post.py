import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class create_post_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.admin_username = 'instructor'
        self.admin_password = 'maverick1a'
        self.admin_url = 'http://127.0.0.1:8000/admin/'
        self.new_post_url = 'http://127.0.0.1:8000/admin/app/post/add/'
        self.posts_url = 'http://127.0.0.1:8000/admin/app/post/'

    def test(self):
        #Logging in as instructor
        driver = self.driver
        driver.get(self.admin_url)
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(self.admin_username)
        time.sleep(1)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(self.admin_password)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        assert("Logged In")
        time.sleep(1)

        #Submitting new post
        driver.get(self.new_post_url)
        time.sleep(1)
        select = Select(driver.find_element_by_id("id_author"))
        select.select_by_index(2)
        time.sleep(1)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("Test Post")
        time.sleep(1)
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("Test Post Text")
        time.sleep(1)
        elem = driver.find_element_by_xpath("//input[@value='Save']").click()
        assert("Post Submited")
        time.sleep(1)

        #Verifying the post exists
        driver.get(self.posts_url)
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[contains(text(), 'Test Post')]")
        assert("Logged In")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()
