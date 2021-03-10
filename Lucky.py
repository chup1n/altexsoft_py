while True:
    print('Please enter your ticket number here:')
    x = str(input())
    if len(x) < 4 or len(x) > 8:
        print('The ticket number must be from 4 to 8 digits long.')
    if len(x) % 2 != 0 and len(x) >= 4:
        x = '0' + x
    if len(x) == 4:
        x = int(x)
        l1 = ((x // 1000) % 10)
        l2 = ((x // 100) % 10)
        l3 = ((x // 10) % 10)
        l4 = ((x // 1) % 10)
        if l1 + l2 == l3 + l4:
            print('You have lucky ticket number!')
        else:
            print('Sorry but your ticket number is not lucky.')
    elif len(x) == 6:
        x = int(x)
        l1 = ((x // 100000) % 10)
        l2 = ((x // 10000) % 10)
        l3 = ((x // 1000) % 10)
        l4 = ((x // 100) % 10)
        l5 = ((x // 10) % 10)
        l6 = ((x // 1) % 10)
        if l1 + l2 + l3 == l4 + l5 + l6:
            print('You have lucky ticket number!')
        else:
            print('Sorry but your ticket number is not lucky.')
    elif len(x) == 8:
        x = int(x)
        l1 = ((x // 10000000) % 10)
        l2 = ((x // 1000000) % 10)
        l3 = ((x // 100000) % 10)
        l4 = ((x // 10000) % 10)
        l5 = ((x // 1000) % 10)
        l6 = ((x // 100) % 10)
        l7 = ((x // 10) % 10)
        l8 = ((x // 1) % 10)
        if l1 + l2 + l3 + l4 == l5 + l6 + l7 + l8:
            print('You have lucky ticket number!')
        else:
            print('Sorry but your ticket number is not lucky.')
