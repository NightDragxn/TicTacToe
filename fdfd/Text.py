import random

Computer_wahl = random.randint(1, 3)

if Computer_wahl == 1:
    Computer_wahl = "Schere"

elif Computer_wahl == 2:
    Computer_wahl = "Stein"
else: 
    Computer_wahl = "Papier"

print(Computer_wahl)

if input("Schere") & Computer_wahl == 1:
    print("sieg")
