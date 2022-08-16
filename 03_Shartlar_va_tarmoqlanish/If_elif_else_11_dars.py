# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 06:49:09 2022

@author: Ogabek
"""

                               #PYTHON DARSLARI. 11-DARS
                               #MAVZU:IF-ELIF-ELSE. BIR NECHTA
                               #SHARTLARNI TEKSHIRISH
#son = -72
#if son<0:
#    print("Manfiy son")
#else:
#   print("Musbat son")
#   yosh = int(input('Yoshingiz nechada?'))  #YOKI PRINT O'RNIGA>>>>NARX = 4000<<< YOZIB VA OHIRIDA PRINT(F"SIZGA KIRISH {NARX} SO'M") DEYISH MUMKIN!!!
#if yosh<4:
#    print('Sizga kirish bepul.')
#elif yosh<12:
#    print("Sizga kirish 5000 so\'m")
#elif yosh<18:
#    print("sizga kirish 20000 ming so\'m")
#else:
#    print("Sizga kirish 10000 so\'m")
                 #OR OPERATORI
#kun = input("Bugun nima kun?>>")
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#    print('Bugun dam olish kuni')
#else:
#    print('Bugun ish kuni')
                 #AND OPERATORI
#kun = input("Bugun qaysi kun?>>")
#harorat = float(input("Havo harorati qanday?>>"))
#if kun.lower()=='yakshanba' and harorat>=20:
#     print("CHo'milgani ketdik!")
#elif kun.lower()=='yakshanba' and harorat<20:
#     print("Uyda dam olamiz!")      
#kun = input("Bugun nima kun?>>")
#harorat = float(input("Havo harorati qanday?>>"))
#if(kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#    print("CHo'milgani ketdik")
#elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
#    print("Uyda dam olamiz!")    
               #boolean mantiqiy malumotlar turi.
#narh = 15000
#choy = True
#salat = False 

#if choy and salat:
#        narh = narh + 10000
#elif choy or salat:
#      narh = narh + 5000     
#print(f"Jami {narh} so'm")
#narh = 15000
#choy = True   
#salat = False
#non = True   #BU YERDA TRUE O'RNIGA '1' FALSE ORNIGA'0' QO'YSA BO'LADI!!!!
#kompot = False
#tort = True
#if choy:
#     print("Mijoz choy oldi.")
#     narh = narh +3000
#if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
#if non:
#     print("Mijoz non oldi.")
#     narh = narh + 7000
#if kompot:
#     print("Mijoz kompot oldi.")
#if tort:
#     print("Mijoz tort oldi.")
#print(f"Jami {narh} so'm")
                         #IN METODI
#menu = ['osh', 'qozonkabob','shashlik','norin','somsa']
#'manti' in menu #menu da manti bormi
#menu = ['osh','qozonkabob','shashlik','norin','somsa']
#ovqat = input('Nima ovqat yeysiz?>>>')
#if ovqat.lower() in menu:
#      print('Buyurtma qabul qilindi.')
#else:
#      print('Afsuski bizda bunday ovqat yo\'q')
#menu = ['osh','qozonkabob','shashlik','norin','somsa']
#buyurtmalar = ["osh","somsa","manti","shashlik"]
#for taom in buyurtmalar:
#      if taom in menu:
#          print(f"Menuda {taom}  bor")
#      else:
#          print(f"Kechirasiz, menuda {taom} yo'q")
#else:
#    print("Savatchangiz bo'sh!")