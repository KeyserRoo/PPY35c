import random


def z1():
    def dodaj(a, b):
        return a + b

    def odejmij(a, b):
        return a - b

    def mnoz(a, b):
        return a * b

    def dziel(a, b):
        if b != 0:
            return a / b
        else:
            return "B musi być różne od zera"

    a = float(input("Podaj liczbę a: "))
    b = float(input("Podaj liczbę b: "))

    print("Dodawanie:", dodaj(a, b))
    print("Odejmowanie:", odejmij(a, b))
    print("Mnożenie:", mnoz(a, b))
    print("Dzielenie:", dziel(a, b))


def z2():
    def kelvin_to_celsius(TK):
        if TK < 0:
            return None
        else:
            return TK - 273.15

    TK = float(input("Podaj temperaturę w Kelwinach: "))
    TC = kelvin_to_celsius(TK)
    print("Temperatura w stopniach Celsjusza:", TC)


def z3():
    def silnia_iteracyjnie(n):
        silnia = 1
        for i in range(1, n + 1):
            silnia *= i
        return silnia

    def silnia_rekurencyjnie(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * silnia_rekurencyjnie(n - 1)

    n = int(input("Podaj liczbę: "))
    print("Silnia iteracyjnie:", silnia_iteracyjnie(n))
    print("Silnia rekurencyjnie:", silnia_rekurencyjnie(n))


def z4():
    def najmniejszy_najwiekszy(sekwencja):
        min_index, min_value = min(enumerate(sekwencja), key=lambda x: x[1])
        max_index, max_value = max(enumerate(sekwencja), key=lambda x: x[1])
        return min_index, min_value, max_index, max_value

    lista = [random.randint(-100, 100) for _ in range(15)]
    print("Lista:", lista)
    min_index, min_value, max_index, max_value = najmniejszy_najwiekszy(lista)
    print("Najmniejszy element: indeks {}, wartość {}".format(
        min_index, min_value))
    print("Największy element: indeks {}, wartość {}".format(
        max_index, max_value))


def z5():
    def najwieksze_wartosci_kolumny(a):
        """Zwraca wektor zawierający największe wartości każdej kolumny."""
        return [max(row) for row in zip(*a)]

    def zamien_kolumny(a, i, j):
        """Zamienia miejscami dwie kolumny w tablicy."""
        for row in a:
            row[i], row[j] = row[j], row[i]

    def wstaw_najwieksza_wartosc(a, b):
        """Wstawia do każdego wiersza tablicy a innej wartości w miejsce elementu o największej wartości."""
        for i, row in enumerate(a):
            max_index = row.index(max(row))
            a[i][max_index] = b[i]

    w = int(input("Podaj wartość w: "))
    k = int(input("Podaj wartość k: "))

    a = [[random.randint(-15, 15) for _ in range(k)] for _ in range(w)]
    b = [random.randint(-20, 20) for _ in range(w)]

    print("Tablica a:")
    for row in a:
        print(row)

    print("\nTablica b:")
    for row in b:
        print(row)

    najwieksze_wartosci = najwieksze_wartosci_kolumny(a)
    print("\nNajwiększe wartości każdej kolumny:", najwieksze_wartosci)

    zamien_kolumny(a, 0, 1)
    print("\nTablica a po zamianie kolumn:")
    for row in a:
        print(row)

    wstaw_najwieksza_wartosc(a, b)
    print("\nTablica a po wstawieniu nowych wartości:")
    for row in a:
        print(row)


def z6():
    n = int(input("Podaj rozmiar tablic: "))
    a = [[float(input()) for _ in range(n)] for _ in range(n)]
    b = [[float(input()) for _ in range(n)] for _ in range(n)]
    c = [[float(input()) for _ in range(n)] for _ in range(n)]


def z7():
    n = int(input("Podaj liczbę odcinków: "))
    A = [[float(input()), float(input())] for _ in range(n)]
    B = [[float(input()), float(input())] for _ in range(n)]


def z4D():
    class Samochod:
        def __init__(self, marka, rok, cena):
            self.marka = marka
            self.rok = rok
            self.cena = cena

    def z4Dwczytaj_dane(n):
        tablica = []
        for _ in range(n):
            wiersz = []
            for _ in range(n):
                marka, rok, cena = input(
                    "Podaj odzielone spacjami markę, rok i cenę samochodu: "
                ).split()
                wiersz.append(Samochod(marka, int(rok), float(cena)))
            tablica.append(wiersz)
        return tablica

    def z4Dzwiększ_ceny(tablica, n):
        for j in range(n - 1):
            najmłodsza_cena = min(tablica[i][j].cena for i in range(1, n)
                                  if tablica[i][j].rok > tablica[0][j].rok)
            for i in range(n):
                if tablica[i][j].cena < tablica[i][0].cena:
                    tablica[i][j].cena += najmłodsza_cena

    def z4Ddrukuj_dane(tablica, n):
        for i in range(n):
            for j in range(n):
                if 'f' not in tablica[i][j].marka and 'z' not in tablica[i][
                        j].marka:
                    print(tablica[i][j].marka, tablica[i][j].rok,
                          tablica[i][j].cena)

    def z4Dzwiększ_ceny_najtanszych(tablica, n):
        A = []
        for i in range(len(tablica)):
            for j in range(len(tablica[i])):
                if i == j or i + j == n - 1:
                    A.append([tablica[i][j], i, j])
        najtansze = sorted(A, key=lambda x: x[0].cena)[:2]
        for car, i, j in najtansze:
            tablica[i][j].cena *= 1.15

    n = int(input("Podaj rozmiar tablicy: "))
    tablica1 = z4Dwczytaj_dane(n)
    tablica2 = z4Dwczytaj_dane(n)

    z4Dzwiększ_ceny(tablica1, n)
    z4Dzwiększ_ceny(tablica2, n)

    z4Ddrukuj_dane(tablica1, n)
    z4Ddrukuj_dane(tablica2, n)

    z4Dzwiększ_ceny_najtanszych(tablica1, n)
    z4Dzwiększ_ceny_najtanszych(tablica2, n)


def main():
    z1()
    z2()
    z3()
    z4()
    z5()
    z6()
    z7()
    z4D()


if __name__ == "__main__":
    main()
