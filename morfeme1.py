# -*- coding: utf-8 -*-
niska = "Da li je moguće da sam i dalje niska?!"
jedan_karakter = niska[0]
isti_karakter=niska[-38]
print(jedan_karakter)
print(len(niska))
print(isti_karakter)


nekoliko_karaktera = niska[0:15]
print(nekoliko_karaktera)

nekoliko_karaktera_s_kraja = niska[-15:-2]
print(nekoliko_karaktera_s_kraja)


reč="pevač"
reč_osnova=reč[0:3]
print(reč_osnova)
reč_sufiks=reč[3:5]
print(reč_sufiks)

rec="beogradski"
print(len(rec))
rec_osnova=rec[0:7]
print(rec_osnova)
rec_sufiks=rec[7:11]
print(rec_sufiks)

rec2="spavanje"
print(len(rec2))
rec2_osnova=rec2[0:4]
print(rec2_osnova)
rec2_tematski_vokal=rec2[4]
print(rec2_tematski_vokal)
rec2_sufiks=rec2[5:]
print(rec2_sufiks)


