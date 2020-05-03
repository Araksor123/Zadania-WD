Ćwiczenia 2 WD, Bartosz Napiórkowski
Zad 1
a = input()
print(a.count(" "))

Zad 2
import sys

print ("Podaj pierwsza wartosc:")
a = sys.stdin.readline()
b = int(a)
print ("Podaj druga wartosc:")
c = sys.stdin.readline()
d = int(c)
x = str(b*d)
sys.stdout.write(x)

Zad 3
>
<
>=
<=
==
!=
is
in
not is/in
and
or
not

Zad 4
print("Podaj liczbe:")
a = input()
a = int(a)
if a < 0:
    a *= -1
print(a)

Zad 5
a, b, c = input("Podaj trzy liczby oddzielone spacjami: ").split(" ")
a = int(a)
b = int(b)
c = int(c)
if 0 <= a <= 10 and a > b and b > c:
    print("Warunki spelnione!")
else:
    print("Warunki nie sa spelnione!")
  
Zad 6
for x in range(5, 100, 5):
    print(str(x)+ " ")

Zad 7
while True:
    print("Podaj liczbe:")
    a = input()
    a = int(a)
    print(a*a)
    
Zad 8
x = 0
lista = []
while x < 5:
    print("Podaj liczbe:")
    a = input()
    lista += a
    x += 1

Zad 9
print ("Podaj liczbe:")
a = input()
a = int(a)
b = 0
while a > 0:
    b += a%10
    a //= 10
print("Suma cyfr liczby: " + str(b))

Zad 10
print ("Podaj dodatnia liczbe nie wieksza niz 10:")
a = input()
a = int(a)

if 1 <= a <= 10:
    for x in range(1,a+1,1):
        print(x * 'A')

Zad 11
print ("Podaj wysokosc diamentu, minimum 3, maksimum 9:")
a = input()
a = int(a)
if 3 <= a <= 9:
    for x in range(1,a+1,2):
        print((x * 'o').center(a))
    if a % 2 == 0:
        print((a-1) * 'o')
    for x in reversed(range(1,a-1,2)):
        print((x * 'o').center(a))
      
Zad 12
for x in range(1,11):
     for y in range(1,11):
          print (f"{x*y:>5}", end = " ")
     print()
    
Zad 14
import math
print("Podaj liczbe: ")
a = input()
a = int(a)
try:
    pierwiastek = math.sqrt(a)
    print("Wynik= " + str(pierwiastek))
except ValueError:
    print("Nie mozna policzyc tego pierwiastka!")
 
Zad 15
print("Podaj liczbe: ")
try:
    a = int(input())
    print("Podana liczba to: " + str(a))
except:
    ValueError: print("Podales litere zamiast cyfry!")
