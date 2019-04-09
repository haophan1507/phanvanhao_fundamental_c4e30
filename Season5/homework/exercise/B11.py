def is_inside(list1,list2) :
    if len(list1) ==  2 and len(list2) == 4:
        x       = list1[0]
        y       = list1[1]
        x_rec   = list2[0]
        y_rec   = list2[1]
        width   = list2[2]
        height  = list2[3]

        if (x > x_rec and x < (x_rec + width)) and (y > y_rec and y < (y_rec + height)):
            return True
        else:
            return False
    else:
        return False
list1 = []
list2 = []
x = int(input('Nhap toa do x cua diem :'))
list1.append(x)
y = int(input('Nhap toa do y cua diem :'))
list1.append(y)
x_rec = int(input('Nhap toa do x cua hcn :'))
list2.append(x_rec)
y_rec = int(input('Nhap toa do y cua hcn :'))
list2.append(y_rec)
width = int(input('Nhap chieu dai cua hcn :'))
list2.append(width)
height = int(input('Nhap chieu cao cua hcn :'))
list2.append(height)
print(is_inside(list1,list2))