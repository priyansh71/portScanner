#Implementing Scalar multiplication of two points modulo p in Ecc
#Scalar multiplication

from Crypto.Util.number import inverse

p = 9739
A = 497
B = 1768
n = 7863
zero = [0,0]
X = [2339, 2213]

def find_lambda(P,Q):
    if(P == Q):
        return ((3*(P[0]**2) + A) %p) * inverse((2*P[1]) % p ,p)
    else:
        return (Q[1]-P[1]) %p * inverse((Q[0]-P[0]) %p,p)

def summer(P,Q):
    if P == zero:
        return Q
    elif Q == zero:
        return P
    elif P[0] == Q[0] and P[1]+Q[1] ==0:
        return zero
    else:
        x3 = (find_lambda(P,Q)**2 - P[0] - Q[0] ) %p
        y3 = (find_lambda(P,Q)*(P[0] - x3) - P[1])% p
    return [x3,y3] 


def mult(n,P):
    Q = P
    R = zero
    while n>0:
        if n % 2 == 1:
            R = summer(Q,R)
            Q = summer(Q,Q)
            n = n//2
        elif n % 2 == 0:
            Q = summer(Q,Q)
            n = n//2
        elif n <= 0:
            break
    return R

print(mult(n,X))

