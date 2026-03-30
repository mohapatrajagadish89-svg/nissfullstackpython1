for i in range(4, 0, -1):
    ch = ord('D')
    for j in range(i):
        print(chr(ch), end=" ")
        ch -= 1
    print()