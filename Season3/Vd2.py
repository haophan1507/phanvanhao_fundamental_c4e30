n = int(input('Nhap n :'))
a = []
i = 2
while n != 1 :
    if n % i == 0 :
        a.append(i)
        n /= i
    else :
        i += 1
print(a)