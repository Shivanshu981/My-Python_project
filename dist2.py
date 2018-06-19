# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 02:54:41 2018

@author: Shivanshu
"""
"""
user_input=int(input("Value"))
ages = {"Dave":user_input,"Mary":42,"John":58}

print(ages["Dave"])
"""
"""
user_input2=str(input("Key"))
user_input3=int(input("Value"))
ages2={user_input2:user_input3}

print(ages2[user_input2])
"""

"""
dist=str(input("Name"))
user_input2=str(input("Key"))
user_input3=int(input("Value"))
dist={user_input2:user_input3}

print(dist[user_input2])
"""

while True:
    print("Press 1 to enter the value\n Press 2 to append")
    user_input=str(input("Enter your choice- "))
    if user_input=="1":
       dist=str(input("Distonary Name:- "))
       d=dist;
       key=str(input("Key- "))
       value=str(input("Value- "))
       dist={key:value}
       print(d)
    elif user_input=="2":
        key=str(input("Key- "))
        value=str(input("Value- "))
        dist[key]=value
        
    elif user_input=="3":
         print("db.insert."+str(d)+str(dist))
    elif user_input=="q":
        break
        
        
    
    
    
