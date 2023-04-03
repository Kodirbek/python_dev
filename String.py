#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 21:16:49 2023

@author: zero
"""

# =============================================================================
# # STRING USTIDA AMALLAR

# ism = 'Ahad'
# print('Mening ismim ', ism)
# print('Mening ismim ' + ism)
# familiya = 'Qayum'
# print(ism + familiya)
# print(ism + ' ' + familiya)
# =============================================================================

# =============================================================================
# # f-string
# 
# ism = "Ahad"
# familiya = "Qayum"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)
# 
# ism = "James"
# familiya = "Bond"
# print(f"Salom, mening ismim {ism}. {ism} {familiya}!")
# 
# =============================================================================

# =============================================================================
# # MAHSUS BELGILAR
# 
# print("Hello World!")
# print("Hello \tWorld!")   # \t -> TAB
# print("Hello \nWorld")    # \n -> next line
# 
# =============================================================================

# =============================================================================
# # STRING METODLAR
# 
# ism = "James"
# familiya = "Bond"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())
# print(ism_sharif.lower())
# print(ism_sharif.title())  # har bir so'z bosh harf bn boshlanadi
# print(ism_sharif.capitalize()) # faqat birinchi so'z bosh harf bn boshlanadi
# =============================================================================

# =============================================================================
# # STRIP funksiyasi
# 
# meva = "    olma    "
# print("Men " + meva + "ni yaxshi ko'raman")
# print("Men " + meva.lstrip() + "ni yaxshi ko'raman")
# print("Men " + meva.rstrip() + "ni yaxshi ko'raman")
# print("Men " + meva.strip() + "ni yaxshi ko'raman")
# 
# # yuqoridagi funksiyalar chapdagi, o'ngdagi yoki ikkala tomondagibo'shliqlarni olib tashlaydi
# 
# =============================================================================


# INPUT funksiyasi

ism = input("Ismingiz nima?\n>>>")
print("Assalomu alaykum, " + ism.title())




















