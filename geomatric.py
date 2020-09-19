from math import log2

def prob(n,p):
    assert 0 < p <= 1
    return p * ((1-p)**(n-1))

def infoMeasure(n, p):
    assert 0 <p <= 1
    return -log2(prob(n,p))

def sumProb(N,p):
    assert 0 < p <= 1
    sum = 0
    for i in range(1,N+1):
        sum += prob(i,p)
    return sum
    """
        We can use sumProb() to verify that the sum of geometric distribution equals to 1
	    by giving different N from a small (say 1) to a large integer (say 1000) and observe 
	    how the results converge to 1
    """

def approxEntropy(N,p):
    assert 0 < p <= 1
    sum = 0
    for i in range(1,N+1):
        sum += infoMeasure(i,p)*prob(i,p)
    return sum
    """
        Approximates the Shannon entropy of geometric distribution with a very large N
    """
print(approxEntropy(100,1/2))

