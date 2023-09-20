def permutation(n):
    perm = []
    return permNext(perm, n)


def permNext(p, n):
    if len(p) == n:
        print(p)
        return
    else:
        for x in range(n):
            if x not in p:
                p.append(x)
                permNext(p, n)
                p.pop()


permutation(5)
