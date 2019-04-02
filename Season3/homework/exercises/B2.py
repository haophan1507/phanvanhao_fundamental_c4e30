sheep = []
#2.1
n = int(input('Nhap kich thuoc dan cuu : '))
for i in range(n) :
    cuu = int(input('Kich thuoc con cuu la : '))
    sheep.append(cuu)
print('Kich thuoc dan cuu :',end = ' ')
print(sheep)
#2.2
'''m = sheep[0]
for i in range(1,n) :
    if m < sheep[i] :
        m = sheep[i]
print('Con cuu co kich thuoc lon nhat la ',m)
#2.3
m1 = sheep.index(m)
del sheep[m1]
sheep.insert(m1,8)
print('Dan cuu sau khi cat long la : ',end = ' ')
print(sheep)
#2.4
for i in range(n) :
    sheep[i] += 50
print('Sau 1 thang dan cuu tang len : ',end = ' ')
print(sheep)'''
#2.5
month = int(input('Ban muon tinh trong may thang : '))
for i in range(month) :
    print('MONTH ',i+1)
    for i in range(n) :
        sheep[i] += 50
    print('Sau 1 thang dan cuu tang len : ',end = ' ')
    print(sheep)
    m = sheep[0]
    for i in range(1,n) :
        if m < sheep[i] :
            m = sheep[i]
    print('Con cuu co kich thuoc lon nhat la ',m)
    m1 = sheep.index(m)
    del sheep[m1]
    sheep.insert(m1,8)
    print('Dan cuu sau khi cat long la : ',end = ' ')
    print(sheep)
#2.6
sum = 0 
for i in range(n) :
    sum += sheep[i]
print('Tong kich thuoc dan cuu ',sum)
print('So tien muon co ',sum,'*','2$','=',sum*2,'$')