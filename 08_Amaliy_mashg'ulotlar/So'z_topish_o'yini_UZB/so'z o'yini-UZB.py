# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 07:31:14 2022

@author: Ogabek
"""
import random 
from uzwords import words


def get_word():
    word  =  random.choice ( words )
    while  "-"  in  word  or  " "  in  word :
        word  =  random.choice ( words )
    return  word.upper()


def display(user_letters, word):
    display_letter  =  " "
    for  letter  in  word :
        if  letter  in  user_letters :
            display_letter  +=  letter
        else:
            display_letter  +=  " - "
    return  display_letter
            
    
def play():
    word  =  get_word()
    
    word_letters  =  set ( word )
    
    user_letters = ''
    print(f"Men {len(word)} ta harfli so'z o'yladim. Men o'ylagan so'zni toping?")
 
    while  len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f"SHu vaqtgacha kiritgan harflaringiz: {user_letters} ")
        
        letter = input("Harf kiriting: ").upper()
        if letter in user_letters:
            print ("Bu harfni avval kiritgansiz.  Boshqa harf kiriting: ")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} HARFI TO'G'RI. ")
        else:
            print("Bunday harf yo'q")
        user_letters += letter

    print(f"TABRIKLAYMAN. {word} so'zini {len(user_letters)} ta urinishda topdingiz. ")


play()