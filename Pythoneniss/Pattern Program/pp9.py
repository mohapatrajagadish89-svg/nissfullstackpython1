for i in range(1, 5):
    ch = ord('A') + i - 1
    for j in range(i):
        print(chr(ch), end=" ")
        ch -= 1
    print()