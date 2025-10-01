import nrrd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
nazwa_pliku = 'skull.nrrd'
def konwo(przekroj, filtr):
    wyostrzony = np.array(przekroj)
    for x in range(0, przekroj.shape[0] - filtr.shape[0] + 1):
        for y in range(0, przekroj.shape[1] - filtr.shape[1] + 1):
            wyostrzony[x+1, y+1] = np.sum(przekroj[x:x+filtr.shape[0],
            y:y+filtr.shape[1]] * filtr)
    return wyostrzony

obraz, naglowek = nrrd.read(nazwa_pliku)
print(naglowek)
print(obraz.shape)

#Generowanie obrazu bezfiltrowe
rys, osie = plt.subplots(ncols=5, nrows=2, constrained_layout=True)
i = 0
for os in osie.flatten():
    os.imshow(obraz[i, :, :], cmap=plt.cm.gray, vmin=0, vmax=255)
    os.set_xticks([])
    os.set_yticks([])
    i += obraz.shape[0] // len(osie.flatten())
plt.savefig('zuchwa_bez_filtru.png')

#Generowanie obrazu z filtrem
filtr1 = np.array([[-1/8, 1/4, -1/8],
[1/4, 2, 1/4],
[-1/8, 1/4, -1/8]])
rys, osie = plt.subplots(ncols=5, nrows=2, constrained_layout=True)
i = 0
cmap = ListedColormap(["black","white",  "red", "white"])
for os in osie.flatten():
    wyostrzony = konwo(obraz[i, :, :], filtr1)
    os.imshow(wyostrzony, cmap=plt.cm.gray, vmin=0, vmax=255)
    os.set_xticks([])
    os.set_yticks([])
    i += obraz.shape[0] // len(osie.flatten())
plt.savefig('zuchwa_filtr1.png')



filtr2 = np.array([[1/4, 1/4, 1/4],
[1/4, 1, 1/4],
[1/4, 1/4, 1/4]])
rys, osie = plt.subplots(ncols=5, nrows=2, constrained_layout=True)
i = 0
for os in osie.flatten():
    wyostrzony = konwo(obraz[i, :, :], filtr2)
    os.imshow(wyostrzony, cmap=plt.cm.gray, vmin=0, vmax=255)
    os.set_xticks([])
    os.set_yticks([])
    i += obraz.shape[0] // len(osie.flatten())
plt.savefig('zuchwa_filtr2.png')

