from datetime import datetime
import time

def fibonacci(n):
    fib = [1, 1]
    for i in range(n-2):
        _next = fib[i] + fib[i+1]
        fib.append(_next)

    return fib[len(fib)-1]

# n = 35
n = 60

sT = time.time() # 使用time module
startTime = datetime.now() # 使用datetime module

print("fibonacci(%d) = %d" % (n, fibonacci(n)))

eT = time.time() # 使用time module
endTime = datetime.now() # 使用datetime module

sec = eT - sT # 使用time module
seconds = endTime - startTime # 使用datetime module

print("time: %f"%(sec)) # 使用time module
print("time:{}".format(seconds)) # 使用datetime module
