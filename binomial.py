import math
import matplotlib.pyplot as plt


def calculateFactorial(n, acc=1):
    if n < 2:
        return acc
    return calculateFactorial(n - 1, acc * n)


def prob(n, p, N):
    pr: float = calculateFactorial(N) / (calculateFactorial(n) * calculateFactorial(N - n) * (2. ** N))
    return pr


def infoMeasure(n, p, N):
    l: float = -math.log2(prob(n, p, N))
    return l


def sumProb(n, p, N):
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, N)
    return sum


'''
Biện luận:

'''


def approxEntropy(n, p, N):
    sum = 0
    for i in range(0, N + 1):
        sum += -prob(i, p, N) * infoMeasure(i, p, N)
    return sum


stepP = 0.1
x = []
y = []
for i in range(1, 100):
    p = i * stepP
    x.append(p)
    y.append(approxEntropy(100, p, 100))

print(x, y)
plt.plot(x, y)
# if __name__ == "__main__":
#     _n = 7
#     _p = 0.5
#     _N = 17
#     print(prob(_n, _p, _N))
#     print(infoMeasure(_n, _p, _N))
#     print(sumProb(_n, _p, _N))
#     print(approxEntropy(_n, _p, _N))
