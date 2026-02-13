#zadatak1
brojevi = [15,20,30,40,50]
#zadatak2
print(brojevi [0])
print(brojevi [4])
#zadatak3
print(f"lista brojevi ima {len(brojevi)} elemenata")
#zadatak4
ukupan_zbir = sum(brojevi)
print(ukupan_zbir)
#zadatak5
prosecna_vrednost = sum(brojevi) / len(brojevi)
print(prosecna_vrednost)
#zadatak 6
gradovi = ["Banjaluka", "Istocno Sarajevo","Doboj", "Bijeljina",  ]
#zadatak7
spojeni_gradovi = ",".join(gradovi)
print(spojeni_gradovi)
#zadatak8
brojevi.append(60)
print(brojevi)
#zadatak9
brojevi.insert(1 , 10)
print(brojevi)
#zadatak10
brojevi.remove(60)
print(brojevi)
#zadatak11
brojevi = [15,20,30,40,50]
print("Max: ", max(brojevi))
print("Min: ", min(brojevi))
#zadatak12
brojevi.sort()
print(brojevi)
#zadatak13
print(brojevi[::-1])
#zadatak14
kopija = brojevi.copy()
print(kopija)
#zadatak15
drugi_brojevi =[1, 2, 3, 4, 5, 6]
brojevi += drugi_brojevi
print(brojevi)
#zadatak16
brojevi = [15,20,30,40,50]
brojevi = brojevi.count(5)
print(brojevi)
#zadatak17
brojevi = [15,20,30,40,50]
if 7 in brojevi:
    print("Element exists in the list")
else:
    print("Element does not exist in the list")
#zadatak18
cena_proizvoda = [500, 600, 700, 800, 900, 1000]
ukupna_cena_proizvoda = sum(cena_proizvoda)
prosecna_cena_proizvoda = sum(cena_proizvoda) / len(cena_proizvoda)
print(ukupna_cena_proizvoda)
print(prosecna_cena_proizvoda)
#zadatak 19
imena = ["Milos", "Stefan,", "Milutin"]
print(f"u listi su sledeca imena: ", " ".join(imena))
#zadatak 20
ocene=[3,4,3,5,5]
prosecna_ocena =(sum(ocene)/ len(ocene))
print(f"prosecna ocena: {prosecna_ocena} najveca ocena: {max(ocene)} najmanja ocena: {min(ocene)}")
