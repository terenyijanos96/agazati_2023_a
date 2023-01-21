import ertekel
import pogyasz1
import sorozat

ertekel.ertek_bekero()
sorozat.dollar_jellel_elvalasztott_random_12_szam()
sorozat.konzol_kiir()
sorozat.fajlba_kiir()
pogyasz1.beolvas()

print(f"III/A, B:\n\tA pogyászok száma: {pogyasz1.poggyaszok_szama()}")
print(f"III/C:\n\tAz 51 cm-es pogyászok átlag súlyértéke: {pogyasz1.poggyaszok_atlag_sulya()} g")
legmagasabb = pogyasz1.legmagasabb_poggyasz_meretei()
print(f"III/D:\n\tA legmagasabb pogyász méretei: {legmagasabb.a}x{legmagasabb.b}x{legmagasabb.c}, súlya: {legmagasabb.m} kg.")
