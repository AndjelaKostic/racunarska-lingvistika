# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 01:31:16 2017

@author: Korisnik
"""
"""
DOMAĆI ZADATAK 2:
Napravite mini rečnik sinonima i antonima pod promenljivom "rečnik" tako što
ćete odabrati 3 reči i pronaći uz njih barem 2 antonima i 2 sinonima.
Strukura koju napišete treba da omogući da:
    - Komanda print(rečnik["reč"]["sinonimi"]) ispiše sve sinonime reči.
    - Komanda print(rečnik["reč"]["antonimi"]) ispiše sve antonime reči.
    - Komanda print(rečnik["reč"]["sinonimi"][0]) ispiše prvi sinonim reči.
    - Komanda print(rečnik["reč"]["antonimi"][1]) ispiše drugi antonim reči.
    - Pokretanje postojećih linija koda ispiše reč, zatim njene sinonime,
      zatim njene antonime.
Nisku "reč" u gornjim primerima zamenite svojim rečima, a termine "sinonimi" i
"antonimi" koristite u postojećoj formi.
O tome šta postojeće linije koda rade razgovaraćemo na sledećem predavanju.
"""

# ovde dodajte svoj kod

rečnik ={"radostan":{"sinonimi":["srećan","veseo"],"antonimi":["tužan","žalostan"]},"istinitost":{"sinonimi":["verodostojnost","tačnost"],"antonimi":["neistinost","netačnost"]},"vredan":{"sinonimi":["dragocen","skup"],"antonimi":["bezvredan","jeftin"]}}
print(rečnik["radostan"]["sinonimi"])
print(rečnik["radostan"]["antonimi"])
print(rečnik["radostan"]["sinonimi"][0])
print(rečnik["radostan"]["antonimi"][1])

print(rečnik["istinitost"]["sinonimi"])
print(rečnik["istinitost"]["antonimi"])
print(rečnik["istinitost"]["sinonimi"][0])
print(rečnik["istinitost"]["antonimi"][1])

(rečnik["vredan"]["sinonimi"])
print(rečnik["vredan"]["antonimi"])
print(rečnik["vredan"]["sinonimi"][0])
print(rečnik["vredan"]["antonimi"][1])


for reč in rečnik.keys():
    
    print("Reč: ", reč) 
    sin = "Sinonimi: "
    ant = "Antonimi: "

    for sinonim in rečnik[reč]["sinonimi"]:
        sin += sinonim + ", "
    print(sin[:-2])

    for antonim in rečnik[reč]["antonimi"]:
        ant += antonim + ", "    
    print(ant[:-2] + "\n")

