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
Lx = []
Ly = []
list1, list2 = [], []
s = []
q = []
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Projet stats")


canvas.create_line((0, 0), (0, 500), width=10, fill="maroon2")
canvas.create_line((0, 500), (500, 500), width=3, fill="maroon2")
canvas.create_line((0, 0), (0, 500), width=10, fill="maroon2")
canvas.create_line((0, 0), (10, 10), width=2, fill="maroon2")
canvas.create_line((490, 490), (500, 500), width=2, fill="maroon2")

for i in range(5):
    canvas.create_line((0, i*100), (500, i*100), fill="pink", width=3)
    canvas.create_line((i*100, 0), (i*100, 500), fill="pink", width=3)
    canvas.create_line((0, i*100), (WIDTH, i*100), fill="pink", width=3)
    canvas.create_line((i*100, 0), (i*100, HEIGHT), fill="pink", width=3)

nb = 100


def creer_fichier_alea(nb):
    fichier = open("coordonnees.txt", "w")
    for i in range(0, nb, 2):
        x = int(rd.randint(0, 500))
        y = int(rd.randint(0, 500))
        fichier.write(str(x) + " " + str(y) + "\n")
    fichier.close()


def lit_fichier_X():
    X = []
    fichier = open("coordonnees.txt", "r")
    for i in range(0, nb//2):
        line = fichier.readline()
        val = line.split()
        X += [val[0]]
    fichier.close()
    return(X)


def lit_fichier_Y():
    Y = []
    fichier = open("coordonnees.txt", "r")
    for i in range(0, nb//2):
        line = fichier.readline()
        val = line.split()
        Y += [val[1]]
    fichier.close()
    return(Y)


def trace_Nuage(X, Y):
    nb_points = 0
    x = X
    y = Y
    for i in range(0, nb//2):
        abscice = x[i]
        ordonnees = y[i]
        canvas.create_oval(
            int(abscice)+1,
            HEIGHT-(int(ordonnees))+1,
            int(abscice)-1,
            HEIGHT-(int(ordonnees)-1)
        )
        nb_points += 1
    return(nb_points)


def tracer_droite(serie):
    a = int(serie[0])
    b = int(serie[1])
    color = int(rd.randint(1, 5))
    if color == 1:
        c = "blue2"
    elif color == 2:
        c = "red"
    elif color == 3:
        c = "maroon2"
    elif color == 4:
        c = "dark green"
    else:
        c = "dark violet"
    d = canvas.create_line(
            0,
            HEIGHT-b,
            WIDTH,
            HEIGHT-(a*int(WIDTH)+b),
            fill=c
        )
    return(d)


def changer_couleur(serie):
    tracer_droite(serie)


def moyenne(serie):
    valeur_moyenne = 0
    m = serie
    for i in range(0, nb//2):
        M = int(m[i])
        valeur_moyenne += M/(nb//2)
    return(valeur_moyenne)


def variance(serie):
    var = 0
    v = serie
    for i in range(0, nb//2):
        V = int(v[i])
        var += (V-int(moyenne(serie))**2)/(nb//2)
    return(var)


def covariance(serieX, serieY):
    cov = 0
    X = serieX
    Y = serieY
    for i in range(0, nb//2):
        x = int(X[i])
        y = int(Y[i])
        cov += ((x-moyenne(serieX))*(y-moyenne(serieY)))/nb
    return(cov)


def correlation(serieX, serieY):
    a = (int(covariance(serieX, serieY)))
    b = (int(variance(serieX)))*int(variance(serieY))
    cor = (a/(b)**1/2)
    return(cor)


def fortecorrelation(serieX, serieY):
    cor = correlation(serieX, serieY)
    if cor > 0.8 or cor < -0.8:
        return(True)
    else:
        return(False)


def droite_reg(serieX, serieY):
    a = (int(correlation(serieX, serieY))/(int(variance(serieX))))
    b = (int(moyenne(serieY)-a*int(moyenne(serieX))))
    return(a, b)


def dessin(event):
    global Lx, Ly
    xclic = event.x
    yclic = event.y
    while 0 < xclic < WIDTH and 0 < yclic < HEIGHT:
        Lx.append(xclic)
        Ly.append(yclic)
    trace_Nuage(Lx, Ly)


###
# def dessiner(n):
#     global list1, list2
# tracage des points avec la souris lors du clic gauche
#    cv.create_line(
#        (float(n.x),
#        float(n.y)),
#        (float(n.x) + 2,
#        float(n.y) + 2),
#        fill='purple'
#    )
#     list1.append(n.x)  # creation des listes des coordonnes de la souris
#     list2.append(n.y)
###

def activer():
    root.bind('<Button-1>', dessin)


def desactiver_dessin():
    root.unbind('<Button-1>')


droite = tk.Button(
    text="tracer la droite",
    fg="black",
    bg="white",
    command=lambda: tracer_droite(
            droite_reg(
                lit_fichier_X(),
                lit_fichier_Y()
            )
        )
    )


couleur = tk.Button(
    text="changer la couleur",
    fg="black",
    bg="white",
    command=lambda: changer_couleur(
            tracer_droite(
                droite_reg(
                    lit_fichier_X(),
                    lit_fichier_Y()
                )
            )
        )
    )


quit = tk.Button(
    text="quitter",
    fg="black",
    bg="white",
    command=root.destroy
)


nuage = tk.Button(
    text="tracer le nuage de points",
    fg="black",
    bg="white",
    command=lambda: trace_Nuage(
        lit_fichier_X(),
        lit_fichier_Y()
    )
)


dessin1 = tk.Button(
    text="dessin nuage ",
    fg="black",
    bg="white",
    command=activer()
)


desactiver = tk.Button(
    text="desactiver le mode dessin",
    fg="black",
    bg="white",
    command=desactiver_dessin()
)

creer_fichier_alea(nb)


nuage.grid(column=0, columnspan=2, row=3)
canvas.grid(column=0, row=0, rowspan=3)
droite.grid(column=1, row=0)
couleur.grid(column=1, row=1)
dessin1.grid(column=1, row=3)
desactiver.grid(column=0, columnspan=2, row=4)
quit.grid(column=1, row=2)


root.mainloop()
