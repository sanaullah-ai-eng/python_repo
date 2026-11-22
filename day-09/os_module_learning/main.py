import os 
print(os.getcwd())  # gave us the current working directory 
# os.chdir("C:\\Users")       # folder badlo (cd command jaisa)
print(os.getcwd())

# "C:\\Users\\Ali"      # double backslash
# r"C:\Users\Ali"       # r = raw string (best)
# "C:/Users/Ali"        # forward slash (Windows mein bhi chalta hai)


#Folder bnana and hatana 
import os
os.mkdir("data")