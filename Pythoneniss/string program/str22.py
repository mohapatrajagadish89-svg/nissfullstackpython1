#find/rfind
#1-find("x")
#find() returns the index of first occurrence
#If the character is not found, it returns -1

#2-rfind("e")
#rfind() returns the last occurrence index

#Index positions:
#w  e  l  c  o  m  e
#0  1  2  3  4  5  6


s = "welcome"
print(s.find("x"))
print(s.rfind("e"))	

#o/p- -1,6