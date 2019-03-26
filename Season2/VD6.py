for x in range(101):
    for y in range(101):
        for z in range(101):
            if x*y*z == x*x + y*y + z*z:
                print(x,y,z)