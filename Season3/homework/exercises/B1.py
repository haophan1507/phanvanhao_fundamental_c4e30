shop = ['T-Shirt','Sweater']
loop = True
while loop :
    Nhap = input('Welcome to our shop, what do you want (C, R, U, D)? ')
    if Nhap == 'R' or Nhap =='r':
        print('Our items:',shop)
    elif Nhap == 'C' or Nhap =='c':
        New = input('Enter new item:')
        shop.append(New)
        print('Our items:',shop)
    elif Nhap == 'U' or Nhap == 'u':
        Vtri = int(input('Update position? '))
        New = input('New item? ')
        del shop[Vtri-1]
        shop.insert(Vtri-1, New)
        print('Our items:',shop)
    elif Nhap == 'D' or Nhap =='d' :
        Delete = int(input('Delete position? '))
        del shop[Delete - 1]
        print('Our items:',shop)
    else :
        loop = False