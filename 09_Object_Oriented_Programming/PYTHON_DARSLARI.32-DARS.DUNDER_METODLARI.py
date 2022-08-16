# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 16:36:00 2022

@author: Ogabek
"""

                     #PYTHON DARSLARI
                     #32-DARS
                     #DUNDER METODLAR

#class Avto:
#    """Avtomobil klassi"""
#    __num_avto = 0
#    def __init__(self,make,model,rang,yil,narh):
#        """Avto xususiyatlari"""
#        self.make = make
#        self.model = model
#        self.rang = rang
#        self.yil = yil
#        self.narh = narh
#        Avto.__num_avto += 1
        
#    def __repr__(self):
#        return f"Komponiyasi: {self.make}, Modeli: {self.model}, Rangi: {self.rang}, Narhi: {self.narh} dollar. "
        
#    def __eq__(self,y):
#        return self.narh==y.narh
    
#    def __lt__(self,y):
#        return self.narh<y.narh
#    
#    def __le__(self,y):
#        return self.narh<=y.narh
    
        



#class Avtosalon:
#    """AvtoSalon klassi"""
#    def __init__(self,name):
#        self.name = name
#        self.avtolar = []
        
#    def __repr__(self):
#        return f"{self.name} avtosaloni"
#    
#    def getitem(self,index):
#        return self.avtolar[index]
    
    
 #   def add_avto(self,*qiymat):
 #       for avto in qiymat:
#            if isinstance(avto,Avto):
#                self.avtolar.append(avto)
#            else:
#                print("Avto kiriting:")
                
#    def __len__(self):
#        return len(self.avtolar)
#                
#    def setitem(self,index,value):
#        if isinstance(value,Avto):
#           self.avtolar[index]=value
           
#    def __add__(self,qiymat):
#        if isinstance(qiymat,Avtosalon):
#            yangi_salon = Avtosalon(f"{self.name} {qiymat.name}")
#            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            
    

#salon1 = Avtosalon("MaxAvto")

#avto1 = Avto("GM","Malibu","Qora",2020,40000)
#avto2 = Avto("GM","Lacetti","Oq",2020,20000)
#avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
#avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
#avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
#avto6 = Avto("Honda","Accord","Oq",2017,42000)
#salon1.add_avto(avto1,avto2,avto3,avto4,avto5,avto6)



                       #AMALIYOT

class Shaxs:
    """Shaxs yaratuvchi klass"""
    def __init__(self,ism,familiya,passport,tyil):
        """shaxs xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def __repr__(self):
        return f"{self.ism}  {self.familiya}. "
        f"Passport: {self.passport},  {self.tyil}-yilda tug'ilgan"
    
    def get_age(self,yil):
        """Talaba yoshi"""
        return yil - self.tyil
    
    
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,id_nomer):
        """Talabani xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.id_nomer = id_nomer
        self.bosqich = 1
#        self.manzil = manzil
        self.fanlar = []
        self.dars = 0
        
    def get_id(self):
        """Talabani ID raqami"""
        return self.id_nomer
    
    def get_bosqich(self):
        """Talaba bosqichi"""
        return self.bosqich
    
    def __lt__(self,y):
        return self.bosqich<y.bosqich
    
    def __eq__(self,y):
        return self.bosqich==y.bosqich
    
    def add_bosqich(self):
        self.bosqich += 1
        
    
    def get_info(self):
        """kwkrfkmqwfw"""
        info = f"{self.ism}  {self.familiya}. "
        info += f"{self.bosqich}-bosqich.  ID raqami  {self.get_id()} "
        
        
talaba1 = Talaba("Valijon","Aliyev","FKQWERTY123",1999,"NUMBER345")
talaba2 = Talaba("Akmal","Aliyev","FKQ123dTY123",2001,"WJJ12K13K4K")