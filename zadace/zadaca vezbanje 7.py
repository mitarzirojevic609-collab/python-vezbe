products = {
    "hleb" : {
        "cena" : 100,
        "kolicina" : 50,
    },
    "pivo" : {
        "cena" : 150,
        "kolicina" : 220,

}
}


option = None
while option not in ["dodaj", "obrisi"]:
    option = input("Sta zelite da odredite? [obrisi dodaj]").lower()

if option == "obrisi":
    product = None

    while product not in products:
        product = input("Unesite ime proizdvoda za brisanje").lower()

    del products[product]

elif option == "dodaj":

    product = None

    while product in products or product == None:
        product = input("Unesite ime proizdvoda koje ne postoji").lower()

    product_Price = None
    while product_Price == None or product_Price <=0:
        product_Price = int(input("unesite cenu proizvoda"))


    product_Amount = None
    while product_Amount == None or product_Amount <0:
        product_Amount = int(input("unesite kolicinu proizvoda"))

    print(product, product_Price, product_Amount)



    products[product] = {
        "cena" : product_Price,
        "kolicina" : product_Amount,

    }

print(products)