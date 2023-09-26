hadane_cislo = randint (1, 101)
cislo = input

if hadane_cislo == cislo:
    print('Gratulujeme, uhádli jste číslo')
elif hadane_cislo > cislo:
    print(cislo, 'je větší než hádané číslo')
elif hadane_cislo < cislo:
    print(cislo,'je menší než hádané číslo')

