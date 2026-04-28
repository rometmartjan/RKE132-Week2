#Alusta programmi
#Küsi kasutajalt tema perekonnanime
#Salvesta vastus muutujasse last_name
#Küsi kasutajalt tema sugu
#Salvesta vastus muutujasse gender
#Kui gender on võrdne sõnaga "m", siis väljasta: „Tere, härra [Perekonnanimi]!“
#Kui gender on võrdne sõnaga "n", siis väljasta: „Tere, proua [Perekonnanimi]!“
#Kui kasutaja sisestab midagi muud, väljasta: „Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis).“
#Programmi lõpp

last_name = input("Mis on sinu perekonnanimi?: ")
gender = input("Mis on sinu sugu? (vali 'm' või 'n'): ")

if gender == "m":
    print("Tere, härra " + last_name + "!")
elif gender == "n":
    print("Tere, proua " + last_name + "!")
else:
    print("Tere tulemast, " + last_name + "! (sugu ei olegi tähtis).")

