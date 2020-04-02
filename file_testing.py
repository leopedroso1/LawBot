# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:25:09 2020

@title: Webscrapping from Oficial News from Justice Court of São Paulo
@author: Leonardo Pedroso dos Santos - CTO

@comments: Module OK - 2020-04-02

"""



# Later: add try catch
#try:

file_reader = open(r"C:\Users\Leonardo\Documents\diario_v3.txt",'rt') # TO DO: append txt files

full_text = []  
processos = []
idx = 0

# Later: transform in a function
for myline in file_reader: # OK
 
    full_text.append(myline) # OK

# Later: transform in a function
while idx < len(full_text):

    if idx + 2 >= len(full_text): # Treating end of file exception. Control end of loop 
        break
    
    if full_text[idx].find('PROCESSO') == 0:
        
        if full_text[idx + 4].find('VARA') == 0:            

            processos.append([
                
                full_text[idx], 
                full_text[idx + 1],
                full_text[idx + 2],
                full_text[idx + 3],
                full_text[idx + 4],
                "",
                "",

                ])            
            
            
        if full_text[idx + 5].find('VARA') == 0:

            processos.append([
                
                full_text[idx], 
                full_text[idx + 1],
                full_text[idx + 2],
                full_text[idx + 3],
                full_text[idx + 4],
                full_text[idx + 5],                
                ""

                ])            

            
        if full_text[idx + 6].find('VARA') == 0:
            
            processos.append([
                
                full_text[idx], 
                full_text[idx + 1],
                full_text[idx + 2],
                full_text[idx + 3],
                full_text[idx + 4],
                full_text[idx + 5],                
                full_text[idx + 6]

                ])            
        

    idx += 1
    
file_reader.close()    

#        
#        processos.append([full_text[idx], idx, "teste"])
#        
#        print(idx)
#        print(idx + 5)
#        print(full_text[idx + 5])
        
#        if full_text[idx + 5].find('PROCESSO') == 0:
#        
#            print(idx + 5)
#            print(full_text[idx + 5])
#
#        elif full_text[idx + 4].find('PROCESSO') == 0:
#
#            print(idx + 4)
#            print(full_text[idx + 4])             
#
#        else:
#            print(idx + 6)
#            print(full_text[idx + 6])
                    
    
# SOLUÇÃO COM UM 'FOR'    
#for idx in full_text: # Se for USUCAPIAO pegue + 3 se não pegue + 4 para montar o data frame
#   
#    if idx.find('PROCESSO') == 0:
#               
#        processos.append(idx.strip())
#      
#    if idx.find('CLASSE') == 0:
#       
#        classes.append(idx)
#
#    if idx.find('REQDO') == 0 or idx.find('EMBARGDO') == 0 or idx.find('EXECTDO') == 0 :
#       
#        reqdo.append(idx)
#
#    if idx.find('VARA') == 0:
#       
#        vara.append(idx)
#




#
#
#       if full_text[idx + 4].find('VARA') == 0:            
#
#            idx_inserted_1 = idx + 1
#            idx_inserted_2 = idx + 2
#            idx_inserted_3 = idx + 3
#            idx_inserted_4 = idx + 4
#            idx_inserted_5 = 0
#            idx_inserted_6 = 0
#
#            
#        if full_text[idx + 5].find('VARA') == 0:
#            
#            idx_inserted_1 = idx + 1
#            idx_inserted_2 = idx + 2
#            idx_inserted_3 = idx + 3
#            idx_inserted_4 = idx + 4
#            idx_inserted_5 = idx + 5
#            idx_inserted_6 = 0
#
#            
#        if full_text[idx + 6].find('VARA') == 0:
#            
#            idx_inserted_1 = idx + 1
#            idx_inserted_2 = idx + 2
#            idx_inserted_3 = idx + 3
#            idx_inserted_4 = idx + 4
#            idx_inserted_5 = idx + 5
#            idx_inserted_6 = idx + 6
#            
#        processos.append([
#                
#                full_text[idx], 
#                full_text[idx_inserted_1],
#                full_text[idx_inserted_2],
#                full_text[idx_inserted_3],
#                full_text[idx_inserted_4],
#                full_text[idx_inserted_5],
#                full_text[idx_inserted_6],
#                         
#                ])
