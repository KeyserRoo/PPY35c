# def main():
#     x = 'mielonka'
#     while x:
#         print(x,end=' ')
#         x = x[1:]

#     # x = 'mielonka'			error
#     # while x:
#     #     print(x,end=' ')
#     #     x = x[-1:]
        
#     # x = 'mielonka'			error
#     # while x:
#     #     print(x,end=' ')
#     #     x = x[:1]

#     x = 'mielonka'
#     while x:
#         print(x,end=' ')
#         x = x[:-1]

# if __name__ == '__main__':
# 	main()

import random
import math as m
    
def zadanie1():
    print(random.randint(1,100))
    print(random.randint(1,100))
    print(random.randint(1,100))
    print(random.randint(1,100))
    print(random.randint(1,100))
    
def zadanie2():
    a = int(input("Podaj 1 liczbe: "))
    b = int(input("Podaj 2 liczbe: "))
    c = int(input("Podaj 3 liczbe: "))
    v_min,v_max = a,a
    
    if v_min > b:
        v_min=b
        
    if v_min>c:
        v_min=c
    
    if v_max<b:
        v_max=b
    
    if v_max<c:
        v_max=c
        
    print("min -> ",v_min,"\nmax -> ",v_max)
    
def zadanie3p1():
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
        
def zadanie3p2():
    print("dla rownania ax^2 + bx + c = 0:")
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    c = int(input("Podaj c: "))
    
    if a==0:
        print("to nie jest rownanie kwadratowe")
        return
    
    delta = m.pow(b,2) - 4*a*c
    
    if delta>0:
        x1 = (-b-m.sqrt(delta))/(2*a)
        x2 = (-b+m.sqrt(delta))/(2*a)
        
        print("\n\ndelta -> ",delta)
        print("Pierwiastki rownania to:")
        print("x1 -> ",x1)
        print("x2 -> ",x2)
        
    elif delta==0:
        x = (-b)/(2*a)
        
        print("\n\ndelta -> ",delta)
        print("Pierwiastek rownania to:")
        print("x -> ",x)
        
    else:
        print("nie ma rozwiazan")
        return
    
    
    
    
    
def main():
    # zadanie1()
    # zadanie2()
    # zadanie3p1()
    zadanie3p2()
    
    
if __name__ == '__main__':
    main()