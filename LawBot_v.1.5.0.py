# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:46:01 2020

@title: Webscrapping from Oficial News from Justice Court of São Paulo
@author: Leonardo Pedroso dos Santos - CTO

"""

import sys
import WebScrapping


# Dependencies: Selenium and Pyautogui
# Select 1.000 pages once

#import time
#import pyautogui
#from selenium import webdriver
#from selenium.webdriver.support.ui import Select # Support for user interface
#from selenium.webdriver.chrome.options import Options # Set browser options

   
if __name__ == "__main__":
    
    try:
        controller = WebScrapping.Browser()
        controller.runWebScrapping()
        controller.browser.close()
        
    except:
        
        print(sys.exc_info)
    

   
    


    



