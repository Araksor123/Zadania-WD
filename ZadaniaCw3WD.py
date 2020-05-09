zad 1
A = [1/x for x in range(1, 11)]
B = [2**a for a in range(0, 11)]
C = {x: x for x in B if x % 4 == 0}
print(A)
print(B)
print(C)

zad 2
import random
macierz = [random.sample(range(0, 20), 4) for x in range(4)]
przekatna = []
for i in range(len(macierz)):
    przekatna.append(macierz[i][i])
print(macierz)
print(przekatna)

zad 3
produkty = {"banany": "sztuki","jablka": "sztuki",
            "orzechy": "kg","makaron": "opakowania" }
sztuki = {value: wartosc for value, wartosc in produkty.items() if wartosc == "sztuki"}
print(sztuki)

zad 4
def lin(a):   
    if a > 0:
        print("Funkcja jest rosnaca")
    elif a == 0:
        print("Funkcja jest stala")
    else:
        print("Funkcja jest malejaca")
lin(-4)

zad 5
def sprawdz(a1, a2):
    if a1 == a2:
        print("Proste sa rownolegle")
    elif a1* a2 == -1:
        print("Proste sa prostopadle")
sprawdz(5, -1/5)

Zad 6
def pr(x, y, a, b):
    import math
    print(math.sqrt((x-a)**2 + (y-b)**2))
pr(1, 4, 6, 8)

Zad 7
def przeciwpr(a, b):
    import math
    print(math.sqrt(a**2 + b**2))
przeciwpr(3, 4)

Zad 8 
def ciag(a=1, r=1, ile=10):
    ciag = [x for x in range(a, r*ile+1, r)]
    print(ciag)
ciag()

Zad 9
def ciag(a=1, r=1, ile=10):
    ciag = [x for x in range(a, r*ile+1, r)]
    return ciag
def iloczyn(ciag):
    iloczyn = 1
    for x in ciag: 
         iloczyn = iloczyn * x  
    return iloczyn
print(iloczyn(ciag()))

Zad 10
def lista(** zakupy):
    return sum(zakupy.values())
print(lista(banany=13, jablka=6, ogorki=3))
