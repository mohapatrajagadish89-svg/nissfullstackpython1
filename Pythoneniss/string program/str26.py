#join()
#Step 1: split()
#L= s.split()
#Converts string into a list of words
#Result:['ram', 'is', 'a', 'good', 'boy']

#Step 2: join()
#s1 = " ".join(L)
#join() converts list → string
#" " means words will be joined with a space
#Result:"ram is a good boy"


s="ram is a good boy"
L=s.split()
s1=" ".join(L)
print(s1)

#o/p- ram is a good boy
