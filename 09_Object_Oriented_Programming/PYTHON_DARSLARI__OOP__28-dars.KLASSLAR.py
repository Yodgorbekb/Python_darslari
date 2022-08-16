# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:10:43 2022

@author: Ogabek
"""
                              #PYTHON DARSLARI
                              #28-DARS
                              #KLASSLAR


class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
    def get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def get_age(self,yil):
        return yil - self.tyil
        
        
    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya}, tug'ilgan yilim {self.tyil}"
       
talaba1 = Talaba("Olim","Olimov",2000)
talaba2 = Talaba("Husan","Hasanov",1995)
talaba3 = Talaba("Akrom","Alimov",2003)

                                   #AMALIYOT

class User:
    def __init__(self,ism,foydalanuvchi_ismi,email):
       self.ism = ism
       self.foydalanuvchi_ismi = foydalanuvchi_ismi
       self.email = email
       
    def name(self):
        return self.ism
    
    def lastname(self):
        return self.foydalanuvchi_ismi
    
    def get_ago(self):
        pass
    
    def gmail(self):
        return self.email
    
    def get_info(self):
        return f'Foydalanuvchi: {self.foydalanuvchi_ismi}, ismi {self.ism}, elektron manzili {self.email}'
        

user1 = User("Alijon","Ali","alijon1994@gmail.com")
