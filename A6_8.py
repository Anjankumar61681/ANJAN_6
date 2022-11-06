''' Write a python script to check whether a given
 quadratic equationhas two real &
 distinct roots, real & equal roots  or 
 imaginary root'''
print("Enter a value of a ,b and c of quadrtic equation:")
a,b,c=int(input()),int(input()),int(input())
d=b**2-4*a*c
if d>0:
    print("Real and distinct rots")
elif(d==0):
    print("Real and equal roots")
else:
    print("Imaginary roots")                      #x**2+bx+c=0 quartic equation