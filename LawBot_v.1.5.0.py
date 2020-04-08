# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:46:01 2020

@title: Webscrapping from Oficial News from Justice Court of São Paulo
@author: Leonardo Pedroso dos Santos - CTO

"""

import sys
import os
import time
import pyautogui
import pandas as pd
from datetime import date
import WebScrapping
import FileManagement
import WebSearch

# Dependencies: Selenium / Pyautogui / Google Chrome / Adobe Reader DC / unidecoder / Pandas
# Adobe Reader DC: Must be configured before start. 
   
if __name__ == "__main__":
    
    df = [] # Main dataframe
    df_companies = []
    df_contacts = []
    output_path = os.path.dirname(os.path.abspath(__file__))

    try:
        print("Setting up the environment")
        controller = WebScrapping.Browser()
        controller.runWebScrapping()

        time.sleep(5) # 5s for system stability raises

        print("Starting data manager")
        datamanager = FileManagement.FileManagement()
        datamanager.convertToTXT()
        
#        controller.cleanEnvironment() # clean files processed
        
        datamanager.loadFiles()
        df, df_companies = datamanager.createDataFrame()
                
        time.sleep(5) # 5s for system stability raises
        
        web = WebSearch.WebSearch(df_companies)
        df_contacts = web.searchWebSource()

        print('Saving data to excel')
        
        pd.DataFrame(df_contacts).to_excel(output_path + '\Processed_'+str(date.today())+'.xlsx',header=False, index=False)
        
        print('Process executed successfully')

    except:
            pyautogui.keyUp('alt') # Secure to release all keys pressed
            controller.browser.close()
            print(sys.exc_info()[0]) # Retrieve the error
            sys.exit() # Abort mission!           
    

