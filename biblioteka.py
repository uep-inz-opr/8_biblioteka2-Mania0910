from asyncio.windows_events import NULL
from multiprocessing.spawn import import_main_path

from xmlrpc.client import boolean

class Ksiazka:
    def __init__(self, tytul: str, autor: str):
        self.tytul = tytul
        self.autor = autor
        self.liczba_egzemplarzy = 0


class Egzemplarz:
    def __init__(self, rok_wydania: str, ksiazka: Ksiazka):
        self.rok_wydania = rok_wydania
        self.wypozyczony = False
        self.ksiazka = ksiazka

class Biblioteka:
    def __init__(self, limit_wypozyczen):
        self.limit_wypozyczen = limit_wypozyczen
        self.egzemplarze = []
        self.ksiazki = []

    def dodaj_egzemplarz_ksiazki(self, tytul: str, autor: str, rok_wydania: int):
        ksiazka = self.znajdz_ksiazke(tytul, autor)
        if ksiazka == NULL:
            ksiazka = Ksiazka(tytul, autor)
            self.ksiazki.append(ksiazka)
        self.egzemplarze.append(Egzemplarz(rok_wydania, ksiazka))
        ksiazka.liczba_egzemplarzy += 1
        # self.egzemplarze.append(Egzemplarz(rok_wydania, Ksiazka(tytul, autor)))

    def znajdz_ksiazke(self, tytul: str, autor: str):
        for ksiazka in self.ksiazki:
            if ksiazka.tytul == tytul and ksiazka.autor == autor:
                return ksiazka
        return NULL

    def wyswietl_ksiazki(self):
        self.ksiazki.sort(key=lambda x: x.tytul, reverse=False)
        for ksiazka in self.ksiazki:
            krotka_ksiazki = (ksiazka.tytul, ksiazka.autor, ksiazka.liczba_egzemplarzy)
            print(krotka_ksiazki)

biblioteka = Biblioteka(3)
liczba_egzemplarzy = int(input("Podaj liczbę egzemplarzy: "))
for i in range(liczba_egzemplarzy):
    krotka_ezgemplarza = eval(input("Podaj ezgemplarz książki: "))
    biblioteka.dodaj_egzemplarz_ksiazki(krotka_ezgemplarza[0], krotka_ezgemplarza[1], krotka_ezgemplarza[2])
biblioteka.wyswietl_ksiazki()