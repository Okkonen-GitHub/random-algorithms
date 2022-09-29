
#import math
from random import randint

# alkuarvaukseen luomiseen käytetty luku
N = 10

# esittää funktiota, jonka nollakohta halutaan ratkaista
def g(x):
    a=0
    b=1
    c=2.5
    d=0.5
    return a*(x**3) + b*(x**2) + c*x + d
    # return math.sqrt(x+math.sqrt(x**2+1))/2


# solves f(x)=x, or in other terms the intersecting point between y=f(x) and y=x
def solve(f, x):
    
    # tarkistaa onko kaksi liukulukua tietyllä tarkkuudella yhtä suuret
    def almost_equal(a: float, b: float) -> bool:
        precicion = 0.00000001
        return abs(a - b) < precicion

    x_1 = f(x)
    # doing only 100 iterations because it is not guaranteed to always find a solution
    for _ in range(100):
        x_2 = f(x_1)
        print(x_1, x_2)
        if  almost_equal(x_1, x_2):
            return x_1
        else:
            x_1 = x_2





a = randint(-N, N)
x=solve(g, -0.6)
print(x)
