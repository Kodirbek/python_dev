# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime as dt
import math as m
import re

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


# # Foydalanuvchidan telefon raqamini kiritishni so'rang. 
# # Kiritlgan qiymatni andoza yordamida tekshiring
# andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
# while True:
#     tel = input("Telefon raqamingizni kiriting: ")
#     if re.match(andoza, tel):
#         print("Qabul qilindi.")
#         break
#     else:
#         print("Telefon raqam formati not'g'ri.")


# Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. 
# Quyidagi matndan namuna sifatida foydalanishingiz mumkin:
    
matn = """Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI Ushbu 
darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. 
Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test """

andoza = "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
url = re.findall(andoza,matn)
print(url)

# matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza,matn)
# print(email)







