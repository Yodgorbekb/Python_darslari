# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:19:33 2022

@author: Ogabek
"""

class Shaxs:
    """shjfr"""
    def __init__(self,ism,familiya,passport,tyil):
        """shaxs xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """kwkrfkmqwfw"""
        info = f"{self.ism}  {self.familiya}. "
        info += f"Passport: {self.passport},  {self.tyil}-yilda tug'ilgan"
        return info
    
    def get_age(self,yil):
        """Talaba yoshi"""
        return yil - self.tyil