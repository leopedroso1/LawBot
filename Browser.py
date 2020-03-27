# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:59:03 2020

@author: Leonardo
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select # Support for user interface
from selenium.webdriver.chrome.options import Options # Set browser options


class Browser:

    self.preferences = {
        "download.default_directory": r"C:\Users\Downloads",
        "plugins.always_open_pdf_externally": True,
        }

    
    def __init__(self): # Constructor
        
        self.browser_options = Options()
        self.browser_options.add_experimental_option("prefs", self.preferences)
        
    def runWebScrapping(self): # function

        self.browser = webdriver.Chrome(executable_path = r'C:\Users\Leonardo\Desktop\Oxford\Webscrapping\chromedriver', options= self.browser_options) 
        self.browser.maximize_window()
        
        self.browser.get('https://dje.tjsp.jus.br/cdje/index.do;jsessionid=904E03097EDCF133765EE6CB860DFD6B.cdje2') # WARNING: TRANSFORM IN GLOBAL VARIABLE

