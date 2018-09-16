#gas dynamics equations
from math import sqrt
#Isentropic Flow
#Mach Number M and gamma are known
#A.1 To/T
def ToT(M,gamma):
    output = 0.0
    output = 1 + ((gamma-1)/2)*M**2
    return output

#T/To
def TTo(M,gamma):
    output = 0.0
    output = 1/(ToT(M,gamma))
    return output

#A.2 Po/P
def PoP(M,gamma):
    output = 0.0
    output = (1+((gamma-1)/2)*M**2)^(gamma/(gamma-1))
    return output

#P/Po
def PPo(M,gamma):
    output = 0.0
    output = 1/(PoP(M,gamma))
    return output
