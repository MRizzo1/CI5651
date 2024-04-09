import numpy as np
import random


def freivald(A, B, C, n):

    X = [random.randint(0, 1) for _ in range(n)]

    BX = np.zeros((n,))
    for i in range(n):
        for j in range(n):
            BX[i] += B[i, j] * X[j]

    ABX = np.zeros((n,))
    for i in range(n):
        for j in range(0, n):
            ABX[i] += A[i, j] * BX[j]

    CX = np.zeros((n,))
    for i in range(n):
        for j in range(0, n):
            CX[i] += C[i, j] * X[j]

    for i in range(n):
        if (int(ABX[i] - CX[i]) != 0):
            return False

    return True


def checkProduct(A, B, C, n, k):

    for _ in range(k):
        if not freivald(A, B, C, n):
            return False
    return True


def checkInverse(A, B, k=10):
    n = A.shape[0]
    I = np.identity(n)
    AB = checkProduct(A, B, I, n, k)
    BA = checkProduct(B, A, I, n, k)

    return AB and BA


A = np.matrix([[1, 2], [3, 4]])
B = np.matrix([[-2, 1], [3/2, -1/2]])
print(checkInverse(A, B))

A = np.matrix([[4, 3], [3, 2]])
B = np.matrix([[-2, 3], [3, -4]])
print(checkInverse(A, B))

A = np.matrix([[2, 3, 4], [-3, -3, -2], [-2, 1, -1]])
B = np.matrix([[5, 7, 6], [1, 6, -8], [-9, -8, 3]]) * (-1/23)
print(checkInverse(A, B, 20))
