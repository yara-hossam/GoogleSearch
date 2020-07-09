import os
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class HomePageTest(unittest.TestCase):
#this class is for testing google's homepage
    @classmethod
    def setUp(cls):
        # get the path of chromedriver
        dir = os.path.dirname(__file__)
        chrome_driver_path = dir + "\chromedriver.exe"
        # create a new Chrome session
        cls.driver = webdriver.Chrome(chrome_driver_path)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to google's home page
        cls.driver.get("http://www.google.com/")

    def test_google_homepage_image(self):
        #check the existence of google's icon to check that we're in the correct page
        try:
            self.driver.find_element_by_id("hplogo")
        except NoSuchElementException:
            self.assertTrue(False)
        self.assertTrue(True)

    def test_search_box_exists(self):
        #check existence of search text box
        try:
            self.driver.find_element_by_name("q")
        except NoSuchElementException:
            self.assertTrue(False)
        self.assertTrue(True)

    def test_max_length_search_box(self):
        # get the search textbox
        search_box= self.driver.find_element_by_name("q")
        # check maxlength attribute is set to 2048
        self.assertEqual("2048", search_box.get_attribute("maxlength"))

    def test_gmail_correctly_redirect(self):
        #check that gmail's icon in the right upper corner redirects to the correct URL
        self.driver.find_element_by_link_text("Gmail").click()
        current_url=self.driver.current_url
        self.assertTrue(current_url,"https://mail.google.com/mail/?tab=wm&ogbl")

    def test_google_images_correctly_redirect(self):
        #check that images icon in the right upper corner redirects to google images page
        #by checking for images subtitle under google's image
        self.driver.find_element_by_link_text("Images").click()
        try:
         self.driver.find_element_by_class_name("logo-subtext")
        except NoSuchElementException :
            self.assertTrue(False)
        self.assertTrue(True)


    @classmethod
    def tearDownClass(cls):
    #close browser windows
     cls.driver.quit()


