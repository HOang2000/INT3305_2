from math import log2

def C(k,n):
    if k == 0 or k == n:
        return 1
    if k == 1:
        return n
    return C(k-1,n-1) + C(k,n-1)

def prob(n,p,N):
    assert 0 < p <= 1
    ans = C(n,N) * (p**n) * ((1-p)**(N-n))
    return ans

def infoMeasure(n,p,N):
    assert  0 < p <= 1
    return -log2(prob(n,p,N))

def sumProb(N,p):
    assert 0 < p <= 1
    sum = 0
    for i in range(1,N+1):
        sum += prob(i,p,N)
    return sum

def approxEntropy(N,p):
    assert 0 < p <= 1
    sum = 0
    for i in range(1,N+1):
        sum += infoMeasure(i,p,N) * prob(i,p,N)
    return sum

print(C(2,5))