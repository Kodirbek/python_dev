#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:35:45 2023

@author: zero
"""
# =============================================================================
# 
# def get_user_details(ism, familiya, tyil, tjoy, email=None, tel=None):
#     """Mijoz haqidagi ma'lumotni lug'at ko'rinishida qaytaruvchi funksiya"""
#     users = {'ism': ism,
#              'familiya': familiya,
#              'tyil': tyil,
#              'tjoy': tjoy,
#              'email': email,
#              'tel': tel}
#     return users
# 
# mijozlar = []
# while True:
#     print('\nQuyidagi ma\'lumotlarni kiriting: ')
#     ism = input('Ismingiz: ')
#     familiya = input('Familiyangiz: ')
#     tyil = input('Tug\'ilgan yilingiz: ')
#     tjoy = input('Tug\'ilgan joyingiz: ')
#     email = input('Email manzilingiz (ixtiyoriy): ')
#     tel = input('Telefon raqamingiz (ixtiyoriy): ')
#     
#     mijozlar.append(get_user_details(ism, familiya, tyil, tjoy, email, tel))
#     
#     javob = input('Yana mijoz qo\'shasizmi? (yes/no): ')
#     if javob == 'no':
#         break
# 
# print('\nQuyida mijozlar ro\'yxati: ')    
# for mijoz in mijozlar:
#     
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}, {mijoz['tyil']}-yilda {mijoz['tjoy'].title()}da tug'ilgan."
#           f"\nEmail: {mijoz['email']}, telefon raqami: {mijoz['tel']}")
#     
# =============================================================================
    

# =============================================================================
# # Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
# 
# def get_biggest(x,y,z):
#     value = 0
#     if x>y and x>z:
#         value = x
#     elif y>z:
#         value = y
#     else:
#         value = z
#     
#     return value
# 
# get_biggest(15, -89, 8)
#     
# # Solution
# 
# def kattasi(x,y,z):
#     max = x
#     if y>=max:
#         max = y
#     if z>=max:
#         max = z
#     return max
# 
# kattasi(10,20,-5)
#     
# =============================================================================
    
# =============================================================================
#     
# # Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
# # (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)    
# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#                 
#     return tub_sonlar
# 
# tub_sonlar_top(1,20) 
#     
# n_list = list(range(2,6))
# print(n_list)
#     
# =============================================================================
    

# =============================================================================
# 
# # Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi 
# # sonlar ro'yxatni qaytaruvchi funksiya yozing. 
# # Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik 
# # Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 
# # 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
#     
# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[-1]+sonlar[-2])
#     
#     return sonlar
# 
# fibonacci(10)
# =============================================================================
 

# =============================================================================
# # Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi 
# # harfini katta harfga o'zgatiruvchi funksiya yozing.
# # Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat 
# # qaytaradigan qilib o'zgartiring   
# 
# def katta_harf(matnlar):
#     y_matnlar=[]
#     for i in range(len(matnlar)):
#         y_matnlar.append(matnlar[i].title())   
#     return y_matnlar
# 
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# print(katta_harf(ismlar))
# print(ismlar)
# 
# # Solution
# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar
# 
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)
# =============================================================================
    

# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan 
# foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at 
# qaytaradigan qilib yozing.

# Asl funksiya:
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)
    

# Solution:
    
def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)
    
    
    
    
    
    
    
    
    
    
    