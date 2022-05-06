#########################################
# groupe MIASHS 1
# Nathan TIPAKA
# Johan CHENG
# Clara SAUNIER (SION-SAUNIER)
# https://github.com/uvsq22101095/projet_stats
#########################################

import random as rd

import tkinter as tk

HEIGHT = 500
WIDTH = 500

racine = tk.Tk()
canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH)

L = []
x = 0
y = 0
X_moyen = 0
Y_moyen = 0
varX = 0
varY = 0
n = int(input("un nombre entier naturel"))

# créer des nombre au hazards et les entre dans un fichier texte
fic = open("coordonnées", "w")
for i in range(n):
    x = rd.randint(1, 500)
    y = rd.randint(1, 500)
    fic.write(str(x) + " " + str(y) + "\n")
fic.close()

# transforme le fichier texte en liste de coordonées
fic = open("coordonnées", "r")
for i in range(n):
    line = fic.readline()
    val = line.split()
    L += [val[0], val[1]]
fic.close()

# créer l'abscice et l'ordonnée du canvas
for i in range(5):
    canvas.create_line(
        (0, i*100),
        (WIDTH, i*100),
        fill="pink",
        width=3
    )
    canvas.create_line(
        (i*100, 0),
        (i*100, HEIGHT),
        fill="pink",
        width=3
    )

# créer des axes pour que le canvas soit plus lisible
canvas.create_line(
    (0, 0),
    (0, HEIGHT),
    fill="blue2",
    width=10
)
canvas.create_line(
    (0, HEIGHT),
    (WIDTH, HEIGHT),
    fill="blue2",
    width=3
)
canvas.create_line(
    (0, 0),
    (10, 10),
    fill="blue2",
    width=3
)
canvas.create_line(
    (WIDTH-10, HEIGHT-10),
    (WIDTH, HEIGHT),
    fill="blue2",
    width=3
)


def PLACEMENT_DES_POINTS(n):
    for i in range(0, 2*n-2, 2):
        x = int(L[i])
        y = int(L[i+1])
        # le "HEIGHT -" est nécessaire pour avoir un plan dans le bon sens
    canvas.create_oval(x+1, HEIGHT-y+1, x-1, HEIGHT-y-1, fill="red")
    pass


for i in range(0, 2*n-2, 2):
    X_moyen += int(L[i]) / n
    Y_moyen += int(L[i+1]) / n
canvas.create_oval(
    X_moyen + 5,
    HEIGHT - Y_moyen + 5,
    X_moyen - 5,
    HEIGHT - Y_moyen - 5,
    fill="deep pink"
)
print(
    "la moyenne des abscices est :", X_moyen,
    "\n La moyenne des ordonnées est :", Y_moyen
)

for i in range(0, 2*n-1, 2):
    varX = ((L[i]-X_moyen)**2)/n
    varY = ((L[i+1]-X_moyen)**2)/n

racine.mainloop()