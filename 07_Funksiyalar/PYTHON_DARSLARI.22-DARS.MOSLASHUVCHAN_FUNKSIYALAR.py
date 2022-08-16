# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 18:34:35 2022

@author: Ogabek
"""

                              #PYTHON DARSLARI
                              #22-DARS
                              #MOSLASHUVCHAN FUNKSIYALAR
                                     #*args VA **kwargs

#def avto_info(komponiya, model, rangi,korobka,yili,narhi=None):
#    avto = {'komponiya':komponiya,
#            'model':model,
#            'rangi':rangi,
#            'korobka':korobka,
#            'yil':yili,
#            'narhi':narhi}
#    return avto

#avto1 = avto_info('GM','malibu','qora','avtomat',2018)
#avto2 = avto_info("GM",'Gentra','oq','mexanik',2016,15000)
#avtolar = [avto1,avto2]
#print(avtolar)



def oraliq(min,max):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar
print(oraliq(0,10))
#print(oraliq(10,21))

                               #*args - usuli

#def summa(*sonlar):
#    """Kiritilgan sonlar yig'indisini hisoblaydiga funksiya"""
#    yigindi = 0
#    for son in sonlar:
#        yigindi += son
#    return yigindi

#print(summa(1,2))
#print(summa(1,2,3,4,5))
#print(summa(1,2,3,4,5,6,7,8,9,0,9,))


#def summa(*sonlar):
#    """Kiritilgan sonlar yig'indisini hisoblaydiga funksiya"""
#    return sum(sonlar)

#print(summa(1,2))
#print(summa(1,2,3,4,5))
#print(summa(1,2,3,4,5,6,7,8,9,0,9,))


#def summa(x,y,*sonlar):
#    """Kiritilgan sonlar yig'indisini hisoblaydiga funksiya"""
#    return x+y+sum(sonlar)

#print(summa(1,23))
#print(summa(1,2,3,4,5))
#print(summa(1,2,3,4,5,6,7,8,9,0,9,))


                               #**kwargs- keywords arguments

#def avto_info(komponiya,model,**malumotlar):
#    """Avto haqidagi ma'lumotlarni ko'rinishida qaytaradigan funksiya"""
#    malumotlar['komponiya']=komponiya
#    malumotlar['model']=model
#    return malumotlar

#avto1 = avto_info("GM",'Malibu',rangi='qora')
#avto2 = avto_info('KIA','K5',rangi='qizil',yili=2018,narhi='35000')
#print(avto1,avto2)


#                            AMALIYOT

#def kopaytir(*sonlar):
#    """Istalgancha son qabul qilib ularning ko'paytmasini qaytaradigan funksiya"""
#    kopaytma = 1
#    for son in sonlar:
#        kopaytma *= son
#    return kopaytma

#print(kopaytir(16,2))



#def malumot(ism,familiya,**malumotlar):
#    """Talabalar haqidagi ma'lumotlarni lug'at ko'rinishida qaytaradigan funksiya"""
#    malumotlar['ism']=ism
#    malumotlar['familiya']=familiya
    
#    return malumotlar

#print(malumot('Yodgorbek','Boltaev',yosh=14,t_yil=2008))

