# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 07:54:27 2022

@author: Ogabek
"""

                                 #PYTHON DARSLARI
                                 #24-DARS
                                 #FUNKSIYALAR. SO'NGISO'Z

#import math

#def nom(argument):
#    return ifoda


#lambda argument1, argument2:ifoda=argument1+argument2

#LAMBDA FUNKSIYASI

#uzunlik= lambda pi, r : 2*pi*r
#print(uzunlik(math.pi,10))

#kvadrat = lambda x, y : x ** y
#print(kvadrat(3, 2))


#def daraja(n):
#    return lambda x : x**n

#kvadrat = daraja(2)
#kub = daraja(3)
#print(f"3-ning kvadrari {kvadrat(3)} ga, "
#      f"kubi {kub(3)} ga teng")

#MAP() FUNKSIYASI

#from math import sqrt

#sonlar = list(range(11))
#ildizlar = list(map(sqrt,sonlar))
#print(ildizlar)


#def daraja2(x):
#    """Berilgan sonning kvadratini qaytaradigan funksiya"""
#    return x*x

#print(list(map(daraja2,sonlar)))

#kvadrat = list(map(lambda x:x*x,sonlar))
#print(kvadrat)

#a = [4, 5, 6]
#b = [7, 8, 9]
#a_plus_b = list(map(lambda x,y:x+y,a,b))
#print(a_plus_b)

#ismlar = ['hasan','husan','olim','umid']
#print(list(map(lambda matn:matn.upper(),ismlar)))


#FILTER() FUNKSIYASI

#import random as r

#sonlar = r.sample(range(100),(10))
#print(sonlar)
#def juftmi(x):
#    """x juft bo'lsa True, aks holda False qiymat qaytaruvchi funksiya"""
#    return x%2==0

#juft_sonlar = list(filter(juftmi,sonlar))
#print(juft_sonlar)

#juft_sonlar = list(filter(lambda x: x%2==0,sonlar))
#print(juft_sonlar)


#startswith METODI

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
harf = "o"
mevalar_b = list(filter(lambda meva:meva.startswith(harf),mevalar))
print(mevalar_b)
 

mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)

list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))



#product = lambda x, y : x ** y
#print(product(3, 2))

