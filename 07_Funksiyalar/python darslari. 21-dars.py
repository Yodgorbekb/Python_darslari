# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 17:17:58 2022

@author: Ogabek
"""

                            #PYTHON DARSLARI
                            #21-DARS
                            #FUNKSIYA VA RO'YXAT

#def bahola(ismlar):
#    baholar = {}
#    while ismlar:
#        ism = ismlar.pop()
#        baho = input(f"Talaba {ism.title()}ning bahosini kiritng: ")
#        baholar[ism]=int(baho)
#    return baholar

#talabalar = ['ali','vali','hasan','husan']
#baholar = bahola(talabalar[:])
#print(baholar)

#                              AMALIYOT
#def matnl(matnlar):
#    for n in range(len(matnlar)):
#        matnlar[n]=ismlar[n].title()
        
#ismlar = ['ali','vali','hasan','husan']
#matnl(ismlar)
#print(ismlar)
        
   
#def matnl(matnlar):
#    matnlar = matnlar[:]
#    for n in range(len(matnlar)):
#        matnlar[n]=matnlar[n].title()
#    return matnlar    
#ismlar = ['ali','vali','hasan','husan']
#yangi_ismlar = matnl(ismlar)
#print(ismlar)
#print(yangi_ismlar)

talabalar = ['ali','vali','hasan','husan']
def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
#    while ismlar:
     #   ism = talabalar.title() #ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiritng: ")
        baholar[ism]=baho
    return baholar

baholar = bahola(talabalar)
print(baholar)
print(talabalar)