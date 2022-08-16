# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 16:44:25 2022

@author: Ogabek
"""


                 #PYTHON DARSLARI
                 #35-DARS
                 #FUNKSIYANI TEKSHIRISH

#def get_full_name(ism,familiya):
#    return f"{ism} {familiya}".title()

#print(get_full_name("ali", "valiyev"))


#UNITTEST
#TEST CASE

def get_full_name(ism,familiya,otasi=''):
    if otasi:
         return f"{ism} {otasi} {familiya}".title()
    else:
         return f"{ism} {familiya}".title()