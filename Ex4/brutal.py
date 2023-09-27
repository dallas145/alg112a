# x^2 - 3x + 1 = 0

# 暴力法
from numpy import arange


def f(x):
    return x ** 2 - 3 * x + 1


# 已知x在0到3之間
for i in arange(0, 3, 0.001):
    if abs(f(i)) < 0.001:
        print("x =", i, "f(x) =", f(i))
