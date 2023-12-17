# 本程式參考自 LeeYi-user
# 大概知道梯度下降在做什麼
# 但是看不懂反向傳播
from engine import Value

a = Value(2)
b = Value(1)
c = Value(3)

step = 0.01

while True:
    f = a ** 2 + b ** 2 + c ** 2

    print('a=', a.data, 'b=', b.data, 'c=', c.data, 'f=', f.data)
    f.backward()

    if a.grad < 0.001:
        break

    a -= a.grad * step
    b -= b.grad * step
    c -= c.grad * step
