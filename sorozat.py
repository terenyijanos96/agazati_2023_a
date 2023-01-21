import random

lista = []
def dollar_jellel_elvalasztott_random_12_szam():
    i = 0
    print("II/A, B, C:\n\t", end="")
    szoveg = ""
    while i < 12:
        vel = int(random.random() * 1011) - 10
        szoveg += f'{vel}{"$" if i < 11 else ""}'
        lista.append(vel)
        i+=1

    print(szoveg)

def paratlanok_szama():
    i = 0
    db = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            db+=1
        i+=1

    return db

def konzol_kiir():
    print("II/D, E:\n\tA páratlanok száma:", str(paratlanok_szama()) + ".")

def fajlba_kiir():
    fajlom = open("eredmeny.txt", "w", encoding="utf-8")
    fajlom.write(f"II/F:\n\tA páratlanok száma: {paratlanok_szama()}.")
    fajlom.close()