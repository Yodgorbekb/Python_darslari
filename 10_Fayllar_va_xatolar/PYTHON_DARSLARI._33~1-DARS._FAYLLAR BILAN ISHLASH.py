# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 15:06:24 2022

@author: Ogabek
"""

                        #PYTHON DARSLARI
                        #33-DARS
                        #FAYLLAR BILN ISHLASH

#file = open('pi.txt')
#PI = file.read()
#print(PI)
#file.close()


#WITH OPERATORI

#with open('pi.txt') as file:
#    pi = file.read()
    
    
#print(pi)
    
    
#pi = pi.rstrip()
#pi = pi.replace('\n','')
#pi = pi.float(pi)
#print(pi)


#filename = 'data/talabalar.txt'
#with open(filename) as file:
#    for line in file:
#       print(line)


#with open(filename) as file:
#    talabalar = file.readlines()
    
#print(talabalar)


#talabalar = [talaba.rstrip() for talaba in talabalar]
#print(talabalar)


     #YANGI FAYL OCHISH
    
#faylnomi = 'new_file.txt'
#ism = 'Olimjon Hasanov'
#tyil = 2004
#with open(faylnomi, 'w') as fayl:
#    fayl.write(ism+'\n')
#    fayl.write(str(tyil)+'\n')
    
    
    #FAYLGA YOZISH
    
#faylnomi = 'new_file.txt'

#with open(faylnomi, 'a') as fayl:
#    fayl.write("Alijon Valiyev\n")
#    fayl.write(2000)
    
    
#import pickle

#with open('info','wb') as file:
#    talaba1.pickle.load(file)
#    talaba2.pickle.load(file)
    
#print(talaba1)
#print(talaba2)


                           #AMALIYOT

#import pickle

#with open('pi.txt') as file:
#    pi = file.read()
#pi = pi.rstrip()
#i = pi.replace('\n','')
#pi = pi.replace(' ','')


#bdate = '38765698'
#print(bdate in pi)

#pi = float(pi)

#with open('pi.txt','wb') as file:
#    pickle.dump(pi,file)
    
    


while True:
    book = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    if not book: break
    with open('books.txt','a') as file:
        file.write(book+'\n')