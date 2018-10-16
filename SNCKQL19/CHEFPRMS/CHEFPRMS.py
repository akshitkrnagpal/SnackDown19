import sys
sys.stdin = open('input.txt', 'r')

import math

def isSum(n):
    for i in range(1, math.ceil(n/2) + 1 ):
        if semiPrime(i) and semiPrime(n-i):
            return True
    return False

def prime(num):
    for i in range( 2, math.ceil(num/2) + 1 ):
        if num % i == 0:
            return False
    return True


def semiPrime(num):
    factors = []
    for i in range( 2, math.ceil(num/2) + 1 ):
        if num % i == 0 and prime(i):
            factors.append(i)
    return len(factors) == 2 and factors[0] * factors[1] == num

T = int(input())

for i in range(0, T):

    N = int(input())

    if isSum(N):
        print ('YES')
    else:
        print ('NO')
