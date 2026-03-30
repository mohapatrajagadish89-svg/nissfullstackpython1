for i in range(4, 0, -1):
    ch = ord('A') + i - 1
    for j in range(i, 0, -1):
        print(chr(ch), end=" ")
        ch -= 1
    print()