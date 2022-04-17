import os

# input et creation de la liste
os.system('clear')
testlist = input("Mot a tester : ")
laListe = list(testlist)
indexlistIncrease = 0

# fonction de suppresion de blank space

for test in range(len(testlist)) :
    if laListe[indexlistIncrease] == " " :
        laListe.remove(laListe[indexlistIncrease])
    else :
        indexlistIncrease += 1

# recomoilation en variable et print

test = ''.join(laListe)
print(test)