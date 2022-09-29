
from random import randint

# alkuarvaukseen luomiseen käytetty luku
N = 10

# esittää funktiota, jonka nollakohta halutaan ratkaista
def g(x):
    a=0
    b=0
    c=2
    d=1
    return a*(x**3) + b*(x**2) + c*x + d



def solve(f, x):
    
    # tarkistaa onko kaksi liukulukua tietyllä tarkkuudella yhtä suuret
    def almost_equal(a: float, b: float) -> bool:
        precicion = 0.00000001
        print(a-b)
        return abs(a - b) < precicion

    x_1 = f(x)
    while True:
        x_2 = f(x_1)
        print(x_1, x_2)
        if  almost_equal(x_1, x_2):
            return x_1
        else:
            x_1 = x_2





a = randint(-N, N)
x=solve(g, -2)
print(x)
