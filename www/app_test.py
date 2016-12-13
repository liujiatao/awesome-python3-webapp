#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
'''
sample firefox browser test.
'''
# http://selenium-python.readthedocs.io/getting-started.html
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DevOps4Python(unittest.TestCase):

    def setUp(self):
        self.display = Display(visible=0, size=(1600, 900))
        self.display.start()

        # now Firefox will run in a virtual display. 
        # you will not see the browser.
        #self.driver = webdriver.PhantomJS()
        self.driver = webdriver.Firefox()

    # automation test in web browser 
    def test_mainpage_in_python(self):
        driver = self.driver
        driver.get("http://127.0.0.1:9000")
        self.assertIn("日志", driver.title)
        assert "No results found." not in driver.page_source
        body = self.driver.find_element_by_css_selector('body')        
        driver.save_screenshot('mainpage.png')        
        logging.info('mainpage body: \"' + body.text)

    # automation test in restful 
    def test_restful_users_in_python(self):
        driver = self.driver
        driver.get("http://127.0.0.1:9000/api/users")
        assert "404: Not Found" not in driver.page_source
        body = self.driver.find_element_by_css_selector('body')
        driver.save_screenshot('api-users.png')
        logging.info('restful api/users body: \"' + body.text)

    def tearDown(self):
        self.driver.close()
        self.display.stop()


if __name__ == "__main__":
    unittest.main()


