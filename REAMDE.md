import time
import json

# script pour remplir le dico
import time
d = {}
x = 100
while x > 0:
    x = x-1
    p = ''
    p = input("le nom du gars")
    a = input()
    a = int(a)
    d[a] = p
    print(d)

with open("dates_anniv.json") as json_data:
    d = json.load(json_data)
print(d)

# Obtenir l'heure et la date locale
now = time.localtime(time.time())
jour = time.strftime("%m/%d", now)


liste des noms : 
Louise Meirieu  09/02
Antoine Yeterian  29/05
Aude Hayette  03/01
Olivier Piquant  01/04
Nolwenn Piquant  27/12
Kerrien Piquant  23/02
Geraldine Mercier  13/10
Caro  29/01
Hugo Pham  28/06
Rania Benchekroun 28/07
Sarah Degat 01/10
Juliana Poundoko

Raphaël Ferroni 24/05
Majda Quamorchi 14/03
Ethan Azerad  15/08
Omar Bennani  
Yasmine Selmane 01/05
Thomas Simon 14/12
Marine Simon 10/01
Margot Simon 10/09
Nicola Biviano 17 / 04
Lucien Rondier 19/06
Charles Ecochard 24/02
Zachary Bouaziz 19/06
Arthur Neron 29/09
Emmanuel Berrebi 18/02
Hugo Maujoin 17/06
Eilis Connolly 11/09
Paul Bouyé 26/04
Paul Midy 21/05
Benoît Algourdin  15/12
Illian Joly 03/03
Victoria Saden 11/09
Opéhlie Rus 05/09
Clément Simon  20/11
Marvin Ivard 13 /12
Kévin Couturier 23/05
Walid Essabar  09/02
Alexis Bailly  16/09
Matteo Philip 31/05
Quentin Condon
Pierre Tenand 17/03
Victor Godfrin 20/07
Etienne Lefranc 16/09
Othmane 05/06
Maxence Laisne 06/04
Hugo Monnet
Stanislas Gauss 17/07
Heloïse Vergnole 11/04
Nicolas Saudreau 18/01
Luc Massol 28/02
Amine Cherrered 20/07
Hamza Alhyar
Louis Grosset 15/02
Alexandre Breg 06/06
Nathaniel Chauvet 29/10
Jules Teste 09/02
Paul Sheng  24/12
Julia Beyan  18/05
Matteo Beyan 09/04
Kevan Beyan 11/04
Sandrine Beyan 31/08
Philippe Beyan 14/12
Carolle Calon 01/06
Christophe Calon 10/10
Chantale Hayette 15/10
Valéry Hayette 09/06
David Menart 01/04
Corentin Ruiz 24/11
Marcel 30/03
Gisèle  25/10
Charles Calon 25/12
Cassandre Calon 06/09
Corentin Calon 08/12
clément Calon 12/06
tata Morgane 19/10
tata Sophie 14/11
Tonton Tibo 10/04
lisa Hayette 03/06
Anseis Hayette 29/11
Ismaël Hayette 03/07
Ginette Piquant 23/01
Etienne Watrin 22/09
Axel Jitten 09/05
Laurence Hayette 07/10
Lucas Lecroulant 18/05
Marraine 13/06
Irial 05/10
Elliot Degat 22/03





    import tkinter as tk
from tkinter import messagebox

messagebox.showinfo("Basic Example", "a Basic Tk MessageBox")

# 1) dict avec date et prénom en valeur
# 2) programme qui compare la date d'aujd à l'ensemble des keys du dict. S'il trouve, renvoie un messageBox pour avoir l'info

# 3) aller dans le planifiacteur de tâches pour l'exécuter de manière journalière.






#code final
d = {"david": '26/02', "mark": '23/02', "mak": '01/02', "ark": '22/09'}

# Obtenir l'heure et la date locale
now = time.localtime(time.time())
jour = time.strftime("%d/%m", now)
j = str(jour)
# On regarde si c'est lanniversaire de qqun
n = len(d)
now = time.localtime(time.time())
jour = time.strftime("%d/%m", now)
j = str(jour)

for keys in d:
    print(d[keys])
    if j == d[keys]:
        messagebox.showinfo("Anniversaire", "Anniversaire de " + '' + keys)




import time
import string


# script pour remplir le dico
import time
d = {}
x = 100
while x > 0:
    x = x-1
    p = ''
    p = input("nom")
    a = input()
    d[a] = p
    print(d)