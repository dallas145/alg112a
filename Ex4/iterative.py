# x^2 - 3x + 1 = 0

#  迭代法

def f1(x):
    return (x ** 2 + 1) / 3


def f2(x):
    return (3 * x - 1) / x


def f3(x):
    return (x - 1) ** 2


x1 = x2 = x3 = 1

for i in range(20):
    x1, x2, x3 = f1(x1), f2(x2), f3(x3)
    print("x1: ", x1, "x2: ", x2, "x3: ", x3)
