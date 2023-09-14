# power2n 的四種實作方法

## 問題：
* 在Powrshell執行時，若執行時間太短則無法顯示正確程式耗時，須在WSL環境下才能正確顯示
* 測試兩次的結果中，在WSL環境執行的耗時皆比在Powershell中執行的耗時短

## 執行結果

* Powershell: Python 3.9.16
```
(base) PS C:\Users\mikel\Github\alg112a\Ex2> python power2n.py
input an integer: 30
power2n(30) = 1073741824
time: 0:00:00.001000

power2n_recursive(30) = 1073741824
time: 0:02:13.177518

power2n_recursive_b(30) = 1073741824
time: 0:01:03.701230

power2n_re_lookup(30) = 1073741824
time: 0:00:00.001001
```

* WSL: Python 3.10.6
```
neil@B660M12400:/mnt/c/Users/mikel/Github/alg112a/Ex2$ python3 power2n.py
input an integer: 30
power2n(30) = 1073741824
time: 0:00:00.000846

power2n_recursive(30) = 1073741824
time: 0:01:39.684352

power2n_recursive_b(30) = 1073741824
time: 0:00:49.382430

power2n_re_lookup(30) = 1073741824
time: 0:00:00.000026
```
