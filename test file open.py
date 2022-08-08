import os

mainfolder ='C:\\Users\\Kyle\\Documents\\College\\11_2022 Spring\\3_nano 22sp\\NASA Cu-CNT\\current density data'
subfolder = '\\03-28-22\\'
    
directory = os.fsencode(mainfolder + subfolder)
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".csv"):
         print(mainfolder+subfolder+filename)
         continue
     else:
         print('skip')
         continue
