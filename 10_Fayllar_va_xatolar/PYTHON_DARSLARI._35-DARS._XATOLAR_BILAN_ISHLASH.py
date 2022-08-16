# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 14:30:31 2022

@author: Ogabek
"""

                    #PYTHON DARSLARI
                    #35-DARS
                    #XATOLAR BILAN ISHLASH
                    
#yosh = input("Yoshing kiriting:")

#try:
#    yosh = int(yosh)
#except ValueError:
#    print("Siz butun son kiritmadingiz")
#else:
#    print(f"Siz {2022-yosh} yilda tug'ilgansiz")
    
    
#print("Dastur davom etyapti")
#print("Dastur tugadi")



#ZeroDivisionError

#x,y=5,10
#try:
#    y/(x-5)
#except ZeroDivisionError:
#    print("0 ga bo'lib bo'lmaydi")



#IndexError

#mevalar = ['olma','anor','anjir','uzum'] 
#try:
#    print(mevalar[4])
#except IndexError:
#    print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")



#KeyError

#user = {"username":"sariqdev",
#        "status":"admin",
#        "phone":"998234755678"}

#key="tel"
#try:
#    print(f"Foydalanuvchi: {user[key]}")
#except KeyError:
#    print("Bunday kalit yo'q")

#print(user["username"])



#FileNotFoundError

#filename = "f.txt"
#try:
#    with open(filename) as f:
#        text = f.read()
#except FileNotFoundError:
#    print(f"{filename} mavjud emas")


#import json
#files = ['talabalar.txt','talaba2.json']
#for filename in files:
#    try:
#        with open(filename) as f:
#            talaba = json.load(f)
#    except FileNotFoundError:
#        print(f"{filename} mavjud emas")
        
        
#import json
#files = ['talabalar.txt','talaba2.json']
#for filename in files:
#    try:
#        with open(filename) as f:
#            talaba = json.load(f)
#    except FileNotFoundError:
#        pass
#    else:
#        print(talaba['ism'])



#Bir nechta except

#n = input("Butun son kiriting: ")
#try:
#    n = int(n)
#    x=20/n
#except ValueError:
#    print("Butun son kiritmadingiz")
#except ZeroDivisionError:
#    print("0 ga bo'lib bo'lmaydi")
#else:
#    print(f"x={x}")



#IF ELSE

#while True:
#    yosh = input("Yoshing kiriting:")
#    if yosh.isdigit():
#        yosh = int(yosh)
#        break
       
#print(f"Siz {2022-yosh} yilda tug'ilgansiz")


   