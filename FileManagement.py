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

class FileManagement:

    
    def __init__(self): 

        self.full_text = []  
        self.processos = []
        self.idx = 0
        
    def loadFile(self):
        
        file_reader = open(r"C:\Users\Leonardo\Documents\diario_v3.txt",'rt') # TO DO: append txt files
        
        for myline in file_reader:
 
            self.full_text.append(myline)
        
        self.file_reader.close()
    
    def createDataFrame(self): # function

        # Later: transform in a function
        while self.idx < len(self.full_text):

            if self.idx + 2 >= len(self.full_text): # Treating end of file exception. Control end of loop 
                break
    
            if self.full_text[self.idx].find('PROCESSO') == 0:
        
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
    
                       

        

