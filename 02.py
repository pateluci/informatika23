from random import randint
cislo = int(input("hadejte cislo "))
hadane_cislo = randint (1, 100)


while hadane_cislo != cislo:
    if hadane_cislo < cislo:
        print(cislo, 'je větší než hádané číslo')
        cislo = int(input("hadejte cislo "))
    elif hadane_cislo > cislo:
        print(cislo, 'je menší než hádané číslo')
        cislo = int(input("hadejte cislo "))
    

print(cislo, 'je hádané číslo, gratulujeme.')