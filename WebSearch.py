# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:48:18 2020

@author: Leonardo
"""

import time
import os
import pyautogui
from unidecode import unidecode
from selenium import webdriver


class WebSearch:
    
    
    def __init__(self, dataframe):
      
        self.df = dataframe
              
    def searchWebSource(self):

        idx = 0
        df_final = []
                        
        chrome_driver_path = os.path.dirname(os.path.abspath(__file__)) + '\chromedriver'
        browser = webdriver.Chrome(executable_path = chrome_driver_path) 
        browser.maximize_window()

        browser.get('https://cnpjs.rocks/') # Change if not available

        root_window = browser.window_handles[0] # Chrome window handler        

        time.sleep(3)


        while int(idx) <= len(self.df):
            
            try:
                
                input_text = browser.find_element_by_id('search_side')
                
                company_extract = unidecode(self.df[idx][1])
                
                company = company_extract[:company_extract.find('Ltda')]
                
                print(company[8:])
                
                input_text.send_keys(company[8:])
                
                time.sleep(1)

                pyautogui.hotkey('enter')

                time.sleep(5)
            
                select_company = browser.find_element_by_tag_name('b')
                select_company.click()
        
                time.sleep(5)
    
                tab_window = browser.window_handles[1]
    
                browser.switch_to.window(tab_window)
    
                # Testing...remove this later
                width = int((pyautogui.size()[0]) / 2)
                height = int((pyautogui.size()[1]) / 2) 
                                
                pyautogui.moveTo(width,height)
                    
                time.sleep(3)
                    
                pyautogui.click()
                # Remove until the line above
        
                select_telephone = browser.find_element_by_xpath('//*[@id="main"]/div[2]/ul[5]/li[1]/strong')
                select_email = browser.find_element_by_xpath('//*[@id="main"]/div[2]/ul[5]/li[2]/strong')
                select_ceo = browser.find_element_by_xpath('//*[@id="main"]/div[2]/ul[6]/li[1]/strong')
                select_CNPJ = browser.find_element_by_xpath('//*[@id="main"]/div[2]/ul[1]/li[1]/strong')
    
    
                df_final.append(self.df[idx][0])
                df_final.append(select_CNPJ.text)
                df_final.append(select_ceo.text)
                df_final.append(select_telephone.text)
                df_final.append(select_email.text)

                time.sleep(3)
    
                pyautogui.keyDown('ctrl')
                time.sleep(1)
                pyautogui.press('w')
                time.sleep(1)
                pyautogui.keyUp('ctrl')
            
                browser.switch_to.window(root_window)
                
                idx += 1

            except:
        
                print('Company not found')
                
                idx += 1

        browser.close()        
        return df_final

        
