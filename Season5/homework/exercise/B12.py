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
test = is_inside([200, 120], [140, 60, 100, 200])

if test == True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")