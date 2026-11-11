dictionary={
    "sana":20,
    "fatima" :50,
    "me": 5999
}

print(type(dictionary))# this gaves us the dict>

# method and simple way to access the dict

print(dictionary["sana"])
#           or 
print(dictionary.get("fatima")) #work same 
# if wrong gave NOne
print(dictionary.get("fatimaa" , 0 )) 









    #Adding and removing methods 
dictionary={
    "sana":20,
    "fatima" :50,
    "me": 5999,
    "sanaullah":1111
}

#updating in the dict
dictionary["me"]=40
print(dictionary)
#Add 
dictionary["gender"]= "male"
print(dictionary)
#update using
dictionary.update({"arif":23923 , 'hussanin': 2343})
print(dictionary)



new_dict={'sana': 20, 'fatima': 50, 'me': 40, 'sanaullah': 1111, 'gender': 'male'}
#removing 
new_dict.pop("sana") # 1st method to remove the key and value 
print(new_dict)
# new_dict.clear()  empty krdega dictionary ko 
# del new_dict delete the whole variable 


