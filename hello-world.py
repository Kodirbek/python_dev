#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 22:10:42 2023

@author: zero
"""

import math

# 1. 5 ning 4-darajasini toping
print("5 ning 4-darajasi", 5**4, ".")

# 2. 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
print("22 ni 4 ga bo'lganda", 22%4, "qoldiq qoladi.")

# 3. Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping.
print("Tomonlari 125 ga teng kvadratning yuzi", 125**2, "perimetri esa", 125*4, "ga teng.")

# 4. Diametri 12 ga teng bo'lgan doiraning yuzini toping (π = 3.14 deb oling).
print("Diametri 12 ga teng bo'lgan doiraning yuzi", 3.14 * 6**2, "ga teng.")

# 5. Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping.
print("Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi", math.sqrt(6**2 + 7**2),"ga teng.")


radius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
print("Radiusi" , radius, "ga teng aylananing yuzi =", aylana_yuzi)



