# 本程式使用ChatGPT產生
def distance(a, b):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)

    if a[-1] == b[-1]:
        cost = 0
    else:
        cost = 1

    return min(
        distance(a[:-1], b) + 1,
        distance(a, b[:-1]) + 1,
        distance(a[:-1], b[:-1]) + cost
    )


a = "abcde"
b = "bbbcd"

print(distance(a, b))
