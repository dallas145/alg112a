# 本程式參考自李易同學的程式
# 看到他的程式以後，我覺得我找不到更好的解決方式
# 所以直接借用並將變數命名改為我習慣的方式
def distance(a, b, ai=0, bi=0, R={}):  # a= string A, b= string B
    alen = len(a)                      # ai= index of A, bi= index of B
    blen = len(b)                      # R= store the answer of each step.
    if ai == alen and bi == blen:
        return 0
    elif ai == alen:
        return blen - bi
    elif bi == blen:
        return alen - ai

    if (ai, bi) not in R:
        if a[ai] == b[bi]:
            ans = distance(a, b, ai + 1, bi + 1, R)
        else:
            insert = 1 + distance(a, b, ai, bi + 1, R)
            delete = 1 + distance(a, b, ai + 1, bi, R)
            replace = 1 + distance(a, b, ai + 1, bi + 1, R)
            ans = min(insert, delete, replace)

        R[(ai, bi)] = ans

    return R[(ai, bi)]


def testAnswer(a, b):  # 測試用
    print("First string is:\n" + a)
    print("Second string is:\n" + b)
    emptyD = {}
    ans = str(distance(a, b, 0, 0, emptyD))
    print("Edit distance between them is: " + ans)


a = "This is a test."
b = "This is a test"

a_hash = "a8a2f6ebe286697c527eb35a58b5539532e9b3ae3b64d4eb0a46fb657b41562c"
b_hash = "c7be1ed902fb8dd4d48997c6452f5d7e509fbcdbe2808b16bcf4edce4c07d14e"
H = {}  # 第二次使用必須給予R參數（空字典），不然結果會和上次一樣，但我不知道原因

c = "987654321"
d = "123456789"

# print(distance(a, b, 0, 0))
# print(distance(a_hash, b_hash, 0, 0, H))
# print(distance(c, d, 0, 0, H2))
testAnswer(a, b)
testAnswer(a_hash, b_hash)
testAnswer(c, d)
