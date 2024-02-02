#1. Wczytaj o użytkownika ile lubi owoców, pobieraj je w pętli i zapisz do pliku 

# ile_owocow = int(input("Ile owoców lubisz? "))

# owoc_list = []
# for i in range(ile_owocow):
#     owoc = input("Podaj nazwę owocu: ")
#     owoc_list.append(owoc)


# with open("pliki/owoce.txt", "w") as plik:
#     for owoc in owoc_list:
#         plik.write(owoc + "\n")


#2. wczytaj plik trojkat.txt w ilu wierszach zaprezentowane są dane, z których można zbudować trójkąt?

# with open("pliki/trojkat.txt", "r") as plik:
#     dane = plik.readlines()
#     liczba_wierszy = len(dane)
#     print(liczba_wierszy)

#3. wczytaj dane z pliku anagramy.txt, a następnie oblicz w ilu linijkach są anagramy - słowa, w których są te same litery w innej kolejności, na ekranie wyświetl linijki z anagramami oraz zsumuj ich liczbę i wyświetl. 
    
# with open("pliki/anagramy.txt", "r") as plik:
#     wiersze = [wiersz.strip() for wiersz in plik.readlines()]

# liczba_anagramów = 0
# anagramy = []

# for wiersz in wiersze:
#     posortowany_wiersz = ''.join(sorted(wiersz))
#     if posortowany_wiersz in anagramy:
#         continue
#     anagramy.append(posortowany_wiersz)
#     liczba_anagramów += 1

# print(f"Liczba anagramów: {liczba_anagramów}")

#4. w pliku temperatury.txt są dane pomiarowe z kilkunastu dni. Sprawdź przy pomocy programu komputerowego, dla ilu dni wynik jest powyżej i równy zero, a dla ilu poniżej. Wyświetl na ekranie

# with open("pliki/temperatury.txt", "r") as plik:
#     dane = plik.readlines()
    
#     wynik_powyzej_zero = len([temp for temp in dane if int(temp) >= 0])
#     wynik_ponizej_zero = len([temp for temp in dane if int(temp) < 0])
#     print(f"Ilość dni z wynikiem powyżej lub równym zero: {wynik_powyzej_zero}")
#     print(f"Ilość dni z wynikiem poniżej zera: {wynik_ponizej_zero}")