#implementing GaussianReduction to find the optimal basis of two vectors.
#Gaussian Reduction

V1 = [846835985, 9834798552]
V2 = [87502093,123094980]
temp = [1,1] #random Vector

def mod(V):
    return (V[0]**2 + V[1]**2)**0.5
    # calculates magnitude of a vector
def dot(A,B):
    return A[0]*B[0] + A[1]*B[1]
    # calculates dot product of two vectors
    
m = True
while m:
    if mod(V1) > mod(V2) :
        temp = V1
        V1 = V2
        V2 = temp
    m = int(dot(V1,V2)/(mod(V1)**2))
    V2[0] = V2[0] -m*V1[0]
    V2[1] = V2[1] -m*V1[1]
    if m == 0:
        break
        
print(V1)
print(V2)
