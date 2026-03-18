#casefold()
#It converts the string into lowercase (more powerful than lower())

s = "rAm is a Good Boy"
s = s.casefold()
print(s)

#o/p-ram is a good boy


#Difference between lower() and casefold()
#Both convert to lowercase, but:
#lower() → normal lowercase
#casefold() → stronger lowercase (used for comparisons)