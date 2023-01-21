from Poggyasz import *
lista_poggyasz = []

def beolvas():
    fajlom = open("csomag.txt", "r", encoding="utf-8")
    fejlec, tartalom = fajlom.readline(), fajlom.readlines()
    fajlom.close()

    i = 0
    while i < len(tartalom):
        sor = tartalom[i].strip().split("#")
        lista_poggyasz.append(Poggyasz(sor))
        i+=1

def poggyaszok_szama():
    return len(lista_poggyasz)

def poggyaszok_atlag_sulya():
    i = 0
    db = 0
    osszeg = 0

    while i < len(lista_poggyasz):
        if lista_poggyasz[i].a == 51:
            db+=1
            osszeg += lista_poggyasz[i].m
        i+=1

    return int((osszeg / db) * 1000)

def legmagasabb_poggyasz_meretei():
    maximum_index = 0
    i = 1
    while i < len(lista_poggyasz):
        if lista_poggyasz[maximum_index].b < lista_poggyasz[i].b:
            maximum_index = i
        i+=1
    return lista_poggyasz[maximum_index]

