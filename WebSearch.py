# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:48:18 2020

@author: Leonardo
"""

import time
import pyautogui
from unidecode import unidecode 
from selenium import webdriver


class WebSearch:
    
    
    def __init__(self):
      
        self.browser = webdriver.Chrome(executable_path = r'C:\Users\Leonardo\Desktop\Oxford\Webscrapping\chromedriver') 
        self.browser.maximize_window()
        self.df = []
              
    def searchWebSource(self):
        
        self.browser.get('https://cnpjs.rocks/') # Change if not available

        idx = 0

        df_teste = []

        time.sleep(3)

        while idx <= len(df):

            try:
                input_text = self.browser.find_element_by_id('search_side')
                input_text.send_keys(df[idx])

                time.sleep(1)

                pyautogui.hotkey('enter')

                time.sleep(5)
            
                select_company = self.browser.find_element_by_tag_name('b')
                select_company.click()
        
                time.sleep(5)
    
                tab_window = self.browser.window_handles[1]
    
                self.browser.switch_to.window(tab_window)
    
                # Testing...remove this later
                width = int((pyautogui.size()[0]) / 2)
                height = int((pyautogui.size()[1]) / 2) 
                                
                pyautogui.moveTo(width,height)
                    
                time.sleep(3)
                    
                pyautogui.click()
                # Remove until the line above
        
                select_telephone = self.browser.find_element_by_xpath('//*[@id="main"]/div[2]/ul[5]/li[1]/strong')
                select_email = self.browser.find_element_by_xpath('//*[@id="main"]/div[2]/ul[5]/li[2]/strong')
                select_ceo = self.browser.find_element_by_xpath('//*[@id="main"]/div[2]/ul[6]/li[1]/strong')
                select_CNPJ = self.browser.find_element_by_xpath('//*[@id="main"]/div[2]/ul[1]/li[1]/strong')
    
    
                df_teste.append(df[idx])
                df_teste.append(select_CNPJ.text)
                df_teste.append(select_ceo.text)
                df_teste.append(select_telephone.text)
                df_teste.append(select_email.text)

                time.sleep(3)
    
                pyautogui.keyDown('ctrl')
                time.sleep(1)
                pyautogui.press('w')
                time.sleep(1)
                pyautogui.keyUp('ctrl')
            
                browser.switch_to.window(root_window)

                idx += 1

            except:
        
                print('Empresa não encontrada')
        
                idx += 1
        self.browser.close()







    
    
    def searchGoogle(self):
        
        print("OK")