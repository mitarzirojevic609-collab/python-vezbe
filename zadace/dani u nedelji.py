import matplotlib.pyplot as plt

x= [  "Ponedeljak", "Utorak", "Sreda", "Cetvrtak",
    "Petak",  "Subota", "Nedelja"

]
y = [22, 25, 21, 27, 24, 29, 23]

plt.plot(x, y, marker= 'o', color= "red")

plt.annotate("najtopliji dan",
             xy=("Subota", 29),
             arrowprops=dict(facecolor="black", shrink=0.25)



             )

plt.show()

