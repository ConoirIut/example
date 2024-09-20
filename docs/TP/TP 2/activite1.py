from PIL import Image                   # utilisation d'une bibliothèque spécialisée pour l'image

img = Image.open("pomme.jpg")           # ouverture du fichier

r,v,b=img.getpixel((100,250))           # code R V B du pixel de coordonnées (100,250)

print("canal rouge : ",r,"    canal vert : ",v,"    canal bleu : ",b)     # affichage du code R V B

