"""
Arithmetic              -+*/%
Relational/Comparision  <=,>=,==,!=,<,>
Assignment              =,-=,+=,*=,/=
Logical                 not, and, or
"""

#arithmetic
a=10
b=4
print(a+b)
print(a-b)
print(a**b) #power
print(a/b)
print(a%b) #remainder

#Relational 
c=10
d=5
print(c>d)
print(c<d)
print(c==d)
print(c>=d)

#Assignment
e=9
e+=1
print(e)
e*=3
print(e)

#Logical Operators

var=False
print(not var)
print(not (5>2))
print((3<2) and (7>3))
print((3<2) or (7>3))
