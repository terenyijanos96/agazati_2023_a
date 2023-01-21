def ertek_bekero():
    print("I/A, B:")
    etel_neve = input("\tÉtel neve: ")
    rendelo_neve = input("\tÉtel rendelőjének neve: ")
    ertekeles = int(input("\tÉrtékelés (1-5): "))

    print("I/C:\n\t", end="")

    if ertekeles < 0:
        print("Az értékelés nem lehet negatív!")
    elif ertekeles > 5:
        print("5 pont feletti értékelés nem elfogadható!”!")
    elif 1 <= ertekeles <= 5:
        print("Köszönjük az értékelést!")
