import random
a = str(input ('Nhap chu '))
print(*list(a))
print([random.shuffle(a) for _ in range(len(a))])
