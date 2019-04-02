so = int (input('Nhap so :'))
a = []
n = 2
while n <= so :
    i = 1
    s = 0
    while i <= n/2 :
        if n % i == 0 :
            s += i
            i += 1
        else :
            i += 1
    if s == n :
        a.append(n)
    n += 1
print (a)