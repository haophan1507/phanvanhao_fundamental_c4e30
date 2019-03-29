mass = int(input('Nhap can nang (kg) = '))
height = int(input('Nhap chieu cao (cm) = '))
height = float(height)/100
BMI = mass / (height*height)
if BMI < 16 :
    print('Thieu can nghiem trong.')
elif BMI <= 18.5 :
    print('Thieu can.')
elif BMI <= 25 :
    print('Binh thuong.')
elif BMI <= 30 :
    print('Thua can.')
else :
    print('Beo phi.')