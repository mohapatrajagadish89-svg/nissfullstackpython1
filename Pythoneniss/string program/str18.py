#ljust()/rjust()                                 

#center(10, "*"                   
#String goes in the center
#Extra 3 stars are divided:
#left = 1 star
#right = 2 st

#ljust(10, "*")
#String stays on the left
#Extra stars added to the right

#rjust(10, "*")
#String stays on the right
#Extra stars added to the left

s="welcome"
print(s.center(10,"*"))
print(s.ljust(10,"*"))
print(s.rjust(10,"*"))

#o/p-*welcome**
#    welcome***
#    ***welcome
