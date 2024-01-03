import random, copy


def neighbor(f, x, h=0.01):
    x += random.uniform(-h, h)
    return f(x), x


def hillClimbing(f, x, h=0.01):
    if f(x) <= 0:
        print("更換初始值，使f(x)大於零")
        return

    failCount = 0                      # 失敗次數歸零
    while (failCount < 10000):         # 如果失敗次數小於一萬次就繼續執行
        fnow = f(x)                    # fxy 為目前高度
        f1, xn = neighbor(f, copy.copy(x), h)
        if f1 < fnow:                 # 如果移動後高度比現在高
            if f1 <= 0:
                break

            x = xn
            print('x=', x, 'f(x)=', f1)
            failCount = 0              # 失敗次數歸零

        else:                          # 若沒有更高
            failCount = failCount + 1  # 那就又失敗一次

    else:
        print("無實數解")


def f(x):
    return x**5 + 1


def f1(x):
    return x**8 + 3 * x**2 + 1


def f2(x):
    return x**3 + 5 * x**2 - 2 * x - 5


# hillClimbing(f, 0)
# hillClimbing(f1, 0)
hillClimbing(f2, 10)
