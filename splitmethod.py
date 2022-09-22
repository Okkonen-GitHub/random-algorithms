
from random import randint

N = 10


def f(x):
    a=-2.8
    b=1.7
    c=-2.4
    d=3.3
    return a*(x**3) + b*(x**2) + c*x + d

def solve(f, a: int, b: int) -> int:

    def middlepoint(x1, x2):
        return (x1 + x2)/2

    a_f, b_f = f(a), f(b)

    precision = 10

    if (a_f > 0 and b_f < 0) or (a_f < 0 and b_f > 0):
        # print("a & b", a, b)
        if round(a_f, precision) == round(b_f, precision):
            print("a & b", a, b)
            return a
        c = middlepoint(a, b)
        # print("c", c)
        c_f = f(c)
        if c_f == 0:
            print("c",c)
            return c
        if (a_f > 0 and c_f < 0) or (a_f < 0 and c_f > 0):
            # print("fac")
            return solve(f,a, c)
        else:
            # print("fcb")
            return solve(f, c, b)
    else:
        return


x = None
while x is None:
    a = randint(-N, N)
    b = randint(-N, N)
    x=solve(f, a, b)
    print("RESTART")
print(x)