'''dem = 0 
while True :
    print('Hi', dem)
    
    dem += 1
    if dem >= 3 :
        break
for v in range(10) :
    print(v)
    break

n = str(input('Nhap chuoi '))
while len(n) < 8 :
    print('Nhap lai chuoi')
    n = str(input('Nhap chuoi '))

while True :
    password = input('Nhap pass ')
    if len(password) >= 8 : 
        print(password)
        break

dem = 0
s = 21
while True :
    s = s*0.065 + s
    dem += 1
    if dem >= 9 :
        break
print('So tien sau 9 nam la ',s)

dem = 1
s = 21
while True :
    s = s*0.065 + s
    dem += 1    
    if s > 1200 :
        print('So nam can de mua nha la ',dem )
        break'''

n = int(input('Moi ban nhap so phan tu:'))
ds = []
for v in range(n) :
    so = int(input('Nhap phan tu:'))
    ds.append(so)
for v in ds :
    print(v,end=' ')

sum = 0
dem = 0
for v in ds :
    if v % 2 ==0 :
        sum += v
        dem += 1
print('\nTrung binh cac so chan la ',sum/dem)