z = [1,2,3,4,5]
for a in z:
    for b in z:
        for c in z:
            for d in z:
                for e in z:
                    if a in (b,c,d,e):
                        continue
                    elif b in (a,c,d,e):
                        continue
                    elif c in (a,b,d,e):
                        continue
                    elif d in (a,b,c,e):
                        continue
                    else:
                        print(a,b,c,d,e)