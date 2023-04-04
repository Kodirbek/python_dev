#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 06:38:35 2023

@author: zero
"""

from googletrans import Translator
tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)

# matn_uz = "Python - dunyodagi eng mashxur dasturlash tili!"

# tarjima = tarjimon.translate(matn_uz) #hech qanday parametr berilmasa, avtomtik ingliz tiliga terjima bo'ladi
# print(tarjima.origin) #asl matn
# print(tarjima.src) #asl matn tilini ko'rsatadi
# print(tarjima.text)

# tarjima_ru = tarjimon.translate(matn_uz, dest="ru") #dest='istalgan til'
# print(tarjima_ru.text)


# matn_en = "Tashkent is the capital of Uzbekistan"
# tarjima_uz = tarjimon.translate(matn_en, dest='uz')
# print(tarjima_uz.text)


msg = "Tarjima uchun so'z kiriting (chiqish uchun 'q'ni kiriting): "

while True:
    text = input(msg)
    if text == "q":
        break
    else:
        tarjima = tarjimon.translate(text, src='uz', dest='en')
        print(tarjima.text)