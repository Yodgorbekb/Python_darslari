# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:48:26 2022

@author: Ogabek
Github Web sahifa https://github.com/yodgorbekb/calculator
"""

import random 

def son_top(x=100):
    tasodifiy_son = random.randint(1,x)
    print(f"1 dan {x} gacha son o'yladim. Topa olasizmi?:")
    taxminlar = 0      
    while  True:
        taxminlar += 1
        taxmin = int ( input ( ">>>" ) )
        if taxmin  <  tasodifiy_son :
            print("Xato. Men o'ylagan son bundan kattaroq.Yana harakat qiling:", end='')
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq.Yana harakat qiling:", end='')
        else:
             break
        
    print(f"Tabriklayman. Men o'ylagan sonni {taxminlar}ta taxmin bilan topdingiz")
    return taxminlar
   

def son_top_pc(x=100):
    input(input(f"1 dan {x} gacha son o'ylang va enter tugmasini bosing. Men topishga harakat qilaman\n>>>"))
    taxminlar = 0
    quyi = 1
    yuqori = x
    
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri(t), men o'ylagan son bundan kattaroq(+), yoki kichikroq(-)" .lower() )
        
        if javob  ==  "-" :
            yuqori  =  taxmin - 1
        elif javob  ==  "+" :
            quyi  =  taxmin + 1
        else:
            break
    print(f"Men sizni soningzni {taxminlar}ta taxmin bilan topdim")
    return taxminlar
    
    
    
    
def play(x = 100):
    yana = True
    while yana:
        taxminlar_user  =  son_top ( x )
        taxminlar_pc  =  son_top_pc ( x )
        if  taxminlar_user  >  taxminlar_pc :
            print ( f"Men  { taxminlar_pc } ta taxmin bilan topdim va yutdim!!.\n\n ZO'R MEN SIZNI YUTDIM " )
        elif  taxminlar_user  <  taxminlar_pc :
            print( f"Siz  { taxminlar_user } ta taxmin bilan topdingiz va yutdingiz!!!. \n\nTabriklayman meni yutdingiz,  aqlli o'yinchi ekansiz!!!! " )
        else:
            print ( "DURRANG!!" )
        yana  =  int  ( input ( "Yana o'ynaymizmi. HA(1), YO'Q(0): " ) )
        
play()