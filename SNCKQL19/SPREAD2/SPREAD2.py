import sys
sys.stdin = open('input.txt', 'r')

def days(N, A):
    days = 0
    prev_known = 0
    known = 1
    known_sum = 0

    while known < N:
        iter_sum = sum(A[prev_known:known])
        prev_known = known
        known += known_sum + iter_sum
        known_sum = known_sum + iter_sum
        days += 1
    return days

T = int(input())

for i in range(0, T):

    N = int(input())
    A = list(map(int, input().split()))

    D = days(N, A)

    print (D)
