import os
import requests
import unittest
import time 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        os.environ['NO_PROXY'] = '0.0.0.0'
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
 
    # executed after each test
    def tearDown(self):
    	self.driver.quit()

    ###############
	#### tests ####
	###############
    
    def test_a_index(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.status_code, 200)

    def test_b_search(self):
    	## Connect to localhost
        self.driver.get('http://localhost:5000/')  # Assuming default Flask port
        self.driver.implicitly_wait(10)

        ## Check input
        sentence_input = self.driver.find_element_by_name('sentence')

        ## Fill input
        sentence_input.send_keys('fraud')

        ## Check submit button and submit form
        submit_button = self.driver.find_element_by_name('button_submit')
        submit_button.send_keys(Keys.ENTER)

        time.sleep(3)

        ## Check if no redirect ( may delete )
        new_url = self.driver.current_url
        self.assertEqual(new_url, 'http://localhost:5000/')

        ## Get face value
        first_tweet = self.driver.find_element_by_id("1")
        tweet_content = first_tweet.find_elements_by_tag_name("td")[1]
        self.assertIn('My opponent is a fraud !',tweet_content.text)
        # face_picture = self.driver.find_element_by_name('sentiment-face')
        # self.assertIn('positive_face.png', face_picture.get_attribute("src"))

if __name__ == '__main__':
    unittest.main()		
