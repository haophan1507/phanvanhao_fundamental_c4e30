ex1= {
    1 : 35,
    2 : 36,
    3 : 40,
    4 : 44
}
ex2 = {
    1 : "About 55",
    2 : "About 65",
    3 : "About 75",
    4 : "About 85"
}
dem = 0
print('''Answer the following algebra question:
If x=8, then what is the value of 4(x + 3) ?''')
for i,j in ex1.items() :
    print(i,':',j)
n = int(input('Your choice :'))
if n == 4 :
    print('Bingo')
    dem += 1
else :
    print(':(')
print('''Estimate this answer (exact calculation not needed:
Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?''')
for i,j in ex2.items() :
    print(i,':',j)
n = int(input('Your choice :'))
if n == 2 :
    print('Bingo')
    dem += 1
else :
    print(':(')
print('Your correctly answer',dem,'out of 2 questions')