# 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k, step=0.001):
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step


# 梯度：函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp


def f(p):
    [x, y, z] = p
    return (x - 3) ** 2 + (y + 7) ** 2 + (z - 1) ** 2


def gradient(f, p, step=0.001):
    while True:
        fcurrent = f(p)
        gd = grad(f, p)
        p1 = p.copy()

        for i in range(len(p1)):
            p1[i] -= gd[i] * step

        fnext = f(p1)

        if fnext < fcurrent:
            p = p1
            print('p=', p, 'f(p)=', fnext)

        else:
            break


gradient(f, [2, 1, 3])
