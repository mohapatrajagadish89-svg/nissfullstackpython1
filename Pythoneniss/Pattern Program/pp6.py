for i in range(4):
    for j in range(ord('D'), ord('D') - (4 - i), -1):
        print(chr(j), end=" ")
    print()