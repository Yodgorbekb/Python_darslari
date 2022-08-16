from googletrans import Translator
tarjimon = Translator()
matn_uz = "Python - dunyodagi eng mashxur til"
tarjima = tarjimon.translate(matn_uz, dest='ru')
print(tarjima.origin)
print(tarjima.text)
print(tarjima.scr)
