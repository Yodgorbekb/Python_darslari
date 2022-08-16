# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:58:29 2022

Python darslari
39-dars
PYTHON TASHQI KUTUBXONASI
"""
#pip install googletrans==3.1.0a0
#from googletrans import Translator
#tarjimon = Translator()

#matn_uz = "Python - dunyodagi eng mashxur til"

#tarjima = tarjimon.translate(matn_uz)
#print(tarjima.origin)

#print(tarjima.txt)

#print(tarjima.src)

#Boshqa tillarni tanlash

#3matn_uz = "Python - dunyodagi eng mashxur til"

#tarjima = tarjimon.translate(matn_uz, dest='ru')
#print(tarjima.txt)

#requests moduli
#import requests
#from pprint import pprint

#sahifa = "https://kun.uz/news/main"
#r = requests.get(sahifa)
#pprint(r.text)

#country = "Uzbekistan"
#url = "https://restcountries.eu/rest/v2/name/Uzbekistan"
#r = requests.get(url)
#r_json = r.json(url)
#r_json = r.json()[0]
#pprint(r_json['capital'])


#import requests
#import googletrans

#url = "https://api.adviceslip.com/advice"
#r = requests.get(url)
#advice = r.json()['slip']['advice']
#print(advice)

#translator = googletrans.Translator()
#tarjima = translator.translate(advice, dest='uz')
#print(tarjima.text)



#import requests
#from bs4 import BeautifulSoup

#sahifa = "https://kun.uz/news/main"
#r = requests.get(sahifa)
#pprint(r.text)

#soup = BeautifulSoup(r.text, 'html.parser')
#news = soup.find_all(class_='news-title')
#print(news[0].text)



#import requests
#from bs4 import BeautifulSoup
#from wordcloud import WordCloud
#import matplotlib.pyplot as plt


#sahifa = "https://kun.uz/news/main"
#r = requests.get(sahifa)
#pprint(r.text)

#soup = BeautifulSoup(r.text, 'html.parser')
#news = soup.find_all(class_='news-title')
#matn=""
#for n in news:
#    matn += n.text

# kerakmas so'zlar
#stopwords = ["учун","бўйича","лекин","билан","ва","бор","ҳам","хил","йил"]
# bulutni yaratamiz
#wordcloud = WordCloud(width = 1000, height = 1000, 
#                background_color ='white', 
#                stopwords = stopwords, 
#                min_font_size = 20).generate(matn) 
  
# plot the WordCloud image                        
#plt.figure(figsize = (8, 8), facecolor = None) 
#plt.imshow(wordcloud) 
#plt.axis("off") 
#plt.tight_layout(pad = 0) 
#plt.show()


#import numpy as np
#import cv2

#cap = cv2.VideoCapture(0)
#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

#while True:
#    ret, frame = cap.read()

#   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#    for (x, y, w, h) in faces:
#        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
#        roi_gray = gray[y:y+w, x:x+w]
#        roi_color = frame[y:y+h, x:x+w]
#        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
#        for (ex, ey, ew, eh) in eyes:
#            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

#    cv2.imshow('frame', frame)

#    if cv2.waitKey(1) == ord('q'):
#break
#cap.release()
#cv2.destroyAllWindows()



#from fuzzywuzzy import fuzz
#from fuzzywuzzy import process
#from uzwords import words

#print(fuzz.ratio("salom",'assalom'))
#print(fuzz.ratio("salom",'salim'))


# # Grafik interfeys
