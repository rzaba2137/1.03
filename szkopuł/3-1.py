# Zadanie 1PNK – Papier Nożyce Kamień
# Antek i Arek grają w grę papier nożyce i kamień.
# Gra polega na tym, że każdy z nich w tym samym momencie
# pokazuje ręką jeden z trzech symboli – papier, nożyce lub kamień.

# Funkcja do sprawdzania wyniku gry
def check_game_result(antek, arek):
    if antek == arek:
        return "REMIS"
    elif (antek == 1 and arek == 2) or \
         (antek == 2 and arek == 3) or \
         (antek == 3 and arek == 1):
        return "ANTEK"
    else:
        return "AREK"

# Wejście
antek_gesture, arek_gesture = map(int, input().split())

# Wyjście
print(check_game_result(antek_gesture, arek_gesture))