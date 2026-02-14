# zadatak 1
from itertools import count

lista = ["ovo je lista", 20, 20.5]
if isinstance(lista [0], str):
    print("prvi element je string")
#zadatak 2
if not lista:
    print("lista je prazna")
else:
    print(f"Lista ima {len(lista)} elemenata")
#zadatak3
if len(lista)>3:
    print("prvi element liste" [0])
    print("poslednji element liste" [-1])
else:
    print("lista je prekratka")
#zadatak 4
godina_starosti = [16,17, 23, 25, 30]
if any(godina <18 for godina in godina_starosti):
    print("nisu svi punoljetni")
#zadatak 5
cena_proizvoda = [500, 700, 800, 1200, 3000]
prosecna_cena = sum(cena_proizvoda) /len(cena_proizvoda)
print(prosecna_cena)
if prosecna_cena > 1000:
    print("skupo")
else:
    print("povoljno")
#zadatak 6
lista_stringova = ["Java", "C++", "Python"]
if "Python" in lista_stringova:
    print("u listi je Python")
else:
    print("")
#zadatak 7
brojevi = [3,4,2,1,]
pozitivni = 0
negativni = 0
for broj in brojevi:
    if broj > 0:
        pozitivni += 1
    elif broj < 0:
        negativni += 1
if pozitivni > negativni:
    print("vise pozitivnih")
#zadatak 8
reci = ["moc", "slava", "novac", "zdravlje", "sreca", "vjerovanje"]
najduza = max(reci, key=len)
if len(najduza)>8:
    print("najduza rec je veca od 8 slova")
#zadatak 9
ocene = [1,2,3,4,5]
if 1 in ocene:
    print("ima negativnih ocena")
#zadatak 10
for element in ocene:
    if not isinstance(element, int):
        print("lista ne sadrzi samo brojeve")
        break
    else:
        print("zbir je", sum(ocene))