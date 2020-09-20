import math


def prob(n, p):
    # pr: float = 1 / (math.pow(2, n))
    pr: float = 1 / (2. ** n)
    return pr


def infoMeasure(n, p):
    l: float = -math.log2(prob(n, p))
    return l


def sumProb(N, p):
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p)
    return sum


'''
Bien luan:
Bằng thực nghiệm có thể thấy, khi N càng lớn, tổng xác suất các symbols từ 1 đến N tiến dần đến 1
Từ đó có thể sử dụng hàm sumProb để kiểm chứng tổng xác suất của phân bố geometic bằng 1.

'''


def approxEntropy(n, p):
    sum = 0
    for i in range(1, n + 1):
        sum += prob(i, p) * infoMeasure(i, p)
    return sum


'''
với giá trị p = 1/2, N = 5 => H = 1.78125
với giá trị p = 1/2, N = 10 => H = 1.98828125
với giá trị p = 1/2, N = 3 => H = 1.375
với giá trị p = 1/2, N = 9 => H = 1.978515625
'''
# if __name__ == "__main__":
#     print(approxEntropy(5, 0.5))
#     print(approxEntropy(10, 0.5))
#     print(approxEntropy(3, 0.5))
#     print(approxEntropy(9, 0.5))
