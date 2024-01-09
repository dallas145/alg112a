# 本程式使用ChatGPT產生

def distance(a, b, memo={}):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)

    if (len(a), len(b)) in memo:
        return memo[len(a), len(b)]

    if a[-1] == b[-1]:
        cost = 0
    else:
        cost = 1

    result = min(
        distance(a[:-1], b, memo) + 1,
        distance(a, b[:-1], memo) + 1,
        distance(a[:-1], b[:-1], memo) + cost
    )
    memo[(len(a), len(b))] = result
    return result


def testDistance(a, b):
    emptyD = {}
    ans = distance(a, b, emptyD)
    print(f'First string is:\n\t{a}')
    print(f'Second string is:\n\t{b}')
    print(f'Distance: {ans}\n')


a = "abcdefghijklmnop"
b = "fghijklmonpquesl"

c = "This is a test."
d = "This is a test"

e = "a8a2f6ebe286697c527eb35a58b5539532e9b3ae3b64d4eb0a46fb657b41562c"
f = "c7be1ed902fb8dd4d48997c6452f5d7e509fbcdbe2808b16bcf4edce4c07d14e"

testDistance(a, b)
testDistance(c, d)
testDistance(e, f)
