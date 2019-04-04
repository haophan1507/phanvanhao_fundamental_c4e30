prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
a = ['banana','apple','orange','pear']
for i in range(len(a)) :
    print(a[i])
    print('price :',prices[a[i]])
    print('stock :',stock[a[i]])
s = 0
print('')
for i in range(len(a)) :
    print(a[i],':',prices[a[i]]*stock[a[i]],'$')
    s += prices[a[i]]*stock[a[i]]
print('Tong tien la :',s,'$')