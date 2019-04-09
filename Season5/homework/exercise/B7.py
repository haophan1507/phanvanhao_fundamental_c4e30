def remove_dollar_sign(s) :
    s1 = s.replace('$','')
    return s1
s = input('Nhap s :')
print(remove_dollar_sign(s))