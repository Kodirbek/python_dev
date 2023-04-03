
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:27:47 2023

@author: zero
"""

# =============================================================================
# # Ro'yxatni alifbo bo'yicha tartiblash
# cars = ['GM', 'Ford', 'Tesla', 'Audi', 'BMW']
# cars.sort()
# print(cars)
# 
# # Ro'yxatdagi elementlardan biri bosh harfda bo'lsa, unda o'sha element eng avval kelib keyin kichik 
# # harf bn boshlanadigan elementlar keladi. Shu sabab, listni sort qilganda avval barcha elementlarni 
# # .lower() yoki .upper() yordamida bir xil shaklga keltirib olish lozim. 
# 
# # Ro'yxatni alifboga teskari tartibda qaytarish uchun:
# cars.sort(reverse=True)
# print(cars)
# 
# # Yuqoridagi .sort funksiyasi list elementlari tartibini asl holidan tartiblangan holiga o'zgartiradi.
# # List'ning asl tartibini o'zgartirmagan holda sort qilish uchun quyidagi funksiya ishlatiladi:
# print(sorted(cars))
# print(sorted(cars, reverse=True))
# =============================================================================

# =============================================================================
# # Ro'yxatni .reverse() metodi yordamida teskari tartibga keltiramiz:
# print(cars)
# cars.reverse()
# print(cars)
# 
# # Ro'yxat uzunligini len() metodi yordamida aniqlaymiz:
# len(cars)
# 
# =============================================================================

# =============================================================================
# # RANGE() va qadamlar
# sonlar = list(range(0,11)) # 0 dan 10 gacha raqamlardan list yaratish
# print(sonlar)
# juft_sonlar = list(range(0,21,2)) # 0 dan 20 gacha 2 qadam oralig'ida sonlarni olish
# print(juft_sonlar)
# toq_sonlar = list(range(1,21,2))
# print(toq_sonlar)
# =============================================================================

# =============================================================================
# # MIN(), MAX(), SUM()
# narhlar = [12000, 15000, 600, 56000, 99000]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print(f"Eng arzon narh {arzon}, eng qimmat narh {qimmat}, Jami: {jami}.")
# =============================================================================


# =============================================================================
# # Ro'yxatni kesish:
#     
# cars = ['bmw', 'audi', 'tesla', 'gm', 'ford', 'mercedes-benz']
# # print(cars[1:4]) # prints 'audi', 'tesla', 'gm'
# # print(cars[3:]) # prints 'gm', 'ford', 'mercedes-benz'
# # print(cars[:3]) # prints 'bmw', 'audi', 'tesla'
# 
# # Ro'yxatdan nusxa olish:
# # Listlar reference type bo'lib, bit listdan boshqa list yaratganimizda ehtiyot 
# # bo'lishimiz kerak:
#     
# # my_cars = cars
# # my_cars.remove('bmw')
# # print(my_cars)
# # print(cars)
# 
# # Bu yerda har ikkala listdan ham 'bmw' o'chib ketdi. Demak yuqoridagi usul bilan 
# # nusxa yaratilmas, balki shunchaki orginal listga yana bir nom berilar ekan.
# # Bir listdan boshqa nusxa olish uchun esa quyidagi usuldan foydalanamiz:
# 
# my_cars =cars[:]
# my_cars.remove('bmw')
# print(my_cars)
# print(cars)
# 
# =============================================================================


# =============================================================================
# # Tuples
# # Tuple bu o'zgarmas ro'yxat bo'lib, listdagidek [] emas () bilan yaratiladi:
#     
# cars = ('bmw', 'audi', 'tesla', 'gm', 'ford', 'mercedes-benz')
# 
# # Tuple'ni o'zgartirish kerak bo'lsa uni listga o'zgartirib keyin amalga 
# # oshirsak bo'ladi:
# 
# cars = list(cars)
# cars.append('hyundai')
# cars = tuple(cars)
# 
# =============================================================================


davlatlar = ['uzb', 'kor', 'mor', 'usa', 'eng', 'fr', 'pol', 'den', 'mex']
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort() 
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)


juft_sonlar = list(range(120, 1200, 2)) 
print(len(juft_sonlar)) # 540
print(sum(juft_sonlar)) # 355860
print(max(juft_sonlar) - min(juft_sonlar)) # 1078
print(juft_sonlar[:21])
print(juft_sonlar[260:280])
print(juft_sonlar[-20:])


taomlar = ['osh', 'sho\'rva', 'shavla', 'do\'lma', 'manti']
nonushta = taomlar[:]
nonushta.remove('do\'lma')
nonushta.remove('manti')
nonushta.append('qaymoq')
nonushta.append('non')
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)
nonushta[0] = 'qand'





















