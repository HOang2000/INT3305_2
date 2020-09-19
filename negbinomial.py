from math import log2

def C(k,n):
    if k == 0 or k == n:
        return 1
    if k == 1:
        return n
    return C(k-1,n-1) + C(k,n-1)

def prob(n,p,r):
    assert 0 < p <= 1
    ans = C(n,n+r+1) * (p**r) * ((1-p)**n)
    return ans

def infoMeasure(n,p,r):
    assert  0 < p <= 1
    return -log2(prob(n,p,r))

def sumProb(N,p,r):
    assert 0 < p <= 1
    sum = 0
    for i in range(r,N+1):
        sum += prob(i,p,r)
    return sum

def approxEntropy(N,p,r):
    assert 0 < p <= 1
    sum = 0
    for i in range(r,N+1):
        sum += infoMeasure(i,p,r) * prob(i,p,r)
    return sum
