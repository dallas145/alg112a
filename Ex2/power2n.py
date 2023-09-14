from datetime import datetime

# 方法 1
def power2n(n):
    return 2**n

# 方法 2a: 用遞迴
def power2n_recursive(n):
    if n == 0:
        return 1
    else: return power2n_recursive(n-1) + power2n_recursive(n-1)

# 方法 2b: 用遞迴
def power2n_recursive_b(n):
    if n == 0:
        return 1
    else: return 2 * power2n_recursive(n-1)

# 方法 3: 用遞迴+查表
ans = [None]*1000
ans[0] = 1
def power2n_re_lookup(n):
    if not ans[n] is None:
        return ans[n]
    else:
        ans[n] = power2n_re_lookup(n-1) + power2n_re_lookup(n-1)
        return ans[n]

n = int(input("input an integer: "))

startTime = datetime.now()
print(f'power2n({n}) = {power2n(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'time: {seconds}\n')

startTime = datetime.now()
print(f'power2n_recursive({n}) = {power2n_recursive(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'time: {seconds}\n')

startTime = datetime.now()
print(f'power2n_recursive_b({n}) = {power2n_recursive_b(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'time: {seconds}\n')

startTime = datetime.now()
print(f'power2n_re_lookup({n}) = {power2n_re_lookup(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'time: {seconds}\n')
