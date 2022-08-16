"""
Created on Tue Aug  9 16:26:05 2022

PYTHON DARSLARI
38-DARS
PYTHON STANDART KUTUBXONASI
"""

#import datetime as dt


#hozir = dt.datetime.now()
#print(hozir)

#print(hozir.hour)

#print(hozir.minute)

#print(hozir.second)

# # date()
#bugun = dt.date.today()
#print(f"Bugungi sana: {bugun}")
#ertaga = dt.date(2022,3, 10)
#print(f"Ertangi sana: {ertaga}")


# # time()

#hozir = dt.datetime.now()
#vaqtHozir = hozir.time()
#print(f"Hozir soat: {vaqtHozir}")
#vaqtKeyin = dt.time(23,45,30)
#print(vaqtKeyin)


# #Sanalar orasidagi farq
#bugun = dt.date.today()
#ramazon = dt.date(2022, 4, 13)
#farq = ramazon-bugun
#print(farq)
#print(f"Ramazonga {farq.days} kun qoldi")

# #oatlar orasidagi farq
#hozir = dt.datetime.now()
#futbol = dt.datetime(2022, 3, 10, 23, 45, 00)
#farq = futbol-hozir
#sekundlar = farq.seconds
#minutlar = int(sekundlar/60)
#soatlar = int(minutlar/60)
#print(f"Futbol boshlanishiga {farq.days} kunu {soatlar} soatu {minutlar} minut {sekundlar} sekund qoldi")


# #Math moduli
#import math

#PI = math.pi
#print(f"PI ni qiymati: {PI}")
#E = math.e
#print(f"e ni qiymati {E}")


# #Trigonometriya
#math.sin(math.pi/2)
#math.cos(0)
#math.tan(PI)

# # radianlar va burchaklar o'ratsida konvertsiya
#print(math.degrees(math.pi/2))
#print(math.radians(90))


# # logorifmlar
#natural logorifm
#math.log(5)
#10 asosli lagorifm
#math.log10(10)


# #Sonlarni yaxlitlash
#x = 4.6
#print(math.ceil(x))
#print(math.floor(x))


#Kvadrat ildizi
#x = 81
#math.sqrt(x)

# Darajaga oshirish
#math,pow(x,3) # x ni kubi
#math.pow(x,5) # x ni 5-darajasi
#math.pow(x,1/3) # x dan kub ildiz


# pprint moduli
#from pprint import pprint
#import json

#filename = 'bemor.json'
#with open(filename) as f:
#    bemor = json.load(f)
    
#pprint(bemor)

#import requests
#r = requests.get('https://api.github.com')
#pprint(r.json())


# # RegEx moduli
import re
#from uzwords import words

#word1 = "темур"
#word2 = "томир"
#word3 = "тулпор"

#andoza = "т...р$"

#print(re.match(andoza, word1))
#print(re.match(andoza, word2))
#print(re.match(andoza, word3))

#matches = []
#for word in words:
#    if re.match(andoza,word):
#        matches.append(word)

#print(matches)

# #Emailni ajratib olish
matn = """Kurib turganingizdek, natija yil,
       oy, kun soat, minut, sekund va millisekund 
       koʻrinishida hehe@gmail.com chiqdi. Biz bu qiymatlardan istaganimzni 
       maxsus metodlar yordamida ajratib olishimiz mumkin"""

#andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
#email = re.findall(andoza,matn)
#print(email)


# # Kuchli parolni tekshirish
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yngi parol kiriting"
msg += "(Kamida 8 ta belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, "
msg += "1 ta son va 1 ta belgi bo'lsin):"

while True:
    password = input(msg)
    if re.match(andoza,password):
        print("Maxfiy so' qabul qilinadi")
        break
    else:
        print("Maxfiy  so'z kiritilmadi")