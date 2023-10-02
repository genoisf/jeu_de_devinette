#créé par Francis Genois
#créé en 2023
#tp2 jeu de devinette
from random import *
# je défénis les bornes de le devinette
def bornes():
    a = int(input('quel est le minimum de la devienette?'))
    b = int(input('quel est le maximum de la devienette?'))
    print("j'ai choisi un nombre entre %d et %d. À vous de le deviner..." % (a, b))
    c = randint(a, b)
    return c

devinette = "oui"
# je crée ma boucle
while devinette == "oui":
    # je défénis mes variables
    tentatives = 0
    essai = None
    c = bornes()
    # je crée ma boucle
    while essai != c:
        tentatives = tentatives + 1
        essai = int(input("Entrez votre essai:"))
        # réponse trop grande
        if essai > c:
            print('votre réponse est trop grande')
        # réponse trop petite
        elif c > essai:
            print('votre réponse est trop petite')
    #si vous avez la bonne réponse
    print("Bravo! bonne réponse")
    print("Vous avez réussi en %d tentatives" %(tentatives))
    #si vous voulez rejouer
    devinette = str(input("voulez vous réessayer? oui ou non?"))