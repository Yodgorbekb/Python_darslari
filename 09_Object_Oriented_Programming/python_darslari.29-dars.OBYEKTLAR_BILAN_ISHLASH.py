# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:29:57 2022

@author: Ogabek
"""

                               #PYTHON DARSLARI
                               #29-DARS
                               #OBYEKTLAR BILAN ISHLASH

class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        
        
        
    def get_name(self):
        """Talabaning ismini qytardi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def set_bosqich(self,yangi_bosqich):
        """Talabani kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich
        
    def update_bosqich(self):
        """Talabani bosqichi ni 1taga ko'paytiradi"""
        self.bosqich += 1
        
#    def old(self):
#        """Talabani bosqichi ni 1taga ko'paytiradi"""
#        self.bosqich - 1
    
    def get_age(self,yil):
        return yil - self.tyil
        
        
#    def get_info(self):
#        return f"Ismi: {self.ism}, familiyasi: {self.familiya},   {self.bosqich}-bosqich talabasi"
       
 #    def fullname(self):
 #        return f"{self.ism} {self.familiya},"

class Fan():
    """Fan nomli klass"""
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self,talaba):
        """Fanga talabalar qo'shadi"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
        
    def get_students(self):
        """Fanga yozilgan talabalar"""
        return [talaba.get_name() for talaba in self.talabalar]
    
    def see_methods(klass): 
        return [method for method in dir(klass) if method.startswith('__') is False]



matematika = Fan("Oliy matematika")
talaba1 = Talaba("Olim","Olimov",2000)
talaba2 = Talaba("Husan","Hasanov",1995)
talaba3 = Talaba("Akrom","Alimov",2003)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)


                             #AMALIYOT

class Avto():
    """Avto klassi"""
    def __init__(self,modeli,rang,korobka,narh,yil,km):
        """Avto haqidagi ma'luumotlar"""
        self.modeli = modeli
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.yil = yil
        self.km = 0
#        self.avtolar = []
        
    def get_make(self):
        return self.modeli
    
    def get_color(self):
        return self.rang
    
    def get_box(self):
        return self.korobka
    
    def get_narh(self):
        return self.narh
    
    def get_yil(self):
        return self.narh
    
    def get_km(self):
        return self.km
    
    def get_info(self):
        return f"Avtomabil modeli: {self.modeli}, rangi: {self.rang}, korobkasi: {self.korobka}, narhi: {self.narh}ming dollar, ishlab chiqarilgan yili: {self.yil}, kilometri: {self.km}"
    
    def update_km(self):
#        self.avtolar.append(Avto)
        self.km += 100
        
    def reduce_km(self):
        self.km -= 100
    
    
class Avtosalon():
    """Avtosalon tuzuvchi klass"""
    def __init__(self,salon_nomi,manzili,sotuvdagi_avtomobillar):
        """Avtosalon haqidagi ma'lumotlar"""
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.sotuvdagi_avtomobillar = sotuvdagi_avtomobillar
        self.avtolar = []
        self.avto_son = 0
        
    def avto_kirit(self,salon_nomi):
        self.salon_nomi
    
    def avto_manzil(self):
        return self.manzili
    
    def avto_sotuv(self,sotuvdagi_avtomobillar):
        return self.sotuvdagi_avtomobillar
    
    def avto_qosh(self,avto):
        self.avtolar.append(avto)
        self.avto_son += 1
    
    def get_avto(avto):
        return [avto.get_make() for avto in self.avtolar]
    
    def see_methods(klass): 
        return [method for method in dir(klass) if method.startswith('__') is False]
    
    
salon = Avtosalon("chevrolet","chevrolet@.com","damas")
damas = Avto("Damas","Oq","Mexanik",8500,2006,3000)
salon.avto_kirit(damas)