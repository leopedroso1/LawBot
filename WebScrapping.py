# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:59:03 2020

"""
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import Select # Support for user interface
from selenium.webdriver.chrome.options import Options # Set browser options


class Browser:

    
    def __init__(self): 

        self.preferences = {
                "download.default_directory": r"C:\Users\Downloads",
                "plugins.always_open_pdf_externally": True,
                }        
        
        self.browser_options = Options()
        self.browser_options.add_experimental_option("prefs", self.preferences)
        
    def runWebScrapping(self): # function

        self.browser = webdriver.Chrome(executable_path = r'C:\Users\Leonardo\Desktop\Oxford\Webscrapping\chromedriver', options= self.browser_options) 
        self.browser.maximize_window()
        
        self.browser.get('https://dje.tjsp.jus.br/cdje/index.do;jsessionid=904E03097EDCF133765EE6CB860DFD6B.cdje2') # WARNING: TRANSFORM IN GLOBAL VARIABLE
        
        select_cadastro = Select(self.browser.find_element_by_id('cadernos'))
        select_cadastro.select_by_value("2") # 2 = caderno 3 - Judicial - 1ª Instância - Capital

        time.sleep(5)
        
        elem_consulta = self.browser.find_element_by_id('consultar')
        elem_consulta.click()
        
        time.sleep(5)
        
        width = int((pyautogui.size()[0]) / 2)
        height = int((pyautogui.size()[1]) / 2) 
        
        time.sleep(3)
        
        pyautogui.moveTo(width,height)
        
        time.sleep(3)
        
        pyautogui.click()
        
        time.sleep(3)
        
        pyautogui.hotkey('enter')
        
        time.sleep(3)
        
        pyautogui.hotkey('enter')
 
        time.sleep(2)

        pyautogui.hotkey('alt','s')
