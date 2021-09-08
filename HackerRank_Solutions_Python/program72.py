import cmath

s=complex(input())
z = complex(s)

c_polar1=cmath.polar(z)[0]
c_polar2=cmath.polar(z)[1]
print(c_polar1)
print(c_polar2)