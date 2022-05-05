def FibRecurs(n):
	if n <= 1:
		return n
	else:
		return FibRecurs(n-1) + FibRecurs(n-2)
        
def FibList(n):
    F = [0,1]
    i = 2
    while i <= n:
        F.append(F[i-1]+F[i-2])
        i += 1
    return F[n]

def NaiveGCD(a,b):
    best = 0
    d = 1
    lim = a+b
    while d <= lim:
        if a%d == 0 and b%d == 0:
            best = d
        d +=1
    return best

def EuclidGCD(a,b):
    rem = a%b
    if b == 0:
        return a
    return EuclidGCD(b,rem)

# RUSSIAN PEASANT MULTIPLICATION

import math
import pandas as pd

n1 = 89
n2 = 18
halving = [n1]
print(math.floor(halving[0]/2))
while(min(halving) > 1):
    halving.append(math.floor(min(halving)/2))
doubling = [n2]
while(len(doubling) < len(halving)):
    doubling.append(max(doubling) * 2)
half_double = pd.DataFrame(zip(halving,doubling))
half_double = half_double.loc[half_double[0]%2 == 1,:]
answer = sum(half_double.loc[:,1])