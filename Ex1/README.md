# 費氏數列遞迴版

## 問題：
* 在Powrshell執行時，大多無法顯示正確程式耗時，須在WSL環境下才能正確顯示

## 執行結果

### fib_loop.py

* Powershell: Python 3.9.16
```
(base) PS C:\Users\mikel\Github\alg112a\Ex1> python fib_loop.py
fibonacci(60) = 1548008755920
time: 0.000000
time:0:00:00
```

* WSL: Python 3.10.6
```
neil@B660M12400:/mnt/c/Users/mikel/Github/alg112a/Ex1$ python3 fib_loop.py
fibonacci(60) = 1548008755920
time: 0.000047
time:0:00:00.000046
```

### fib_loop_input.py

* Powershell: Python 3.9.16
```
(base) PS C:\Users\mikel\Github\alg112a\Ex1> python fib_loop_input.py
input an integer: 100
fibonacci(100) = 354224848179261915075
time: 0.001000
time:0:00:00.000999
```

* WSL: Python 3.10.6
```
neil@B660M12400:/mnt/c/Users/mikel/Github/alg112a/Ex1$ python3 fib_loop_input.py
input an integer: 100
fibonacci(100) = 354224848179261915075
time: 0.000067
time:0:00:00.000062
```
