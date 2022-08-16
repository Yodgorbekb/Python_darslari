                               #PYTHON DARSLARI
                               #23-DARS
                               #MODULLAR
   #   KIRISH
    
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
    