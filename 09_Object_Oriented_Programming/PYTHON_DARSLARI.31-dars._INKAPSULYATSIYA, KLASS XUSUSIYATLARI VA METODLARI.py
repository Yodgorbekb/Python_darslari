# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 16:13:20 2022

@author: Ogabek
"""

                    #PYTHON DARSLARI
                    #31-DARS
                    #INKAPSULYATSIA, KLASSNING XUSUSIYATLARI VA METODLARI
                    
from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narhi,km=0):
        """Avto xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narhi = narhi
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
        
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        if km>0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")


