a=10
print(id(a))
print(a)
b=10
print(id(b))
print(b)
a=10
b=a
print(id(a),id(b))
print(a,b)
a=10
print(id(a),a)
a=20
print(id(a),a)
b=10
print(id(b),b)
#swapping 2 number using 3rd variable
a=10
b=10
print("before swapping a=",a,"b=",b)
t=a
a=b
b=t
print("after swapping a=",a,"b=",b)
#swapping 2 number without using 3rd variable



a=10
b=2.5
c="hi"
print(a,b,c)


a=10,2.5,"hi"
print(a)
print(type(a))

a=10
b=20
a,b=b,a
print(a,b)

#swapping 3 number left to right with 4th variable


a=2
b=4
c=6
t=c
c=b
b=a
a=t
print(a,b,c)

#add two number without using + operator
a=10
b=20
c=a--b
print(c)

print("e" in "hello")
print()



a=10
b=10
c=20

print(10<40<20)
print(10>40>20)



























