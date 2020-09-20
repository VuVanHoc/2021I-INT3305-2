import math


def prob(n, p):
    # pr: float = 1 / (math.pow(2, n))
    pr: float = 1 / (2. ** n)
    return pr


def infoMeasure(n, p):
    l: float = -math.log2(prob(n, p))
    return l


def sumProb(n, p):
    sum = 0
    for i in range(1, n + 1):
        sum += prob(i, p)
    return sum


'''
Bien luan:

'''


def approxEntropy(n, p):
    sum = 0
    for i in range(1, n + 1):
        sum += prob(i, p) * infoMeasure(i, p)
    return sum


'''
'''
N = 100
P = 0.5
print(prob(N, P))
print(infoMeasure(N, P))
print(sumProb(N, P))
print(approxEntropy(N, P))
