import math

def oblicz_pole_kola(promien:float):
    return ((math.pow(promien,2))*math.pi)

def oblicz_pole_prostokota(a:float, b:float):
    return a * b

def oblicz_pole_trojkota(a:float, b:float, c:float):
    p = (a + b + c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def oblicz_pole_figury(tablica_danych_figury):
    match len(tablica_danych_figury):
        case 1:
            return oblicz_pole_kola(float(tablica_danych_figury[0]))
        case 2:
            return oblicz_pole_prostokota(float(tablica_danych_figury[0]), float(tablica_danych_figury[1]))
        case 3:
            return oblicz_pole_trojkota(float(tablica_danych_figury[0]), float(tablica_danych_figury[1]), float(tablica_danych_figury[2]))
        case _:
            print("Nieprawidłowa dane")

ilosc_figur = int(input("Podaj liczbe figur: "))
suma_pol_figur = 0
for i in range(ilosc_figur):
    dane_figury = input()
    tablica_danych_figury = dane_figury.split()
    if len(tablica_danych_figury) > 3:
       print("Błąd: można podać maksymalnie 3 liczby")
       exit()
    suma_pol_figur += oblicz_pole_figury(tablica_danych_figury)
print(round(suma_pol_figur,2))

