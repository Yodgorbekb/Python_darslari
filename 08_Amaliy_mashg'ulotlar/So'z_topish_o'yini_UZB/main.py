import random

from uzwords import words


def get_word():

    word  =  random.choice ( words )

    while  " - "  in  word  or  " "  in  words :

        word  =  random.choice ( words )

    return  word.upper ()



def display(user_letters, word):

    display_letter  =  " "

    for  letter  in  word :

        if  letter  in  user_letters :

            display_letter  +=  letter

        else :

            display_letter  +=  " - "

    return  display_letter



def play():

    word  =  get_word ()

    # So'zdagi harflar

    word_letters  =  set ( word )

    # Foydalanuvchi kiritgan harflar

    user_letters  =  ""

    print ( f"Men { len ( word ) } ta harifli so'z o'yladim.  Тоpa olasizmi? " )

    # print(word)

    while  word_letters :

        print ( display ( user_letters,  word ) )

        if  user_letters :

            print ( f"SHu vaqtgacha kiritgan so'zlaringiz:  { user_letters } " )


        letter  =  input ( " Xarf kiriting:  " ).upper()

        if  letter  in  user_letters :

            print  ( " Bu  harifni avval kiritgansiz.  Boshqa harf kiriting. " )

            continue

        elif  letter  in  word :

            word_letters.remove ( letter )

            print ( f"{ letter }  Xarf to'g'ri." )

        else :

            print ( " Bunday harf yo'q. " )

        user_letters  +=  letter

    print ( f"Tabriklayman!  { word }  so'zini { len ( user_letters ) } ta urinishda topdingiz. " )


#from uzwords import words


#def get_word():
#    word = random.choice(words)
#    while "-" in word or " " in word:
#        word = random.choice(words)
#    return word.upper()


#def display(user_letters, word):
#    display_letter = " "
#    for letter in word:
#        if letter in user_letters.upper():
#            display_letter += letter
#        else:
#            display_letter += "-"
#        return display_letter
            
    
#def play():
#    word = get_word()
    
#    word_letters = set(word)
#    
#    user_letters = ''
#    print(f"Мен {len(word)} та харфли соз ойладим. Топа оласизми?")
#    
#    while len(word_letters)>0:
#        print(display(user_letters,word))
#        if len(user_letters)>0:
#            print(f"Шу вактгача киритган харфларингиз: {user_letters} ")
#        
#        letter = input("Харф киритинг: ").upper()
#        if letter in user_letters:
#            print("Бу харифни аввал киритгансиз. Бошка харф киритинг:")
#            continue
#        elif letter in word:
#            word_letters.remove(letter)
#            print(f"{letter} харфи тогри. ")
#        else:
#            print("Бундай харф йок")
#        user_letters += letter
#    print(f"Табриклайман. {word} созини {len(user_letters)} та уринишда топдингиз. ")
            
    


