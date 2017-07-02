# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 12:35:14 2017

@author: Korisnik
"""

x = 2
y = 3

if x < 5:
    x = x + 2 # x += 2
else:
    y = y + 1 # y += 1

print(x, y)    
a = 5
b = 4

if a < b:
    print("Ovo ispisujem ako je a manje od b")
elif a > b:
    print("Ovo ispisujem ako je a veće od b")
else:
    print("Ovo ispisujem u svim ostalim slučajevima, tj. ako je a jednako b")
    
    
a=4
b=4
c=5
if (a==b) and (c>b):
     print("If je ispunjen")
else:
     print("If nije ispunjen")
     
a =19
b =4
c =10

if a < b:
    if a < c:
        print("Ovo ispisujem ako je a manje od b i ako je a manje od c")
    else:
        print("Ovo ispisujem ako je a manje od b i ako a nije manje od c")

if a < b:
    if a < c:
        print("Ovo ispisujem ako je a manje od b i ako je a manje od c")
else:
    print("Ovo ispisujem ako a nije manje od b")
    
x=2
y=3
while x<5:
    y = y * 2 # y *= 2
    x = x + 1 # x += 1
    print(x, y)
    
for i in range(0,10):
    print("ponavljam se")
    print(i)
 
for i in range(10,0,-1):
    print(i)
    
mlSaradnici = ["Milena", "Milan", "Jovana", "Tijana","Isidora"]
for saradnik in mlSaradnici:
    print(saradnik)    
    
brojevi = 0
for x in range(0,101):
    if x < 20 and x % 2 == 0:
        brojevi = brojevi + 1 # brojevi += 1
print(brojevi)
    
reči = ["novinar", "trener", "muzičar", "pekar", "lekar", "apotekar"]
sufiks = "ka"
print(len(reči))

for i in range(len(reči)):
	reči[i] = reči[i] + sufiks

print(reči)

for i in range(len(reči)):
    reči[i]=reči[i][:-2]
print(reči)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    