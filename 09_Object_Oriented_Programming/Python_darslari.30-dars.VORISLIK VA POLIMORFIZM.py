# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 12:46:32 2022

@author: Ogabek
"""

                   #PYTHON DARSLARI
                   #30-DARS
                   #VORISLIK VA POLIMORFIZM

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
    
    
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,id_nomer,manzil):
        """Talabani xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.id_nomer = id_nomer
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        self.dars = 0
        
    def get_id(self):
        """Talabani ID raqami"""
        return self.id_nomer
    
    def get_bosqich(self):
        """Talaba bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """kwkrfkmqwfw"""
        info = f"{self.ism}  {self.familiya}. "
        info += f"{self.bosqich()}-bosqich.  ID raqami  {self.get_id()} "
        
        
class Fan:
    """Talabaning fanlari"""
    def __init__(self,matem,kimyo,fizika):
        """Fanlar"""
#        super().__init__(Talaba)
        self.matem = matem
        self.kimyo = kimyo
        self.fizika = fizika
    
        
    def get_matem(self):
        return self.matem
    
    def get_kimyo(self):
        return self.kimyo
    
    def get_fizik(self):
        return self.fizika
    
    
#    def fanga_yozil(Fan):
#        self.fanlar.append(Fan)
#        self.dars += 1
        
#    def remove_fan():
#        self.dars - 1
        
class Manzil:
    """Manzilini xususiyatlari"""
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
        
    def get_manzil(self):
        """Manzilni kirish"""
        manzil = f"{self.viloyat} viloyati,  {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi,  {self.uy}  uy"
        return manzil
 

talaba1_manzil = Manzil(12,"Olmazor","Bog'bon","Samarqand")
talaba1 = Talaba("Valijon","Aliyev","FKQWERTY123",1999,"NUMBER345",talaba1_manzil)




