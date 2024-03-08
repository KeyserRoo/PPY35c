from datetime import date
import math

def z1():
  print("aaa")
  print("bbb")
  
def z2():
  imie = input()
  rokUrodzenia = input()
  print("twoj wiek:", date.today().year - int(rokUrodzenia))
  
def z3():
  a = 37
  b = 11
  print(int(a/b))
  
def z4():
  a = 37
  b = 11
  print(a%b)

def z5():
  a = float(input())
  b = float(input())
  print(a*b)
  
def z6():
  print(round(math.pi,3))
  
def z7():
  a = input()
  b = input()
  
  print(float(a)+float(b))
  print(float(a)-float(b))
  print(float(a)*float(b))
  print(float(a)/float(b))
  print(math.sqrt(float(a)+float(b)))
  print(float(a)**float(b))
  print(float(b)**float(a))
  
def zd1():
  print("podaj wspolrzedna kartezjanska x: ")
  x = float(input())
  print("podaj wspolrzedna kartezjanska y: ")
  y = float(input())
  print("podaj wspolrzedna kartezjanska z: ")
  z = float(input())
  
  # uklad cylindryczny
  p = math.sqrt(x**2+y**2)
  if p==0:
    fi="indeterminate"
  elif x>=0:
    fi=math.asin(y/p)
  elif x< 0 and y >=0:
    fi=-math.asin(y/p)+math.degrees(math.pi)
  else:
    fi=-math.asin(y/p)+math.degrees(math.pi)
    
  print("zmienne punktu P ukladu cylindrycznego:\nρ - {}\nφ - {}\nz - {}".format(p,fi,z))
    
  # uklad sferyczny:
  r = math.sqrt(x**2+y**2+z**2)
  if r==0:
    theta="indeterminate"
  else:
    theta = math.acos(z/r)
  
  if x == 0:
    fi="indeterminate"
  else:
    fi = math.atan(y/x)
  
  print("zmienne punktu P ukladu cylindrycznego:\nr - {}\nθ - {}\nφ - {}".format(p,fi,z))
  

def main():
  # z1()
  # z2()
  # z3()
  # z4()
  # z5()
  # z6()
  # z7()
  zd1()


if __name__ == '__main__':
  main()