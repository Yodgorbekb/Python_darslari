                                    #PYTHON DARSLARI 
                                    #19-DARS
                                    #FUNKSIYALAR 

                      #YANGI FUNKSIYA

#def salom_ber():
#    """Salom beruvchi funksiya"""
#    print("Assalomu alaykum!")
    
#salom_ber()   

                    #FUNKSIYANI CHAQIRAMIZ
#def salom_ber(ism): # yangi funksiya
#    """Foydalanuvchi ismini qabul qilib, 
#    unga salom beruvchi funksiya"""   #funksiya haqida ma'lumot
#    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
    
#salom_ber('hasan')
#salom_ber('olim')

#salom_ber()

                     #QIYMAT QABUL QILUVCHI FUNKSIYA
#def toliq_ism(ism,familiya):
#    """Foydalanuvchi ismi va familiyasini 
#    jamlab chiqaruvchi funksiya"""
#    print(f"Foydalanuvchi ismi: {ism.title()}\n"
#          f"Foydalanuvchi familiyasi: {familiya.title()}")
    
#toliq_ism('yodgorbek','boltaev')    

#def yosh_hisobla(ism,t_yil):
#    """Foydalanuvchi yoshini hisoblaydigan dastur"""
#    print(f"{ism.title()} {2022-t_yil} yoshda")

#yosh_hisobla('yodgorbek',2008)
#yosh_hisobla(2008,'olim')

#yosh_hisobla(t_yil=1997, ism='olim')


#def toliq_ism(ism,familiya):
#    """Foydalanuvchi ismi va familiyasini 
#    jamlab chiqaruvchi funksiya"""
#    print(f"Foydalanuvchi ismi: {ism.title()}\n"
#          f"Foydalanuvchi familiyasi: {familiya.title()}")
    
#toliq_ism(familiya='boltaev',ism='yodgorbek')    

                      #STANDART QIYMAT

#def yosh_hisobla(tugilgan_yil, joriy_yil=2022):
#    """Foydalanuvchi tug'ilgan yilidan uning yilini hisoblaydigan funksiya"""   
#    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
#    
#yosh_hisobla(2008,2022)
#yosh_hisobla(1993)    

                                          #AMALIYOT
#def ism_yosh_t_yil(ism,yosh,joriy_yil=2022):
#    """Foydalanuvchi ismini, yoshini so'rab
#    uning tug'ilgan yilini chiqaruvchi funksiya"""
#    print(f"Salom {ism.title()} siz {joriy_yil-yosh} yilda tug'ilgan ekansiz")

#funksiya nomi{ ism_yosh_joriy_yil() ]   
 
#ism_yosh_t_yil('ogabek',20,2022)



#def son_kv_kub(son):
#    """Foydalanuvchidan son olib uning kvadrati
#    va kubini hisoblaydigan funksiya"""
#    print(f"{son} sonining kvadrati {son**2} ga teng \n"
#          f"{son} sonining kubi {son**3} ga teng \n"
#          f"{son} sonining 4-darajasi {son**4} ga teng \n"
#          f"{son} sonining 5-darajasi {son**5} ga teng \n"
#          f"{son} sonining 6-darajasi {son**6} ga teng \n"
#          f"{son} sonining 7-darajasi {son**7} ga teng \n"
#          f"{son} sonining 8-darajasi {son**8} ga teng \n"
#          f"{son} sonining 9-darajasi {son**9} ga teng \n"
#          f"{son} sonining 10-darajasi {son**10} ga teng")
    
#son_kv_kub(2)





#def son_toq_juft(son):
#    """Foydalanuvchidan son olib uni toq
#    yoki juft ligini aniqlaydigan funksiya"""
#    if son%2:
#         print(f"{son} toq son") 
#    else:      
#         print(f"{son} juft son")

#son_toq_juft(6)
 
#def kt_kch(son1,son2):
#    """Foydalanuvchidan 2ta son olib
#    uning qaysi biri katta ekanini aniqlab 
#    konsolga chiqaradigan funksiya"""
#    if son1>son2:
#        print(f"Katta son {son1} ")
#    else:
#        print(f"Katta son {son2} ")
   
#kt_kch(23,3)


