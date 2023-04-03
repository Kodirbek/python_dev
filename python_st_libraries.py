# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime as dt
import math as m

# # Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring
# bugun = dt.date.today()
# for _ in range(10):
#     bugun = bugun + dt.timedelta(days=14)
#     print(bugun)
    
    
# # Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
# bugun = dt.date.today()
# ramazon_h = dt.date(2023, 4, 22)
# farq = ramazon_h - bugun
# print(farq)
# print(f"Ramazon Hayitiga {farq.days} kun qoldi.")


# # Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini 
# # qaytaruvchi funksiya yozing
# def otgan_vaqt(yyyy, mm, d):
#     t_kun = dt.date(yyyy, mm, d)
#     bugun = dt.date.today()
    
#     time_passed = bugun - t_kun
#     yil = dt.timedelta(days=365)
#     oy = dt.timedelta(days=30)
    
#     yillar = m.floor(time_passed / yil)
#     oylar = m.floor((time_passed % yil)/ oy)
#     kunlar = (time_passed % oy).days
    
#     print(f"Tug'ilgan kuningizdan hozirgacha {yillar} yil, {oylar} oy, {kunlar} kun o'tdi.")
    
    
# otgan_vaqt(1964, 11, 25)


# Foydalanuvchidan telefon raqamini kiritishni so'rang. 
# Kiritlgan qiymatni andoza yordamida tekshiring