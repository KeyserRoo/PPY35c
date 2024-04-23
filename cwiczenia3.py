import random as r


def z1():
    numbers = []
    sum, max, min, indexMin, indexMax = 0, -11, 21, 0, 0
    for i in range(20):
        element = r.randint(-10, 20)
        sum += element
        if max < element:
            max = element
            indexMax = i
        if min > element:
            min = element
            indexMin = i
        numbers.append(element)
    swap = numbers[indexMax]
    numbers[indexMax] = numbers[indexMin]
    numbers[indexMin] = swap
    print(numbers)


def z2():  #stoopid, but uses list comprehension
    pyt_triples = [(x, y, z) for x in range(1, 31) for y in range(x, 31)
                   for z in range(y, 31) if x**2 + y**2 == z**2]
    print(pyt_triples)


def z3(n):
    A = tuple(tuple(r.randint(1, 11) for _ in range(n)) for _ in range(n))

    sum_on_diagonal = 0
    for i in range(n):
        print(A[i])
        sum_on_diagonal += A[i][i]

    print(sum_on_diagonal)


def z4(n):
    A = [[-4, 0, 5], [6, 2, 2], [-3, 2, 7]]
    B = [[2, 5, 4], [10, 2, 8], [8, 1, -7]]
    boring_multiplication = []
    for i in range(n):
        A.append([])
        B.append([])
        boring_multiplication.append([])
        for j in range(n):
            a = r.randint(-5, 14)
            b = r.randint(1, 10)
            A[i].append(a)
            B[i].append(b)
            boring_multiplication[i].append(a * b)

    W = z4matrixGenerator()
    z4MatrixMultiplication(W[0], W[1])


def z4MatrixMultiplication(A, B):
    no_a_rows, no_b_rows = len(A), len(B)
    no_a_columns, no_b_columns = len(A[0]), len(B[0])
    if no_a_columns != no_b_rows:
        print("multiplication not possible!")
        return
    resultMatrix = [[] for _ in range(no_a_rows)]
    for i in range(no_b_columns):
        V = []
        for b_row in B:
            V.append(b_row[i])
        for j in range(no_a_rows):
            resultMatrix[j].append(z4DotProduct(A[j], V))
    print(resultMatrix)


def z4DotProduct(U, V):
    toReturn = 0.0
    for i in range(len(U)):
        toReturn += U[i] * V[i]
    return toReturn


def z4matrixGenerator():
    A = []
    B = []
    resheight = r.randint(3, 6)
    reswidth = r.randint(3, 6)
    samelength = r.randint(3, 6)
    for i in range(resheight):
        A.append([])
        for _ in range(samelength):
            A[i].append(r.randint(-5, 5))
    for i in range(samelength):
        B.append([])
        for _ in range(reswidth):
            B[i].append(r.randint(-5, 5))
    print(A)
    print(B)
    return [A, B]


def z5():
    pass


def z6():
    pass


def z7():
    pass


def z8():
    pass


def z9():
    pass


def z10():
    pass


def zD3a(n, x):
    if x < 1 or x > 7: return
    A = [[
        r.randint(0, x) if i - j > 0 or i + j >= n else r.randint(
            -3 * i - 1, 5 * j + 4) for j in range(n)
    ] for i in range(n)]
    for i in range(n):
        print("[ ", end="")
        for j in range(n - 1):
            print(f"{A[i][j]},\t", end="")
        print(A[i][len(A[i]) - 1], end="")
        print(" ]")
    return A


def zD3b(A, k):
    n = len(A)
    threshold = int(input("podaj prog sumy elementow: "))
    column_sums = [sum(A[i][j] for i in range(n)) for j in range(n)]

    for j in range(n):
        if column_sums[j] > threshold:
            A = [
                A[i][:j] + A[i][j + 2:j + 3] + A[i][j:j + 2] + A[i][j + 3:]
                for i in range(n)
            ]
        else:
            A = [
                A[i][:j] + A[i][j + k:j + k + 1] + A[i][j:j + k] +
                A[i][j + k + 1:] for i in range(n)
            ]
    for i in range(len(A)):
        print("[ ", end="")
        for j in range(len(A) - 1):
            print(f"{A[i][j]},\t", end="")
        print(A[i][len(A[i]) - 1], end="")
        print(" ]")
    return A


def main():
    z1()
    z2()
    z3(10)
    z4(4)
    z5()
    z6()
    z7()
    z8()
    z9()
    z10()
    A = zD3a(7, 6)
    zD3b(A, 3)


if __name__ == "__main__":
    main()
