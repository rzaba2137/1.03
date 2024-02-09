ile_ocen = int(input("Ile ocen wypisać?: "))

ocena_list = []
for _ in range(ile_ocen):
    ocena = input("Podaj ocenę: ")
    ocena_list.append(ocena)

with open("pliki/ocena.txt", "w") as plik:
    for ocena in ocena_list:
        plik.write(ocena + "\n")

with open("pliki/ocena.txt", "r") as plik:
    oceny = plik.read().split()

print(oceny)