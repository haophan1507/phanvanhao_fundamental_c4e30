alpha = 'abcdefghijklmnopqrstuvwxyz'
list(alpha)
n = input('Nhap chuoi :')
n.islower()
list(n)
for i in range(len(alpha)) :
    count = 0
    dem = 0 
    while dem != len(n) :
        if alpha[i] == n[dem] :
            dem += 1
            count += 1
        else :
            dem += 1
    if count == 0 :
        continue
    else :
        print(alpha[i],':',count)