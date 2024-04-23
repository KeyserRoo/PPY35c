import random
import math as m


def z1():
    print(random.randint(1, 100))
    print(random.randint(1, 100))
    print(random.randint(1, 100))
    print(random.randint(1, 100))
    print(random.randint(1, 100))


def z2():
    a = int(input("Podaj 1 liczbe: "))
    b = int(input("Podaj 2 liczbe: "))
    c = int(input("Podaj 3 liczbe: "))
    v_min, v_max = a, a

    if v_min > b:
        v_min = b

    if v_min > c:
        v_min = c

    if v_max < b:
        v_max = b

    if v_max < c:
        v_max = c

    print("min -> ", v_min, "\nmax -> ", v_max)


def z3p1():
    a = int(input("Podaj 1 liczbe: "))
    b = int(input("Podaj 2 liczbe: "))
    c = int(input("Podaj 3 liczbe: "))

    if a < 0 or b < 0 or c < 0:
        print("Podaj prawidlowe dane")
        return

    if (a**2 + b**2 == c**2) or (c**2 + b**2 == a**2) or (a**2 + c**2 == b**2):
        print("Jest 3 pitagorejska")
    else:
        print("Nie jest")


def z3p2():
    print("dla rownania ax^2 + bx + c = 0:")
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    c = int(input("Podaj c: "))

    if a == 0:
        print("to nie jest rownanie kwadratowe")
        return

    delta = m.pow(b, 2) - 4 * a * c

    if delta > 0:
        x1 = (-b - m.sqrt(delta)) / (2 * a)
        x2 = (-b + m.sqrt(delta)) / (2 * a)

        print("\n\ndelta -> ", delta)
        print("Pierwiastki rownania to:")
        print("x1 -> ", x1)
        print("x2 -> ", x2)

    elif delta == 0:
        x = (-b) / (2 * a)

        print("\n\ndelta -> ", delta)
        print("Pierwiastek rownania to:")
        print("x -> ", x)

    else:
        print("nie ma rozwiazan")
        return


def z4():
    for i in range(11):
        print("y = ", 3 * i)


def z5():
    for item1 in range(1, 101):
        for item2 in range(1, 101):
            print(item1, " * ", item2, " : ", item1 * item2)


def z6():
    counter = 0
    for number in range(1000, 10000):
        if (m.pow((number - number % 100) / 100, 2) +
                m.pow(number % 100, 2) == number):
            print(
                m.pow((number - number % 100) / 100, 2) +
                m.pow(number % 100, 2))
            counter += 1
    print(counter)


def z7List():
    k = int(input("podaj k"))
    A = [1, 2]
    for i in range(2, k):
        A.append(3 * A[i - 1] + A[i - 2])
    print(A)


def z7Variable():
    k = int(input("podaj k"))
    a = 1
    b = 2
    for item in range(k - 2):
        temp = a
        a = b
        b = 3 * a + temp
        print(temp)
    print(a)
    print(b)


def z8():
    epsilon = 1.0e-8
    x = float(input("Podaj x"))
    x = x % (2 * m.pi)
    sin_x = 0
    k = 0
    term = x
    while abs(term) >= epsilon:
        sin_x += term
        k += 1
        term = (-1)**k * x**(2 * k + 1) / m.factorial(2 * k + 1)
    print(sin_x)
    print(m.sin(x))


def z9List():
    A = [1.0]
    index = 0
    while (4 * index + 2) / (index + 2) * A[index] < 1000000:
        A.append((4 * index + 2) / (index + 2) * A[index])
        index += 1

    even = 0
    odd = 0
    for item in A:
        if item % 2 == 0:
            even += 1
        else:
            odd += 1

    print(A)
    print("Even:", even)
    print("Odd:", odd)


def zZD2():
    X = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    k = int(input("Prosze wprowadzic ile chcesz podac liczb:"))
    Y = []
    if k < 0 and k > 10:
        print("Ale daj z przedzialu 1-9 :P")
        return
    for item in range(k):
        Y.append(int(input(f"Prosze wprowadzic {item} liczbe:")))
    for x in X:
        for y in Y:
            funkcjaZD2(x, y)


def funkcjaZD2(x, y):
    sum = 0.0
    if m.sin(x) > m.cos(y):
        for item in range(1, 11):
            sum += m.pow(x + y, item) / m.factorial(item)
    else:
        sum = m.pow(x, 5) + m.pow(x, 3) * m.pow(y, 2) * m.pow(x, 4)
    print(f"f({x},{y}) = {sum}")


def main():
    z1()
    z2()
    z3p1()
    z3p2()
    z4()
    z5()
    z6()
    z7List()
    z7Variable()
    z8()
    z9List()
    zZD2()


if __name__ == '__main__':
    main()
