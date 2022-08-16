# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:17:01 2022

@author: Ogabek
"""

                     #PYTHON DARSLARI
                     #37-DARS
                     #KLASSNI TEKSHIRISH unittest MODULI

class Car:
    """(self,make,model,year,km=0,price=None)"""
    def __init__(self,make,model,year,km=0,price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km
        
    def set_price(self,price):
        self.price = price
        price
    def add_km(self,km):
        """Km ga yana km qo'shadi"""
        if km>0:
            self.__km += km
        else:
            raise ValueError("Kilometr manfiy bo'lishi mumkun emas")
            
    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()}, "
        info += f"{self.year}-yil, {self.__km} km yurgan."
        if self.price:
            info += f" Narhi: {self.price}"
        return info
    
    def get_km(self):
        return self.__km
    
