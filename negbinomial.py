import math


def calculateFactorial(n, acc=1):
    if n < 2:
        return acc
    return calculateFactorial(n - 1, acc * n)


def prob(n, p, N, r):
    pr: float = (calculateFactorial(N - 1) * math.pow(p, r) * math.pow(1 - p, N - r)) / (
                calculateFactorial(N - r) * calculateFactorial(r - 1))
    return pr


def infoMeasure(n, p, N, r):
    l: float = -math.log2(prob(n, p, N, r))
    return l


def sumProb(n, p, N, r):
    sum = 0
    for i in range(r, N + 1):
        sum += prob(i, p, N, r)
    return sum


'''
Biện luận:

'''


def approxEntropy(n, p, N, r):
    sum = 0
    for i in range(0, N + 1):
        sum += -prob(i, p, N, r) * infoMeasure(i, p, N, r)
        # sum += prob(i, p, N) * math.log2(prob(i, p, N))
    return sum


'''
'''
# if __name__ == "__main__":
#     _n = 7
#     _p = 0.7
#     _N = 5
#     _r = 3
#     print(prob(_n, _p, _N, _r))
#     print(infoMeasure(_n, _p, _N, _r))
#     print(sumProb(_n, _p, _N, _r))
#     print(approxEntropy(_n, _p, _N, _r))
