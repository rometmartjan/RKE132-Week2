#Alusta programmi
#Küsi kasutajalt, mitu klaasi vett ta juba täna joonud on
#Arvuta protsent, mille see moodustab soovituslikust kogusest
#Kui protsent < 50: väljasta: „Joo rohkem vett, keha vajab seda!“
#Kui protsent < 100: väljasta: „Tubli, jätka samas vaimus!“
#Kui protsent ≥ 100: väljasta: „Suurepärane, oled oma päevase eesmärgi täitnud!“
#Programmi lõpp

glasses = int(input("Mitu klaasi vett sa juba täna joonud oled?: "))
percent = glasses/8*100

if percent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif percent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud")