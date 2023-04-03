# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime as dt


# Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring

bugun = dt.date.today()
for _ in range(10):
    bugun = bugun + dt.timedelta(days=14)
    print(bugun)