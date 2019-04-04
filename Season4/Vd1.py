a = {'computer' : 'may tinh','mouse' : 'chuot','keyboard' : 'ban phim'}
while True :
    b = (input('Moi ban nhap vao 1 tu : '))
    if b == 'exit' or b == 'out' :
        break
    if b in a :
        print(a[b])
    else :
        print('Tu nay khong co trong tu dien.')
        c = input('Moi ban nhap nghia cua tu :')
        a[b] = c