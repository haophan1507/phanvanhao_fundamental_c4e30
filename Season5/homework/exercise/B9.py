def get_even_list(l) :
    l1 = []
    for i in l :
        if i % 2 ==0 :
            l1.append(i)
    return l1
n = int(input('Nhap so phan tu cua list :'))
l = []
for i in range(n) :
    n1 = int(input('Nhap :'))
    l.append(n1)
print(get_even_list(l))