import math
import random


def zadanie1():
    x = int(input("Podaj x: "))
    first_number = None
    second_number = None
    count = 0

    while True:
        number = int(input("Podaj liczbę: "))
        if first_number is None:
            first_number = number
        elif second_number is None:
            second_number = number
        else:
            if number == first_number and second_number == number:
                break
            first_number, second_number = second_number, number

        if 10 <= number <= 99 and number % x == 0:
            count += 1

    print(
        f"Liczba wczytanych liczb dwucyfrowych podzielnych przez {x}: {count}")


def zadanie2():
    x = int(input("Podaj x: "))
    first_number = None
    second_number = None
    condition = True
    sum_numbers = 0
    count = 0
    while condition:
        inp = int(input("Wprowadz liczbe: "))
        if first_number is None:
            first_number = inp
        elif second_number is None:
            second_number = inp
        else:
            if (inp == first_number
                    and second_number == inp) or (inp == second_number
                                                  and first_number == inp):
                condition = False
            else:
                first_number, second_number = second_number, inp
        if inp % x == 0:
            sum_numbers += inp
            count += 1
    if count > 0:
        average = sum_numbers / count
        print(f"Średnia arytmetyczna z liczb podzielnych przez {x}: {average}")
    else:
        print("Nie znaleziono liczb podzielnych przez x.")


def zadanie3():
    first_number = float(input("Wprowadz pierwszą liczbę: "))
    second_number = float(input("Wprowadz drugą liczbę: "))
    sum_first_two = first_number + second_number
    sum_current_two = 0
    max_abs_value = max(abs(first_number), abs(second_number))
    positive_sum = 0
    positive_count = 0
    while sum_current_two <= sum_first_two:
        current_number = float(input("Wprowadz kolejną liczbę: "))
        sum_current_two += current_number
        if current_number > 0:
            positive_sum += current_number
            positive_count += 1
        max_abs_value = max(max_abs_value, abs(current_number))
    if positive_count > 0:
        average_positive = positive_sum / positive_count
        print(
            f"Największa liczba co do wartości bezwzględnej: {max_abs_value}")
        print(f"Średnia arytmetyczna liczb dodatnich: {average_positive}")
    else:
        print("Nie znaleziono liczb dodatnich.")


def zadanie4():
    first_char = None
    second_char = None
    total_chars = 0
    other_chars = 0
    while True:
        char = input("Wprowadź znak: ")
        if first_char is None:
            first_char = char
        elif second_char is None:
            second_char = char
        else:
            if (char == first_char
                    and second_char == char) or (char == second_char
                                                 and first_char == char):
                break
            first_char, second_char = second_char, char
        total_chars += 1
        if char not in [first_char, second_char]:
            other_chars += 1
    if total_chars > 0:
        percentage = (other_chars / total_chars) * 100
        print(f"Procentowy udział innych znaków: {percentage}%")
    else:
        print("Nie wprowadzono żadnych znaków.")


def zadanie5():
    first_word = None
    second_word = None
    condition = True
    total_letters = 0
    e_count = 0
    d_count = 0
    while condition:
        word = input("Wprowadź napis: ")
        if first_word is None:
            first_word = word
        elif second_word is None:
            second_word = word
        else:
            if (word == first_word
                    and second_word == word) or (word == second_word
                                                 and first_word == word):
                condition = False
            else:
                first_word, second_word = second_word, word
        if total_letters >= 10:
            condition = False
        total_letters += len(word)
        if not any(char.isupper() for char in word):
            e_count += word.count('e')
            d_count += word.count('d')
    print(f"Całkowita liczba liter 'e': {e_count}")
    print(f"Całkowita liczba liter 'd': {d_count}")


def zadanie6():
    n = int(input("Podaj n: "))
    first_number = None
    second_number = None
    third_number = None
    condition = True
    count = 0
    total = 0
    while condition:
        number = int(input("Wprowadź liczbę: "))
        if first_number is None:
            first_number = number
        elif second_number is None:
            second_number = number
        else:
            if (number == first_number and second_number == third_number) or (
                    number == second_number and first_number == third_number):
                condition = False
            else:
                first_number, second_number, third_number = second_number, third_number, number
        if count >= n:
            condition = False
        if number > n and (number % 2 == 0 or number % 5 == 0):
            total += 1
        count += 1
    print(
        f"Całkowita liczba wartości większych od {n} i podzielnych przez 2 lub 5: {total}"
    )


def zadanie7():
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    n = int(input("Podaj n: "))
    if a >= b:
        print("Wartość a musi być mniejsza od b.")
        return
    count = 0
    total = 0
    while count < n:
        number = int(input("Wprowadź liczbę: "))
        if a < number < b:
            print("Liczba musi być spoza zakresu <a, b>.")
            continue
        if number < 0 and number % 2 == 0:
            total += number
        count += 1
    print(f"Suma ujemnych liczb podzielnych przez 2: {total}")


def zadanie8():
    k = int(input("Podaj k: "))
    first_number = None
    second_number = None
    condition = True
    total = 0
    count = 0
    while condition:
        number = int(input("Wprowadź liczbę: "))
        if first_number is None:
            first_number = number
        elif second_number is None:
            second_number = number
        else:
            if (number == first_number and second_number == number) or (
                    number == second_number and first_number == number):
                condition = False
            else:
                first_number, second_number = second_number, number
        if count >= k:
            condition = False
        if number < 0 and number % 2 == 0:
            total += number
        count += 1
    print(f"Suma ujemnych liczb podzielnych przez 2: {total}")


def zadanie9():
    first_word = None
    second_word = None
    third_word = None
    condition = True
    total_letters = 0
    t_count = 0
    k_count = 0
    while condition:
        word = input("Wprowadź napis: ")
        if first_word is None:
            first_word = word
        elif second_word is None:
            second_word = word
        else:
            if (word == first_word
                    and second_word == word) or (word == second_word
                                                 and first_word == word):
                condition = False
            else:
                first_word, second_word, third_word = second_word, third_word, word
        if total_letters >= 7:
            condition = False
        total_letters += len(word)
        if any(char.isupper() for char in word):
            t_count += word.count('t')
            k_count += word.count('k')
    print(f"Całkowita liczba liter 't': {t_count}")
    print(f"Całkowita liczba liter 'k': {k_count}")


def zadanie11(K):
    n = 5
    M = 10
    A = [[''] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            while True:
                word = input(f"Wprowadź napis dla A[{i}][{j}]: ")
                if len(word) <= M and word[0].islower() and word[-1].islower():
                    A[i][j] = word
                    break
                else:
                    print(
                        "Napis musi mieć nie więcej niż M znaków i zaczynać i kończyć się małą literą."
                    )

    print("Tablica A przed przesunięciem:")
    for row in A:
        print(' '.join(row))

    for i in range(n):
        if i % 2 == 0 and len(A[i][0]) > len(A[i][-1]):
            A[i] = A[i][1:] + A[i][:1]
        elif i % 2 != 0 and len(A[i][-1]) > K:
            A[i] = A[i][-1:] + A[i][:-1]

    print("Tablica A po przesunięciu:")
    for row in A:
        print(' '.join(row))


def zadanie12():
    n = 5
    X = 6
    K = 2
    A = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                A[i][j] = random.uniform(2 * j, 4 * (j + 1) + 5)
            else:
                A[i][j] = random.uniform(0, X)

    print("Tablica A przed przesunięciem:")
    for row in A:
        print(' '.join(map(str, row)))

    for j in range(n):
        if A[0][j] < A[-1][j]:
            A = [row[j:] + row[:j] for row in A]
        else:
            A = [row[-K:] + row[:-K] for row in A]

    print("Tablica A po przesunięciu:")
    for row in A:
        print(' '.join(map(str, row)))


def zadanie13_a(n, M):
    A = [[''] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            while True:
                word = input(f"Wprowadź napis dla A[{i}][{j}]: ")
                if len(word) <= M and word[0].isupper() and word[-1].isupper():
                    A[i][j] = word
                    break
                else:
                    print(
                        "Napis musi mieć nie więcej niż M znaków i zaczynać i kończyć się dużą literą."
                    )

    return A


def zadanie13_b(A, n):
    for i in range(n):
        if i % 2 == 0 and len(A[i][0]) > len(A[i][-1]):
            A[i] = A[i][1:] + A[i][:1]
        elif i % 2 != 0 and len(A[i][-1]) > len(A[i][0]):
            A[i] = A[i][-1:] + A[i][:-1]

    return A


def zadanie13_c(A):
    print("Tablica A przed przesunięciem:")
    for row in A:
        print(' '.join(row))

    print("Tablica A po przesunięciu:")
    for row in A:
        print(' '.join(row))


def zadanie14_a(n, X):
    A = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i < j:
                A[i][j] = random.uniform(-3 * i + 1, 5 * j + 4)
            else:
                A[i][j] = random.uniform(0, X)

    return A


def zadanie14_b(A, n, K, user_sum):
    for j in range(n):
        column_sum = sum(A[i][j] for i in range(n))
        if column_sum > user_sum:
            A = [row[j:] + row[:j] for row in A]
        else:
            A = [row[-K:] + row[:-K] for row in A]

    return A


def zadanie14_c(A):
    print("Tablica A przed przesunięciem:")
    for row in A:
        print(' '.join(map(str, row)))

    print("Tablica A po przesunięciu:")
    for row in A:
        print(' '.join(map(str, row)))


def zadanie15(n):
    A = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i < j:
                A[i][j] = random.uniform(2 * i - 4, 4 * j + 5)
            else:
                A[i][j] = random.uniform(0, 6)

    for i in range(n):
        for j in range(n):
            if i < j:
                x = A[i][j]
                if x <= 5:
                    A[i][j] = x**3 + x**2 - 5 * x
                else:
                    A[i][j] = math.cos(x)

    for i in range(n):
        A[i] = A[i][1:] + A[i][:1]
        A[i] = A[i][:-1] + A[i][0]

    print("Tablica A po przesunięciu:")
    for row in A:
        print(' '.join(map(str, row)))


def zadanie16(n, a, b):
    A = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i < j:
                A[i][j] = random.randint(a, b)
            else:
                A[i][j] = random.randint(0, 6)

    for i in range(n):
        for j in range(n):
            if i < j:
                x = A[i][j]
                if x > -4:
                    A[i][j] = x**2 - 3 * x
                else:
                    A[i][j] = 1 / (math.sin(x) + 4)

    B = list(map(list, zip(*A)))

    for i in range(n):
        A[i] = A[i][4:] + A[i][:4]
        A[i] = A[i][-4:] + A[i][:-4]

    print("Tablica A po przesunięciu:")
    for row in A:
        print(' '.join(map(str, row)))

    print("Tablica B po transpozycji:")
    for row in B:
        print(' '.join(map(str, row)))


def main():
    zadanie1()
    zadanie2()
    zadanie3()
    zadanie4()
    zadanie5()
    zadanie6()
    zadanie7()
    zadanie8()
    zadanie9()
    zadanie11(7)
    zadanie12()

    n = 5
    M = 10
    X = 6
    K = 2
    user_sum = 10

    A = zadanie13_a(n, M)
    A = zadanie13_b(A, n)
    zadanie13_c(A)

    A = zadanie14_a(n, X)
    A = zadanie14_b(A, n, K, user_sum)
    zadanie14_c(A)

    zadanie15(n)
    zadanie16(n,M,X)


if __name__ == "__main__":
    main()
