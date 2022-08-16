# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 17:10:39 2022

@author: Ogabek
"""

                                    #PYTHON DARSLARI
                                    #20-DARS
                                    #QYMAT QAYTARUVCHI FUNKSIYA
#def toliq_ism_yasa(ism, familiya):
#    """To'liq ism yasovchi funksiya"""
#    toliq_ism = f"{ism} {familiya}"
#    print(toliq_ism)
    
#toliq_ism_yasa('olim','olimov')


#MAHALLIY O'ZGARUVCHI YOKI ICHKI O'ZGARUVCHI
#              LOCAL VARIABLE
#  return kalit so'zi

#def toliq_ism_yasa(ism, familiya):
#    """To'liq ism yasovchi funksiya"""
#    toliq_ism = f"{ism} {familiya}"
#    return toliq_ism
    
#talaba = toliq_ism_yasa("olim","hakimov")


#def toliq_ism_yasa(ism, familiya):
#    """To'liq ism yasovchi funksiya"""
#    toliq_ism = f"{ism} {familiya}"
#    return toliq_ism
#    
#talaba1 = toliq_ism_yasa("olim","hakimov")
#talaba2 = toliq_ism_yasa("ali","hakimov")
#print(f"Darsga kelmagan talabalar {talaba1} va {talaba2}")



#          IXTIYORIY ARGUMAENT
#def toliq_ism_yasa(ism,familiya,otasining_ismi=''):
#    """Toliq_ism_qaytaruvchi_familiya"""
#    if otasining_ismi:
#        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#    else:
#        toliq_ism = f"{ism} {familiya}"
#    return toliq_ism.title()

  
#talaba1 = toliq_ism_yasa('olim','olimov')
#talaba2 = toliq_ism_yasa('vali','hakimovich')
#print(f"Darsga kelmagan talabalar {talaba1} va {talaba2}")



#           LUG'AT QYTARISH
#def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
#    avto = {'kompaniya':kompaniya,
#            'model':model,
#            'rangi':rangi,
#            'korobka':korobka,
#            'yili':yili,
#            'narh':narhi}
#    return avto

#avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
#avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
#avtolar = [avto1, avto2]



#print("Onlayn bozoridagi mavjud avtomabillar:")
#for avto in avtolar:
#   if avto['narh']:
#       narh = avto['narh']
#   else:
#       narh = "Nom'alum"
#   print(f"{avto['rangi']} {avto['model']}. Narhi: {narh}")

    
#           RO'YHAT QAYTARISH
#def oraliq(min,max):
#    sonlar = []
#    while min<max:
#        sonlar.append(min)
#        min += 1
#    return sonlar

#print(oraliq(0,10))

    
#          FUNKSIYA VA TSIKL

def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rangi':rangi,
            'korobka':korobka,
            'yili':yili,
            'narh':narhi}
    return avto

print("Saytimizdagi avtolar ro'yhati")
avtolar = []
while True:
    print("\nQuyidagi ma'lumotlarni kiriting:" ,end= '')
    kompaniya = input("Ishlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Yili: ")
    narhi = input("Narhi: ")


    avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narhi))

    javob = input("Yana avto qo'shasizmi?  (yes/no): ")
    if javob == 'no':
        break

print("\nSalonimizdagi avtolar:")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "No'malum"
    print(f"{avto['rangi'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}$$dollar")
    
    
#                      AMALIY MASHG'ULOT

#def shahs_malumot(ism,familiya,t_yil,yosh,t_joy,email='',tel_raqami=None):
#    malumot = {'ism':ism,
#               'familiya':familiya,
#               't_yil':t_yil,
#               'yosh':2022-t_yil,
#               't_joy':t_joy,
#               'email':email,
#               'tel_raqami':tel_raqami}
#    return malumot 

#print("SHahs haqidagi ma'lumotlarni kiriting.")
#shahslar = []
#while True:
#    ism = input("Ismingiz nima?: ")
#    familiya = input("Familiyangiz nima?: ")
#    t_yil = int(input("Tug'ilgan yiligingizni kiriting: "))
#    t_joy = input("Tug'ilgan joyingizni kiriting: ")
#    email = input("Email manzilingizni kiriting: ")
#    tel_raqami = input("Telefon raqamingizni kiriting: ")
#

#    shahslar.append(shahs_malumot(ism,familiya,t_yil,t_joy,email,tel_raqami))
#    javob = input("Yana shahs qo'shasizmi?  (yes/no)")
#    if javob=='no':
#        break
#    
#print("shahslar:")
#for shahs in shahslar:
#       print(f"{shahs['ism'].title()} {shahs['familiya'].title()}, "
#             f"{shahs['yosh']} yoshda, telefon raqami{shahs['tel_raqami']}")
    


#def son(x,y,z):
   # """Foydalanuvchidan uchta son qabul qilib
    #ularning eng kattasini konsolga chiqaruvchi
    #funksiya"""
    #max = x
   # if y>=max:
    #    max = y
   # if z>=max:
  #      max = z
 #   return max

#son(12,34,-16)


#def hisobla(radius,pi=3.14159):
#    aylana = {'radius':radius,
#              'diametr':2*radius,
#              'perimetr':2*radius*pi,
#              'yuza':pi*radius**2}
#    return aylana

#son = hisobla(5)
#print(son)



#def tub_sonlar_top(min,max):    
#    tub_sonlar = []    
#    for n in range(min,max+1):
#        tub = True
#        if (n==1):
#            tub = False
#        elif(n==2):
#            tub = True
#       else:
#           for x in range(2,n):
#               if(n%x==0):
#                    tub = False
#       if tub:
#            tub_sonlar.append(n)
                
#    return tub_sonlar
#tub_son = tub_sonlar_top(1,20)
#print(tub_son)









#def toliq_ism(ism,familiya):
#    """Toliq ism qaytaruvchi funksiya"""
#    toliq_ism = f"{ism} {familiya}"
#    return toliq_ism

#talaba1 = toliq_ism('olim','hakimov')
#talaba2 = toliq_ism('hakim','olimov')

#print(f"Darsga kelmagan talabalar {talaba1} va {talaba2}")
