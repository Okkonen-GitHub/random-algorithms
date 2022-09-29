
from random import randint

# x-koordinaatti läheltä funktion nollakohtaa
N = 10

# esittää funktiota, jonka nollakohta halutaan ratkaista
def f(x):
    a=-2.8
    b=1.7
    c=-2.4
    d=3.3
    return a*(x**3) + b*(x**2) + c*x + d


def solve(f, a: int, b: int) -> int:

    # laskee kahden pisteen puolivälissä olevan pisteen x-koordinaatin
    def middlepoint(x1, x2):
        return (x1 + x2)/2

    # arvot f(a) ja f(b)
    a_f, b_f = f(a), f(b)

    precision = 10

    # f(a) ja f(b) ovat erimerkkiset
    if (a_f > 0 and b_f < 0) or (a_f < 0 and b_f > 0):
        # print("a & b", a, b)
        if round(a_f, precision) == round(b_f, precision):
            # print("a & b", a, b)
            return a
        c = middlepoint(a, b)
        # print("c", c)
        c_f = f(c)
        if c_f == 0:
            # x = c ja f(c) = 0
            return c
        if (a_f > 0 and c_f < 0) or (a_f < 0 and c_f > 0):
            # uusi tarkasteluväli on [a, c]
            return solve(f,a, c)
        else:
            # uusi tarkasteluväli on [c, b]
            return solve(f, c, b)
    else:
        return


x = None
while x is None:
    #print("Start!")
    # valitaan tarkistelu väli [a, b] osittain satunnaisesti niin monta kertaa kuin on pakko
    a, b = randint(-N, N), randint(-N, N)
    x=solve(f, a, b)

print(x)
#   > python splitmethod.py
#   > 0.9722855963777874
