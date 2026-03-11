products = {
    "hleb" :{
        "cena" : 100,
        "kolicina": 50,
    },
    "pivo" : {
        "cena": 150,
        "kolicina": 220
    },
    "narandze" : {
        "cena": 240,
        "kolicina": 120
    }
}

allowed_options = ["dodaj", "obirsi", "izlistaj",
                   "stop", "istorijat", "obrisi sve",
                   "prikazi najskuplji proizvod", "pnp"]

option = None
history = []

while option not in allowed_options:
    option = input(f"Sta zelite da odradite{", ".join(allowed_options)} \n").lower()

    if option == "obrisi":
        product = None

        while product not in products:
            product = input("unesite ime proizvoda za brisanje:\n").lower()

            del products[product]

            msg = f"obrisali ste {product}\n"
            print(msg)
            history.append(msg)
            option = None

    elif option == "dodaj":

        product = None

        while product in products or product == None:
            product = input("unesite ime proizvoda koje ne postoji:\n")

        product_price = None
        while product_price is None or product_price <=0:
            product_price = int(input("Unesite cijenu proizvoda:\n"))

        product_amount = None
        while product_amount is None or product_amount < 0:
            product_amount = int(input("Unesite kolicinu proizvoda:\n"))

        products[product] = {
            "cena" : product_price,
            "kolicina": product_amount,
        }
        option = None

        msg = f"Dodali ste novi proizvoda {product}\n"
        print(msg)
        history.append(msg)

    elif option == "izlistaj":
        print(products)
        option = None

    elif option == "istorijat":
        print(history)
        option = None

    elif option == "obrisi sve":
        product = {}
        option = None

    elif option == "prikazi najskuplji proizvod" or "pnp":

        most_expensive_price = 0
        most_expensive_product = None


        for product in products:
           if most_expensive_price < products[product]["cena"]:
            most_expensive_price = products[product]["cena"]
            most_expensive_product = product
            print(most_expensive_product, most_expensive_price)

        print(products[most_expensive_product]["cena"])

print(products)

