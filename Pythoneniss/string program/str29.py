#decode()
#Step 1: encode()
#b=s.encode()
#Converts string → bytes
#"ram" becomes:b'ram'

#Step 2: Print bytes
#print(b)
#Output:b'ram'

#Step 3: decode()
#s1=b.decode()
#Converts bytes → string
#b'ram' becomes:"ram"

#Step 4: Print string
#print(s1)
#Output:ram

s="ram"
b=s.encode()
print(b)
s1=b.decode()
print(s1)
