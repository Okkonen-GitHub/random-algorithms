
from random import randint
from numpy.polynomial import polynomial

# x-koordinaatti läheltä funktion nollakohtaa
N = 10

# esittää funktiota, jonka nollakohta halutaan ratkaista
class funk:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    # returns the function's value at x
    def h(self, x):
        return self.a*x**3 + self.b * x**2 + self.c * x + self.d

    # returns the function's derivative's value at x
    def hd(self, x):
        pol = polynomial.Polynomial([self.d, self.c, self.b, self.a])
        der = pol.deriv() # polynomifunktion derivaatta // the derivative of a polynomial (function)
        print(pol.integ())
        coefs = der.coef # ja sen kertoimet // and its coefficients
        # lasketaan derivaatta funktion arvo kohdassa x
        # // compute the value of the derivative function at x
        result = 0
        for p, c in enumerate(coefs):
            # c*x^p
            result += c*x**p
        return result

    pass

def solve(f: funk, x):
    def almost_equal(a, b):
        precicion = 0.0000000001
        # print(a-b)
        return abs(a - b) < precicion

    
    def formula(f: funk, x):
        return (x - (f.h(x))/(f.hd(x)))

    x_1 = formula(f, x)
    while True:
        x_2 = formula(f, x_1)
        if almost_equal(x_1, x_2):
            return x_1
        else:
            x_1 = x_2

# ax³+bx²+cx+d 
my_f = funk(0,-0.5,2,1)

# the initial guess
x_0=randint(-N, N)

x=solve(my_f, x_0)
print(x)
