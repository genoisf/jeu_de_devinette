#créé par Francis Genois
#créé en 2023
#tp2 jeu de devinette

# je défénis mes variables
from random import*
loop = 1
tentatives = 1

# je défénis les bornes de le devinette
def bornes():
    a = int(input('quel est le minimum de la devienette?'))
    b = int(input('quel est le maximum de la devienette?'))
    print("j'ai choisi un nombre entre %d et %d. À vous de le deviner..." %(a, b))
    c = randint(a,b)
    return c
c = bornes()

# je crée ma boucle
while loop == 1:
    essai = int(input("Entrez votre essai:"))
    if essai == c:
        print("Bravo! bonne réponse")
        print("Vous avez réussi en %d tentatives" %(tentatives))
        loop = loop + 1

    else:
        print("mauvaise réponse")
        tentatives = tentatives + 1
        if essai > c:
            print('votre réponse est trop grande')
        else:
            print('votre réponse est trop basse')