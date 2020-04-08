# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:33:31 2020

@title: Webscrapping from Oficial News from Justice Court of São Paulo
@author: Leonardo Pedroso dos Santos - CTO

"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:59:03 2020

"""


import time
import os
import subprocess
import pyautogui
from unidecode import unidecode 

# Add a Today at data frame

class FileManagement:

    
    def __init__(self): 

        self.full_text = []  
        self.processos = []
        self.prosecution_company = []
        self.idx = 0
        self.adobePath = r"C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
        self.files_path = os.path.expanduser('~\Documents')
        self.time_control = 5
    
    def convertToTXT(self):
        
        print("Converting PDF to txt")
                
        idx_files = 1          
        max_files = 80 # WARNING: Transform to parameter later. Total amount = 80. 10 is only for testing purposes
            
        while idx_files <= max_files:
            
            if idx_files == 1:
                    
                subprocess.Popen("%s %s" % (self.adobePath, self.files_path + '\diario.pdf'))
              
            else:
                    
                subprocess.Popen("%s %s" % (self.adobePath, self.files_path + '\diario'+str(idx_files)+'.pdf'))
                
            time.sleep(self.time_control)

            pyautogui.keyDown('alt')
        
            time.sleep(self.time_control)
        
            pyautogui.press('q')

            time.sleep(self.time_control)

            pyautogui.press('v')

            time.sleep(self.time_control)

            pyautogui.keyUp('alt')
    
            time.sleep(self.time_control)
    
            pyautogui.press('enter')
            
            time.sleep(self.time_control) # Waiting for system stability raises

            pyautogui.keyDown('alt')        
            pyautogui.press('f4')
                
            idx_files += 1
            
            pyautogui.keyUp('alt')
        
        
                
    def loadFiles(self):

        print("Caching files into RAM memory")        
        # Adicionar loop
        
        idx_files = 1
        max_files = 1 # set always to a global 80
        
        while idx_files <= max_files:
           
            if idx_files == 1:
            
                file_reader = open(self.files_path + '\diario_v3.txt','rt') # TO DO: append txt files

            else:
            
                file_reader = open(self.files_path + '\diario' + str(idx_files) + '.txt','rt') # TO DO: append txt files
            
#        file_reader = open(r"C:\Users\Leonardo\Documents\diario_v3.txt",'rt') # TO DO: bind txt files -- REMOVE LATER
        
            # loop for read the data from file
            for myline in file_reader:
                
                self.full_text.append(myline)
                
            file_reader.close()
        
            idx_files += 1
            
    
    def createDataFrame(self): # function

        print("Creating main data frame")        

        # Run over all file searching for useful information
        while self.idx < len(self.full_text):

            if self.idx + 2 >= len(self.full_text): # Treating end of file exception. Control end of loop 
                break
    
            if self.full_text[self.idx].find('PROCESSO') == 0: # If we detect a prosecution build the dataframe using the following information. Each prosecution has its own particularity
        
                if self.full_text[self.idx + 4].find('VARA') == 0:            

                    self.processos.append([
                
                        self.full_text[self.idx], 
                        self.full_text[self.idx + 1],
                        self.full_text[self.idx + 2],
                        self.full_text[self.idx + 3],
                        self.full_text[self.idx + 4],
                        "",
                        "",

                    ])            
            
            
                if self.full_text[self.idx + 5].find('VARA') == 0:

                    self.processos.append([
                
                        self.full_text[self.idx], 
                        self.full_text[self.idx + 1],
                        self.full_text[self.idx + 2],
                        self.full_text[self.idx + 3],
                        self.full_text[self.idx + 4],
                        self.full_text[self.idx + 5],                
                        ""

                    ])            

            
                if self.full_text[self.idx + 6].find('VARA') == 0:
            
                    self.processos.append([
                
                    self.full_text[self.idx], 
                    self.full_text[self.idx + 1],
                    self.full_text[self.idx + 2],
                    self.full_text[self.idx + 3],
                    self.full_text[self.idx + 4],
                    self.full_text[self.idx + 5],                
                    self.full_text[self.idx + 6]

                    ])

            self.idx += 1

        print("Creating companies data frame")        
            
        self.idx = 0
        
        # Create a dataframe with companies only. We can improve the efficiency later by using just one function given CEO feedback
        # TEST: May be will be necessary additional control here
        while self.idx < len(self.full_text):

            if self.idx + 2 >= len(self.full_text):  
                break
    
            if self.full_text[self.idx].find('PROCESSO') == 0: # If we detect a prosecution build the dataframe using the following information. Each prosecution has its own particularity
                
                process_class = unidecode(self.full_text[self.idx + 1])
        
                if process_class[8:].find('USUCAPIAO') == 0:
                    
                    self.prosecution_company.append([
                
                    self.full_text[self.idx], 
                    ""
                        
                    ])
    
                elif self.full_text[self.idx + 4].find('VARA') == 0:
                
                    self.prosecution_company.append([
                
                        self.full_text[self.idx], 
                        (self.full_text[self.idx + 3])
                        
                        ])

                elif self.full_text[self.idx + 5].find('VARA') == 0:
                
                    self.prosecution_company.append([
                
                        self.full_text[self.idx], 
                        (self.full_text[self.idx + 4])
                        
                        ])            
            
                elif self.full_text[self.idx + 6].find('VARA') == 0:
                
                    self.prosecution_company.append([
                
                        self.full_text[self.idx], 
                        (self.full_text[self.idx + 4])
                        
                        ])            
    
            self.idx += 1
                        

        return self.full_text, self.prosecution_company
    
    
    


        

#                if self.full_text[self.idx + 4].find('VARA') == 0:            
#
#                    self.prosecution_company.append([
#                
#                        self.full_text[self.idx], 
#                        self.full_text[self.idx + 3]
#                        
#                    ])            
#            
#            
#                if self.full_text[self.idx + 5].find('VARA') == 0:
#
#                    self.prosecution_company.append([
#                
#                        self.full_text[self.idx], 
#                        self.full_text[self.idx + 4]
#
#                    ])            
#
#            
#                if self.full_text[self.idx + 6].find('VARA') == 0:
#            
#                    self.prosecution_company.append([
#                
#                    self.full_text[self.idx], 
#                    self.full_text[self.idx + 4]
#                    
#                    ])
