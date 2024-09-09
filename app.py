class Film:
    def __init__(self):
        self._tytul = ""
        self._liczba_wypozyczen = 0


    def set_tytul(self, tytul):
        if len(tytul) <= 20:
            self._tytul = tytul
        else:
            print("Tytuł może mieć maksymalnie 20 znaków.")

    def get_tytul(self):
        return self._tytul

    def get_liczba_wypozyczen(self):
        return self._liczba_wypozyczen

    def inkrementuj_wypozyczenia(self):
        self._liczba_wypozyczen += 1


film = Film()
print(f"Tytuł początkowy: {film.get_tytul()}")
print(f"Liczba wypożyczeń początkowa: {film.get_liczba_wypozyczen()}")

film.set_tytul("Incepcja")
print(f"Ustawiony tytuł: {film.get_tytul()}")

print(f"Liczba wypożyczeń przed inkrementacją: {film.get_liczba_wypozyczen()}")
film.inkrementuj_wypozyczenia()
print(f"Liczba wypożyczeń po inkrementacji: {film.get_liczba_wypozyczen()}")


film.inkrementuj_wypozyczenia()
print(f"Liczba wypożyczeń po kolejnej inkrementacji: {film.get_liczba_wypozyczen()}")
