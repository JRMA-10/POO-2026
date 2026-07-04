for c in range(1, 11):
    print(c, end = ' ')
    if c % 2 == 0 and c != 1:
        print(c)
    else:
        print(c - 1)