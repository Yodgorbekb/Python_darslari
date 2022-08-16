# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 06:37:37 2022

@author: Ogabek
"""

mevalar = ['olma','anjir','shaftoli','o\'rik']#mevalar ro'yxati
narhlar = [12000,18000,10900,22000]#narhlar ro'yxati
sonlar = ['bir','ikki',3,4,5]#sonlar va matnlar ro'yxati
ism = [] #bo'sh ro'yxat

print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])

# # title metodi
print("Birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())

narhlar = [12000, 18000, 10900, 22000]
print(narhlar[2] + narhlar[3])

# # Elementlarni o'zgartirish

narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
print(narhlar)

# # Element qo'shish

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
print(mevalar)

# # insert metodi

cars = ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
print(cars)

# # Elementlarni o'chirish

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
print(mevalar)


# # Elementni sug'urib olish

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)