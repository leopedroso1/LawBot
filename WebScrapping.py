# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:59:03 2020

@title: Webscrapping from Oficial News from Justice Court of São Paulo
@author: Leonardo Pedroso dos Santos - CTO

"""
import time
import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import Select # Support for user interface
from selenium.webdriver.chrome.options import Options # Set browser options


class Browser:

    
    def __init__(self): 

        self.preferences = {
                "download.default_directory": r"C:\Users\Downloads",
                "plugins.always_open_pdf_externally": True,
                "download.prompt_for_download": False,
                }        
        
        self.browser_options = Options()
        self.browser_options.add_experimental_option("prefs", self.preferences)
        
        self.max_pages = 80 # Amount of pages to be processed
        self.idx = 2 # page index
        self.time_control = 3 # time stamp. Controll the environment time
        self.chrome_driver_path = os.path.dirname(os.path.abspath(__file__)) + '\chromedriver'
        self.stored_pdf_path = os.path.expanduser('~\Documents') 
        
    def cleanEnvironment(self):
        
        print("Cleaning previous PDF files")
                
        if os.path.exists(self.stored_pdf_path + '\diario.pdf'):

            os.remove(self.stored_pdf_path + '\diario.pdf')
            
            idx_files = 2 # Same value of idx because they control the buffer cleaning after execution
            
            while idx_files <= self.max_pages:
            
                file_name = str(self.stored_pdf_path + '\diario' + str(idx_files) + '.pdf')
            
                os.remove(file_name)
                
#                print(idx_files)
                
                idx_files += 1
                       
        else:
            
            pass
        

    def downloadFiles(self):
        
        while self.idx <= self.max_pages:
            
            print("Downloading: "+ str(self.idx) + "/" + str(self.max_pages))
            
            time.sleep(self.time_control) # Running controllers. Otherwise the robot will be too fast
            
            width = int((pyautogui.size()[0]) / 2)
            height = int((pyautogui.size()[1]) / 2) 
            
            pyautogui.moveTo(width,height)
            pyautogui.click()

            time.sleep(self.time_control)

            pyautogui.hotkey('tab')

            time.sleep(self.time_control)

            pyautogui.hotkey('tab')

            time.sleep(self.time_control)

            pyautogui.hotkey('tab')

            time.sleep(self.time_control)

            pyautogui.hotkey('tab')
            
            time.sleep(self.time_control)

            pyautogui.hotkey('tab')
            
            time.sleep(self.time_control)

            pyautogui.hotkey('enter')

            time.sleep(self.time_control)

            pyautogui.hotkey('tab')

            time.sleep(self.time_control)

            pyautogui.hotkey('tab')

            time.sleep(self.time_control)

            pyautogui.hotkey('tab')

            time.sleep(self.time_control)

            pyautogui.hotkey('tab')

            time.sleep(self.time_control)

            pyautogui.typewrite(str(self.idx))

            pyautogui.hotkey('enter')
            
            time.sleep(self.time_control)
            
            pyautogui.moveTo(width,height)
            pyautogui.click()

            pyautogui.hotkey('enter')

            time.sleep(self.time_control)

            time.sleep(2)

            pyautogui.hotkey('right')
            
            time.sleep(self.time_control)
            
            pyautogui.write(str(self.idx))
            
            time.sleep(self.time_control)
            
            pyautogui.hotkey('enter')
                 
            self.idx += 1
        
        self.browser.close()

        
        
    
    def runWebScrapping(self): # function

        print("Executing Web Scrapping")
        
#        self.prepareEnvironment()
        
        self.browser = webdriver.Chrome(executable_path = self.chrome_driver_path, options= self.browser_options) 
        self.browser.maximize_window()
        
        self.browser.get('https://dje.tjsp.jus.br/cdje/index.do;jsessionid=904E03097EDCF133765EE6CB860DFD6B.cdje2') # WARNING: TRANSFORM IN GLOBAL VARIABLE
        
        time.sleep(5)
        
        select_cadastro = Select(self.browser.find_element_by_id('cadernos'))
        select_cadastro.select_by_value("2") # 2 = caderno 3 - Judicial - 1ª Instância - Capital / # cadernosCad

        time.sleep(3)
        
        elem_consulta = self.browser.find_element_by_id('consultar') # download for full download (website not working properly)
        elem_consulta.click()
        
        time.sleep(5)

        width = int((pyautogui.size()[0]) / 2)
        height = int((pyautogui.size()[1]) / 2) 
                        
        pyautogui.moveTo(width,height)
            
        time.sleep(3)
            
        pyautogui.click()
            
        time.sleep(3)
            
        pyautogui.hotkey('enter')
            
        time.sleep(3)
            
        pyautogui.hotkey('enter')
     
        time.sleep(2)
        
        self.downloadFiles()
    

