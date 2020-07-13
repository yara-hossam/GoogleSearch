import os
import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):
    def setUp(self):
        # get the path of chromedriver
        dir = os.path.dirname(__file__)
        chrome_driver_path = dir + "\chromedriver.exe"
        # create a new Chrome session
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to google's home page
        self.driver.get("http://www.google.com/")


    def test_no_search_text(self):
        #checking that when the search button is clicked with no text entered,
        #the same page is kept opened
        # get the current url before clicking the button
        exp_url=self.driver.current_url
        search_box = self.driver.find_element_by_name("q")
        search_box.clear()
        search_box.send_keys(" ")
        self.driver.find_element_by_name("btnK").click()
        self.assertTrue(exp_url == self.driver.current_url)


    def test_search_result_compatible(self):
        #checking the resulted page includes url that correctly redirects to the required search text
            # get the search textbox
            search_box = self.driver.find_element_by_name("q")
            search_box.clear()
            #write youtube then click the search button
            search_box.send_keys("youtube")
            self.driver.find_element_by_name("btnK").click()
            div = self.driver.find_element_by_class_name('r')
            result=div.find_element_by_css_selector('a').get_attribute('href')
            #print(result)
            self.assertTrue("youtube.com" in result)


    def test_search_suggestions(self):
    #checking if the suggessions list include the required text entered in the search textbox
        suggestions_list=[]
        str="facebook"
        search_box = self.driver.find_element_by_name("q")
        search_box.clear()
        search_box.send_keys(str)
        #getting the suggestions list text content
        elements = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/ul')
        suggestions = elements.find_elements_by_css_selector("li[class='sbct']")
        for element in suggestions:
           str_to_append=element.text
           #print(str_to_append.lower())
           suggestions_list.append(str_to_append.lower())
        self.assertTrue(str in suggestions_list)


    
    def tearDown(self):
    #closing browsers windows
     self.driver.quit()


